"use strict";

const destructiveCommands = /\b(rm\s+-|git\s+(reset|clean|checkout|restore|rebase|push|pull|merge|commit|add|switch|branch)|xcrun\s+simctl\s+erase|adb\s+(shell\s+)?(reboot|root|remount|wipe|uninstall)|fastboot\s+oem|fastboot\s+flashing)\b/i;
const shellMetacharacters = /(\|\||&&|;|\||`|\$\(|<|>|>>|<<|\{|\})/;
const encodedCommand = /(%3[bB]|%7[cC]|%26|%60|\\x[0-9a-fA-F]{2}|\\u[0-9a-fA-F]{4})/;

function commandText(output) {
  const args = output && output.args;
  if (!args || typeof args !== "object") return "";
  return String(args.command || args.cmd || args.script || "");
}

exports.MobileCommandGuard = async () => ({
  "tool.execute.before": async (input, output) => {
    if ((input && input.tool) !== "bash") return;

    const command = commandText(output);
    if (!command.trim()) {
      throw new Error("Blocked malformed bash command.");
    }
    if (shellMetacharacters.test(command) || encodedCommand.test(command)) {
      throw new Error("Blocked chained, redirected, substituted, or encoded bash command.");
    }
    if (destructiveCommands.test(command)) {
      throw new Error("Blocked destructive or repository-mutating mobile command.");
    }
  }
});
