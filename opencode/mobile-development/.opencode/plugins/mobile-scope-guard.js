"use strict";

const path = require("node:path");

const WRITE_TOOLS = new Set(["edit", "write", "apply_patch"]);
const PATH_FIELDS = new Set([
  "file",
  "filePath",
  "filepath",
  "path",
  "target",
  "targetPath",
  "target_file",
]);

function pathFields(args) {
  if (!args || typeof args !== "object") return [];
  const out = [];
  for (const [key, value] of Object.entries(args)) {
    if (PATH_FIELDS.has(key) && typeof value === "string") out.push(value);
  }
  return out;
}

function patchTargets(patch) {
  if (typeof patch !== "string") return [];
  const targets = [];
  for (const line of patch.split(/\r?\n/)) {
    let match = /^\*\*\* (?:Add|Update|Delete) File:\s+(.+?)\s*$/.exec(line);
    if (match) {
      targets.push(match[1]);
      continue;
    }
    match = /^\*\*\* Move to:\s+(.+?)\s*$/.exec(line);
    if (match) {
      targets.push(match[1]);
      continue;
    }
    match = /^(?:---|\+\+\+)\s+(?:(?:a|b)\/)?(.+?)\s*$/.exec(line);
    if (match && match[1] !== "/dev/null") targets.push(match[1]);
  }
  return targets;
}

function candidatePaths(tool, args) {
  const paths = pathFields(args);
  if (tool === "apply_patch" && args && typeof args === "object") {
    paths.push(...patchTargets(args.patch));
  }
  return paths;
}

function isQuoted(value) {
  return (
    (value.startsWith("\"") && value.endsWith("\"")) ||
    (value.startsWith("'") && value.endsWith("'"))
  );
}

function isExtendedWindowsPath(value) {
  return /^\\\\[.?]\\/.test(value);
}

function isWindowsAbsolute(value) {
  return path.win32.isAbsolute(value) || isExtendedWindowsPath(value);
}

function isPosixInsideWorkspace(cwd, value) {
  const workspace = path.posix.resolve(cwd.replace(/\\/g, "/"));
  const resolved = path.posix.resolve(workspace, value.replace(/\\/g, "/"));
  return resolved === workspace || resolved.startsWith(`${workspace}/`);
}

function isWindowsInsideWorkspace(cwd, value) {
  if (!path.win32.isAbsolute(cwd)) return false;
  const workspace = path.win32.resolve(cwd);
  const resolved = path.win32.resolve(workspace, value);
  const relative = path.win32.relative(workspace, resolved);
  return relative === "" || (!relative.startsWith("..") && !path.win32.isAbsolute(relative));
}

function containsTraversal(value) {
  const posixParts = value.replace(/\\/g, "/").split("/");
  const windowsParts = value.replace(/\//g, "\\").split("\\");
  return posixParts.includes("..") || windowsParts.includes("..");
}

function assertInScope(rawPath) {
  if (rawPath.includes("\0")) {
    throw new Error("Blocked null-byte path.");
  }
  if (rawPath !== rawPath.trim() || isQuoted(rawPath)) {
    throw new Error("Blocked quoted or padded mobile-development path.");
  }
  if (/\s/.test(rawPath)) {
    throw new Error("Blocked mobile-development path containing spaces.");
  }
  if (containsTraversal(rawPath)) {
    throw new Error(`Blocked traversal mobile-development path: ${rawPath}`);
  }

  const cwd = process.cwd();
  if (isWindowsAbsolute(rawPath)) {
    if (!isWindowsInsideWorkspace(cwd, rawPath)) {
      throw new Error(`Blocked out-of-scope mobile-development path: ${rawPath}`);
    }
    return;
  }
  if (path.posix.isAbsolute(rawPath)) {
    if (!isPosixInsideWorkspace(cwd, rawPath)) {
      throw new Error(`Blocked out-of-scope mobile-development path: ${rawPath}`);
    }
    return;
  }
  if (!isPosixInsideWorkspace(cwd, rawPath)) {
    throw new Error(`Blocked out-of-scope mobile-development path: ${rawPath}`);
  }
}

exports.MobileScopeGuard = async () => ({
  "tool.execute.before": async (input, output) => {
    const tool = input && input.tool;
    if (!WRITE_TOOLS.has(tool)) return;

    for (const raw of candidatePaths(tool, output && output.args)) {
      assertInScope(raw);
    }
  }
});
