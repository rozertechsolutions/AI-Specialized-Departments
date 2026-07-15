const CONTROL_OPERATORS = ["&&", "||", ";", "|", ">", "<", "`", "$("];
const DESTRUCTIVE_COMMANDS = new Set(["rm", "rmdir", "shred", "mkfs", "dd"]);
const DANGEROUS_GIT_SUBCOMMANDS = new Set([
  "commit",
  "push",
  "pull",
  "merge",
  "rebase",
  "reset",
  "clean",
  "checkout",
  "restore",
  "switch",
  "branch",
  "tag"
]);

function percentDecode(value) {
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
  return decoded;
}

export function tokenizeShell(command) {
  const tokens = [];
  let current = "";
  let quote = null;
  for (let i = 0; i < command.length; i += 1) {
    const char = command[i];
    if (quote) {
      if (char === quote) quote = null;
      else current += char;
      continue;
    }
    if (char === "'" || char === '"') {
      quote = char;
      continue;
    }
    if (/\s/.test(char)) {
      if (current) {
        tokens.push(current);
        current = "";
      }
      continue;
    }
    current += char;
  }
  if (quote) {
    return { tokens, malformed: true, reason: "unterminated-quote" };
  }
  if (current) tokens.push(current);
  return { tokens, malformed: false, reason: "ok" };
}

function hasControlOperator(command) {
  let quote = null;
  for (let i = 0; i < command.length; i += 1) {
    const char = command[i];
    if (quote) {
      if (char === quote) quote = null;
      continue;
    }
    if (char === "'" || char === '"') {
      quote = char;
      continue;
    }
    for (const op of CONTROL_OPERATORS) {
      if (command.slice(i, i + op.length) === op) return true;
    }
  }
  return false;
}

function looksEncoded(command) {
  const lowered = command.toLowerCase();
  return /%[0-9a-f]{2}/i.test(command) ||
    /\b(base64|xxd|openssl)\b.*\b(-d|-decode|enc)\b/i.test(command) ||
    /\b(python|python3|node|ruby|perl|php)\b\s+(-e|-c)\b/i.test(lowered);
}

export function inspectShellCommand(rawCommand) {
  const command = percentDecode(rawCommand).trim();
  if (!command) return { blocked: false, reason: "empty-command" };
  if (command.includes("\0")) return { blocked: true, reason: "nul-byte" };
  if (looksEncoded(rawCommand) || looksEncoded(command)) return { blocked: true, reason: "encoded-or-inline-execution" };
  if (hasControlOperator(command)) return { blocked: true, reason: "shell-control-operator" };

  const parsed = tokenizeShell(command);
  if (parsed.malformed) return { blocked: true, reason: parsed.reason };

  const [program, subcommand] = parsed.tokens;
  if (!program) return { blocked: false, reason: "empty-command" };
  const basename = program.split(/[\\/]/).at(-1);
  if (DESTRUCTIVE_COMMANDS.has(basename)) return { blocked: true, reason: "destructive-command" };
  if (basename === "git" && DANGEROUS_GIT_SUBCOMMANDS.has(subcommand || "")) {
    return { blocked: true, reason: "dangerous-git-subcommand" };
  }
  return { blocked: false, reason: "command-requires-policy" };
}

function commandFromArgs(args) {
  return args?.command || args?.cmd || args?.script || args?.input || "";
}

async function mobileShellSafetyGuard() {
  return {
    "tool.execute.before": async (input, output) => {
      const tool = String(input?.tool || output?.tool || input?.name || output?.name || "");
      if (!/bash|shell|terminal|exec|command/i.test(tool)) return;
      const command = commandFromArgs(output?.args || input?.args || {});
      const result = inspectShellCommand(command);
      if (result.blocked) {
        throw new Error(`mobile-shell-safety-guard blocked command: ${result.reason}`);
      }
    }
  };
}

export default { id: "mobile-shell-safety-guard", server: mobileShellSafetyGuard };
