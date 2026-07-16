"use strict";

const privateKeyMarker = "-----BEGIN [A-Z ]+" + "PRIVATE" + " KEY-----";
const jwtLikeValue = "[A-Za-z0-9_\\-]{32,}\\.[A-Za-z0-9_\\-]{16,}\\.[A-Za-z0-9_\\-]{16,}";
const longHexValue = "[A-Fa-f0-9]{40,}";
const githubTokenValue = "gh[pousr]_[A-Za-z0-9]{36,}|github_pat_[A-Za-z0-9_]{40,}";
const likelySecretValuePattern = new RegExp(`\\b(${privateKeyMarker}|${jwtLikeValue}|${longHexValue}|${githubTokenValue})\\b`);
const assignmentSecretPattern = /\b(api[_-]?key|access[_-]?token|auth[_-]?token|client[_-]?secret|private[_-]?key|password|passwd|secret|keystore[_-]?password)\b\s*[:=]\s*["']?([A-Za-z0-9_./+=-]{12,})["']?/i;
const placeholderPattern = /(\$\{[^}]+}|YOUR_[A-Z0-9_]+|example|sample|placeholder|dummy|test)/i;

function flatten(input) {
  if (typeof input === "string") return input;
  if (!input || typeof input !== "object") return "";
  const seen = new Set();
  const chunks = [];
  const stack = [input];
  while (stack.length) {
    const current = stack.pop();
    if (!current || typeof current !== "object" || seen.has(current)) continue;
    seen.add(current);
    for (const [key, value] of Object.entries(current)) {
      chunks.push(String(key));
      if (typeof value === "string") chunks.push(value);
      else if (value && typeof value === "object") stack.push(value);
    }
  }
  return chunks.join("\n");
}

exports.MobileSecretGuard = async () => ({
  "tool.execute.before": async (input, output) => {
    const tool = input && input.tool;
    if (!["edit", "write", "apply_patch", "bash"].includes(tool)) return;

    const text = flatten(output && output.args);
    if (likelySecretValuePattern.test(text)) {
      throw new Error("Blocked possible secret or credential material in tool input.");
    }
    const assignment = assignmentSecretPattern.exec(text);
    if (assignment && !placeholderPattern.test(assignment[2])) {
      throw new Error("Blocked possible hardcoded secret assignment in tool input.");
    }
  }
});
