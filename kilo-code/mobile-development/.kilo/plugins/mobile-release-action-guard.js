const RELEASE_TERMS = [
  "publish",
  "upload",
  "submit",
  "deploy",
  "distribute",
  "release",
  "promote",
  "rollout",
  "deliver",
  "supply",
  "pilot",
  "firebase appdistribution",
  "appdistribution:distribute",
  "gradle-play-publisher",
  "fastlane"
];

const SIGNING_TERMS = [
  "codesign",
  "notarytool",
  "xcrun altool",
  "apksigner",
  "jarsigner",
  "signingconfig",
  "match",
  "cert",
  "sigh"
];

function normalize(value) {
  return String(value || "")
    .replace(/\\/g, "/")
    .replace(/\s+/g, " ")
    .toLowerCase();
}

export function inspectReleaseAction(value) {
  const text = normalize(value);
  if (!text) return { blocked: false, reason: "empty" };
  for (const term of SIGNING_TERMS) {
    if (text.includes(term)) return { blocked: true, reason: "real-signing-action" };
  }
  for (const term of RELEASE_TERMS) {
    if (text.includes(term)) return { blocked: true, reason: "publication-or-distribution-action" };
  }
  if (/\b(appstore|play\s+store|testflight|play\s+console)\b/.test(text)) {
    return { blocked: true, reason: "store-action" };
  }
  if (/\b(pay|purchase|subscribe|billing)\b/.test(text)) {
    return { blocked: true, reason: "financial-action" };
  }
  return { blocked: false, reason: "not-release-action" };
}

function collectText(value, results = []) {
  if (!value) return results;
  if (typeof value === "string") {
    results.push(value);
    return results;
  }
  if (Array.isArray(value)) {
    for (const item of value) collectText(item, results);
    return results;
  }
  if (typeof value === "object") {
    for (const item of Object.values(value)) collectText(item, results);
  }
  return results;
}

async function mobileReleaseActionGuard() {
  return {
    "tool.execute.before": async (input, output) => {
      const values = collectText(output?.args || input?.args || {});
      for (const value of values) {
        const result = inspectReleaseAction(value);
        if (result.blocked) {
          throw new Error(`mobile-release-action-guard blocked action: ${result.reason}`);
        }
      }
    }
  };
}

export default { id: "mobile-release-action-guard", server: mobileReleaseActionGuard };
