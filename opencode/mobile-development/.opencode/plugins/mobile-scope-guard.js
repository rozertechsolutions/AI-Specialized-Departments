"use strict";

const path = require("node:path");

function values(input) {
  if (!input || typeof input !== "object") return [];
  const out = [];
  const stack = [input];
  while (stack.length) {
    const current = stack.pop();
    if (!current || typeof current !== "object") continue;
    for (const value of Object.values(current)) {
      if (typeof value === "string") out.push(value);
      else if (value && typeof value === "object") stack.push(value);
    }
  }
  return out;
}

function isPathLike(value) {
  return value.includes("/") || value.includes("\\") || value.startsWith(".") || /^[A-Za-z]:[\\/]/.test(value);
}

exports.MobileScopeGuard = async () => ({
  "tool.execute.before": async (input, output) => {
    const tool = input && input.tool;
    if (!["edit", "write", "apply_patch"].includes(tool)) return;

    const cwd = process.cwd();
    const allowed = path.resolve(cwd);
    for (const raw of values(output && output.args)) {
      if (!isPathLike(raw)) continue;
      if (raw.includes("\0")) {
        throw new Error("Blocked null-byte path.");
      }
      const resolved = path.resolve(cwd, raw);
      if (resolved !== allowed && !resolved.startsWith(allowed + path.sep)) {
        throw new Error(`Blocked out-of-scope mobile-development path: ${raw}`);
      }
    }
  }
});
