const SECRET_EXTENSIONS = new Set([
  ".keystore",
  ".jks",
  ".p12",
  ".p8",
  ".pem",
  ".key",
  ".mobileprovision",
  ".cer"
]);

const SECRET_SEGMENTS = new Set([
  ".ssh",
  ".gnupg",
  "credentials",
  "secrets",
  "private",
  "provisioning",
  "keystores"
]);

const PUBLIC_CLIENT_CONFIGS = new Set([
  "google-services.json",
  "GoogleService-Info.plist",
  "firebase_options.dart"
]);

function decodeForInspection(value) {
  let decoded = String(value || "");
  for (let i = 0; i < 2; i += 1) {
    try {
      const next = decodeURIComponent(decoded);
      if (next === decoded) break;
      decoded = next;
    } catch {
      break;
    }
  }
  return decoded.replace(/\\/g, "/");
}

function splitPath(value) {
  return decodeForInspection(value)
    .split("/")
    .filter(Boolean);
}

function extensionOf(value) {
  const name = splitPath(value).at(-1) || "";
  const dot = name.lastIndexOf(".");
  return dot >= 0 ? name.slice(dot) : "";
}

export function inspectSecretPath(rawPath) {
  const normalized = decodeForInspection(rawPath);
  const parts = splitPath(normalized);
  const fileName = parts.at(-1) || "";
  const lowered = parts.map((part) => part.toLowerCase());

  if (!normalized) {
    return { blocked: false, reason: "empty-path" };
  }
  if (PUBLIC_CLIENT_CONFIGS.has(fileName)) {
    return { blocked: false, reason: "public-mobile-client-config" };
  }
  if (lowered.includes("..") || normalized.includes("\0")) {
    return { blocked: true, reason: "malformed-or-traversal-path" };
  }
  if (fileName === ".env" || fileName.startsWith(".env.")) {
    return { blocked: true, reason: "environment-secret-file" };
  }
  if (SECRET_EXTENSIONS.has(extensionOf(normalized).toLowerCase())) {
    return { blocked: true, reason: "secret-or-signing-extension" };
  }
  if (lowered.some((part) => SECRET_SEGMENTS.has(part))) {
    return { blocked: true, reason: "secret-directory-segment" };
  }
  return { blocked: false, reason: "not-secret-path" };
}

function collectPathCandidates(value, results = []) {
  if (!value) return results;
  if (typeof value === "string") {
    results.push(value);
    return results;
  }
  if (Array.isArray(value)) {
    for (const item of value) collectPathCandidates(item, results);
    return results;
  }
  if (typeof value === "object") {
    for (const key of ["path", "file", "filePath", "cwd", "glob", "pattern"]) {
      collectPathCandidates(value[key], results);
    }
  }
  return results;
}

function toolName(input, output) {
  return String(input?.tool || output?.tool || input?.name || output?.name || "");
}

async function mobileSecretPathGuard() {
  return {
    "tool.execute.before": async (input, output) => {
      const tool = toolName(input, output);
      if (!/read|write|edit|glob|grep|search|open/i.test(tool)) return;
      const candidates = collectPathCandidates(output?.args || input?.args || {});
      for (const candidate of candidates) {
        const result = inspectSecretPath(candidate);
        if (result.blocked) {
          throw new Error(`mobile-secret-path-guard blocked ${candidate}: ${result.reason}`);
        }
      }
    }
  };
}

export default { id: "mobile-secret-path-guard", server: mobileSecretPathGuard };
