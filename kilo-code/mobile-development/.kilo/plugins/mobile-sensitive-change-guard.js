const SENSITIVE_FILENAMES = new Set([
  "AndroidManifest.xml",
  "Info.plist",
  "PrivacyInfo.xcprivacy",
  "network_security_config.xml",
  "Podfile.lock",
  "pubspec.lock",
  "package-lock.json",
  "yarn.lock",
  "pnpm-lock.yaml",
  "gradle.lockfile"
]);

const SENSITIVE_SUFFIXES = [
  ".entitlements",
  ".mobileprovision",
  ".keystore",
  ".jks",
  ".p12",
  ".p8",
  ".pem",
  ".key"
];

const SENSITIVE_CONFIG_PATTERNS = [
  /(^|\/)build\.gradle(\.kts)?$/i,
  /(^|\/)settings\.gradle(\.kts)?$/i,
  /(^|\/)gradle\.properties$/i,
  /(^|\/)Podfile$/i,
  /(^|\/)pubspec\.yaml$/i,
  /(^|\/)package\.json$/i,
  /(^|\/)metro\.config\.[cm]?js$/i,
  /(^|\/)app\.json$/i,
  /(^|\/)app\.config\.[jt]s$/i,
  /(^|\/)fastlane\//i
];

function normalizePath(value) {
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

export function inspectSensitiveChange(rawPath) {
  const path = normalizePath(rawPath);
  const name = path.split("/").filter(Boolean).at(-1) || "";
  if (!path) return { blocked: false, reason: "empty-path" };
  if (path.includes("\0") || path.split("/").includes("..")) {
    return { blocked: true, reason: "malformed-or-traversal-path" };
  }
  if (SENSITIVE_FILENAMES.has(name)) {
    return { blocked: true, reason: "sensitive-mobile-file" };
  }
  if (SENSITIVE_SUFFIXES.some((suffix) => name.endsWith(suffix))) {
    return { blocked: true, reason: "sensitive-signing-or-entitlement-file" };
  }
  if (SENSITIVE_CONFIG_PATTERNS.some((pattern) => pattern.test(path))) {
    return { blocked: true, reason: "sensitive-build-or-dependency-config" };
  }
  return { blocked: false, reason: "not-sensitive-change" };
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
    for (const key of ["path", "file", "filePath", "target", "cwd"]) {
      collectPathCandidates(value[key], results);
    }
  }
  return results;
}

async function mobileSensitiveChangeGuard() {
  return {
    "tool.execute.before": async (input, output) => {
      const tool = String(input?.tool || output?.tool || input?.name || output?.name || "");
      if (!/write|edit|patch|create|delete/i.test(tool)) return;
      const paths = collectPathCandidates(output?.args || input?.args || {});
      for (const path of paths) {
        const result = inspectSensitiveChange(path);
        if (result.blocked) {
          throw new Error(`mobile-sensitive-change-guard blocked ${path}: ${result.reason}`);
        }
      }
    }
  };
}

export default { id: "mobile-sensitive-change-guard", server: mobileSensitiveChangeGuard };
