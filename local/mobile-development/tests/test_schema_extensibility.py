import copy
import json
import re
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_MANIFEST_COUNT = 53


class SchemaValidationError(AssertionError):
    pass


def load_yaml(path):
    script = "require 'yaml'; require 'json'; puts JSON.generate(YAML.load_file(ARGV[0]))"
    result = subprocess.run(
        ["ruby", "-e", script, str(path)],
        check=True,
        capture_output=True,
        text=True,
    )
    return json.loads(result.stdout)


def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def resolve_ref(schema, ref):
    if not ref.startswith("#/"):
        raise SchemaValidationError(f"Unsupported external ref: {ref}")
    node = schema
    for part in ref[2:].split("/"):
        node = node[part]
    return node


def check_type(value, expected):
    if isinstance(expected, list):
        return any(check_type(value, item) for item in expected)
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    raise SchemaValidationError(f"Unsupported type: {expected}")


def stable(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def validate(value, subschema, root_schema, path="$"):
    if "$ref" in subschema:
        return validate(value, resolve_ref(root_schema, subschema["$ref"]), root_schema, path)

    if "oneOf" in subschema:
        matches = 0
        last_error = None
        for option in subschema["oneOf"]:
            try:
                validate(value, option, root_schema, path)
                matches += 1
            except SchemaValidationError as exc:
                last_error = exc
        if matches != 1:
            raise SchemaValidationError(f"{path}: expected exactly one matching schema, got {matches}; last error: {last_error}")

    if "const" in subschema and value != subschema["const"]:
        raise SchemaValidationError(f"{path}: expected {subschema['const']!r}, got {value!r}")

    if "enum" in subschema and value not in subschema["enum"]:
        raise SchemaValidationError(f"{path}: {value!r} is not one of {subschema['enum']!r}")

    if "type" in subschema and not check_type(value, subschema["type"]):
        raise SchemaValidationError(f"{path}: expected type {subschema['type']!r}, got {type(value).__name__}")

    if isinstance(value, str):
        if "minLength" in subschema and len(value) < subschema["minLength"]:
            raise SchemaValidationError(f"{path}: string is too short")
        if "pattern" in subschema and re.search(subschema["pattern"], value) is None:
            raise SchemaValidationError(f"{path}: {value!r} does not match {subschema['pattern']!r}")

    if isinstance(value, list):
        if "minItems" in subschema and len(value) < subschema["minItems"]:
            raise SchemaValidationError(f"{path}: array has too few items")
        if subschema.get("uniqueItems"):
            seen = set()
            for item in value:
                encoded = stable(item)
                if encoded in seen:
                    raise SchemaValidationError(f"{path}: array items are not unique")
                seen.add(encoded)
        if "items" in subschema:
            for index, item in enumerate(value):
                validate(item, subschema["items"], root_schema, f"{path}[{index}]")

    if isinstance(value, dict):
        if "minProperties" in subschema and len(value) < subschema["minProperties"]:
            raise SchemaValidationError(f"{path}: object has too few properties")
        for key in subschema.get("required", []):
            if key not in value:
                raise SchemaValidationError(f"{path}: missing required property {key!r}")
        if "propertyNames" in subschema:
            for key in value:
                validate(key, subschema["propertyNames"], root_schema, f"{path}.{key}")
        properties = subschema.get("properties", {})
        for key, item in value.items():
            if key in properties:
                validate(item, properties[key], root_schema, f"{path}.{key}")
            elif subschema.get("additionalProperties") is False:
                raise SchemaValidationError(f"{path}: unexpected property {key!r}")
            elif isinstance(subschema.get("additionalProperties"), dict):
                validate(item, subschema["additionalProperties"], root_schema, f"{path}.{key}")


class SchemaExtensibilityTests(unittest.TestCase):
    def validate_manifest(self, manifest):
        schema_path = (manifest["_path"].parent / manifest["schema"]).resolve()
        self.assertTrue(schema_path.is_file(), f"Missing schema for {manifest['_path']}: {schema_path}")
        schema = load_json(schema_path)
        data = {key: value for key, value in manifest.items() if key != "_path"}
        validate(data, schema, schema)

    def load_manifests(self):
        manifests = []
        for path in sorted(ROOT.glob("**/*.yaml")):
            data = load_yaml(path)
            data["_path"] = path
            manifests.append(data)
        return manifests

    def test_all_existing_manifests_validate(self):
        manifests = self.load_manifests()
        self.assertEqual(EXPECTED_MANIFEST_COUNT, len(manifests))
        for manifest in manifests:
            with self.subTest(path=manifest["_path"].relative_to(ROOT)):
                self.validate_manifest(manifest)

    def test_namespaced_extension_is_accepted(self):
        provider = load_yaml(ROOT / "providers/ollama.example.yaml")
        provider["_path"] = ROOT / "providers/ollama.example.yaml"
        provider["extensions"] = {"vendor_runtime": {"display_name": "Ollama"}}
        self.validate_manifest(provider)

    def test_unknown_top_level_core_property_is_rejected(self):
        tool = load_yaml(ROOT / "tools/project-read.yaml")
        tool["_path"] = ROOT / "tools/project-read.yaml"
        tool["remote_use_requires_explicit_consent"] = True
        with self.assertRaises(SchemaValidationError):
            self.validate_manifest(tool)

    def test_malformed_core_field_is_rejected(self):
        tool = load_yaml(ROOT / "tools/project-read.yaml")
        tool["_path"] = ROOT / "tools/project-read.yaml"
        tool["allowed_operations"] = "read_files"
        with self.assertRaises(SchemaValidationError):
            self.validate_manifest(tool)

    def test_extension_cannot_bypass_provider_security(self):
        provider = load_yaml(ROOT / "providers/ollama.example.yaml")
        provider["_path"] = ROOT / "providers/ollama.example.yaml"
        provider["remote_use_requires_explicit_consent"] = False
        provider["extensions"] = {"vendor_runtime": {"remote_use_requires_explicit_consent": True}}
        with self.assertRaises(SchemaValidationError):
            self.validate_manifest(provider)

    def test_provider_api_key_must_remain_unconfigured(self):
        provider = load_yaml(ROOT / "providers/openai-compatible.example.yaml")
        provider["_path"] = ROOT / "providers/openai-compatible.example.yaml"
        provider["configuration"]["api_key"] = "secret"
        with self.assertRaises(SchemaValidationError):
            self.validate_manifest(provider)

    def test_extension_cannot_enable_mcp_server(self):
        mcp = load_yaml(ROOT / "mcp/servers.example.yaml")
        mcp["_path"] = ROOT / "mcp/servers.example.yaml"
        mcp["servers"] = copy.deepcopy(mcp["servers"])
        mcp["servers"][0]["enabled"] = True
        mcp["servers"][0]["extensions"] = {"host_local": {"enabled": False}}
        with self.assertRaises(SchemaValidationError):
            self.validate_manifest(mcp)


if __name__ == "__main__":
    unittest.main()
