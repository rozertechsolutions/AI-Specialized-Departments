"use strict";

const assert = require("node:assert/strict");
const { test } = require("node:test");
const { mkdtempSync } = require("node:fs");
const { tmpdir } = require("node:os");
const { join } = require("node:path");

const { MobileCommandGuard } = require("../mobile-command-guard.js");
const { MobileExternalActionGuard } = require("../mobile-external-action-guard.js");
const { MobileScopeGuard } = require("../mobile-scope-guard.js");
const { MobileSecretGuard } = require("../mobile-secret-guard.js");

async function handler(factory) {
  const plugin = await factory();
  assert.equal(typeof plugin["tool.execute.before"], "function");
  return plugin["tool.execute.before"];
}

async function assertBlocks(factory, input, output) {
  const before = await handler(factory);
  await assert.rejects(() => before(input, output), /Blocked|malformed|out-of-scope/);
}

async function assertAllows(factory, input, output) {
  const before = await handler(factory);
  await assert.doesNotReject(() => before(input, output));
}

function bash(command) {
  return [{ tool: "bash" }, { args: { command } }];
}

test("plugins register tool.execute.before", async () => {
  for (const factory of [MobileCommandGuard, MobileExternalActionGuard, MobileScopeGuard, MobileSecretGuard]) {
    await handler(factory);
  }
});

test("command guard blocks malformed, chained, encoded, device, and git commands", async () => {
  for (const command of [
    "",
    "git reset --hard HEAD",
    "rm -rf src",
    "adb reboot bootloader",
    "fastboot flashing unlock",
    "echo ok > file",
    "printf x | sh",
    "echo $(cat .env)",
    "echo %3B rm -rf src",
  ]) {
    await assertBlocks(MobileCommandGuard, ...bash(command));
  }
  await assertAllows(MobileCommandGuard, ...bash("./gradlew test"));
  await assertAllows(MobileCommandGuard, { tool: "read" }, { args: { path: "src/main.kt" } });
});

test("external action guard blocks signing, publishing, deployment, and upload", async () => {
  for (const command of [
    "./gradlew bundleRelease",
    "gradle publish",
    "xcodebuild archive -scheme App",
    "xcodebuild -exportArchive -archivePath App.xcarchive",
    "firebase deploy",
    "firebase appdistribution:distribute app.apk",
    "sentry-cli releases files 1 upload-sourcemaps build",
    "eas build --platform ios",
    "eas submit --platform android",
    "appcenter distribute release",
    "npm publish",
    "curl -X POST --upload-file app.apk https://example.com/upload",
    "gh release upload v1 app.apk",
    "codesign --sign Developer App.app",
    "security import cert.p12",
  ]) {
    await assertBlocks(MobileExternalActionGuard, ...bash(command));
  }
  await assertAllows(MobileExternalActionGuard, ...bash("./gradlew test"));
});

test("scope guard blocks traversal, absolute outside paths, Windows paths, and null bytes", async () => {
  const cwd = process.cwd();
  const root = mkdtempSync(join(tmpdir(), "opencode-mobile-"));
  process.chdir(root);
  try {
    await assertBlocks(MobileScopeGuard, { tool: "write" }, { args: { path: "../outside.txt" } });
    await assertBlocks(MobileScopeGuard, { tool: "edit" }, { args: { file: "/tmp/outside.txt" } });
    await assertBlocks(MobileScopeGuard, { tool: "apply_patch" }, { args: { patch: "src/../../outside.txt" } });
    await assertBlocks(MobileScopeGuard, { tool: "write" }, { args: { path: "C:\\Users\\name\\.ssh\\id_rsa" } });
    await assertBlocks(MobileScopeGuard, { tool: "write" }, { args: { path: "src/main.kt\0" } });
    await assertAllows(MobileScopeGuard, { tool: "write" }, { args: { path: "src/main.kt" } });
    await assertAllows(MobileScopeGuard, { tool: "bash" }, { args: { command: "python3 -m unittest" } });
  } finally {
    process.chdir(cwd);
  }
});

test("secret guard blocks real secrets but allows placeholders and public mobile client config", async () => {
  await assertBlocks(MobileSecretGuard, { tool: "write" }, { args: { content: 'api_key="realistic-secret-value-12345"' } });
  await assertBlocks(MobileSecretGuard, { tool: "apply_patch" }, { args: { patch: "-----BEGIN PRIVATE KEY-----" } });
  await assertBlocks(MobileSecretGuard, { tool: "bash" }, { args: { command: "echo ghp_abcdefghijklmnopqrstuvwxyz1234567890" } });
  await assertAllows(MobileSecretGuard, { tool: "write" }, { args: { content: "API_KEY=${OPENAI_API_KEY}\nTOKEN=YOUR_ACCESS_TOKEN" } });
  await assertAllows(MobileSecretGuard, { tool: "write" }, { args: { file: "google-services.json", content: '{"current_key":"AIzaSyDUMMYEXAMPLEPLACEHOLDER123456789"}' } });
  await assertAllows(MobileSecretGuard, { tool: "write" }, { args: { file: "GoogleService-Info.plist", content: "<key>API_KEY</key><string>YOUR_API_KEY</string>" } });
});
