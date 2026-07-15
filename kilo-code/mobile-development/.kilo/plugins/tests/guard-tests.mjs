import assert from "node:assert/strict";
import secretGuard, { inspectSecretPath } from "../mobile-secret-path-guard.js";
import shellGuard, { inspectShellCommand, tokenizeShell } from "../mobile-shell-safety-guard.js";
import releaseGuard, { inspectReleaseAction } from "../mobile-release-action-guard.js";
import sensitiveGuard, { inspectSensitiveChange } from "../mobile-sensitive-change-guard.js";

for (const plugin of [secretGuard, shellGuard, releaseGuard, sensitiveGuard]) {
  assert.equal(typeof plugin.id, "string");
  assert.equal(typeof plugin.server, "function");
}

assert.equal(inspectSecretPath("android/app/google-services.json").blocked, false);
assert.equal(inspectSecretPath("android/app/release.jks").blocked, true);
assert.equal(inspectSecretPath("../.env").blocked, true);
assert.equal(inspectSecretPath("%2e%2e/.ssh/id_rsa").blocked, true);

assert.deepEqual(tokenizeShell('sed -n "1,20p" "ios App/Info.plist"').tokens, [
  "sed",
  "-n",
  "1,20p",
  "ios App/Info.plist"
]);
assert.equal(inspectShellCommand('sed -n "1,20p" "ios App/Info.plist"').blocked, false);
assert.equal(inspectShellCommand("rg TODO src && rm -rf build").blocked, true);
assert.equal(inspectShellCommand("git reset --hard").blocked, true);
assert.equal(inspectShellCommand("python3 -c 'print(1)'").blocked, true);
assert.equal(inspectShellCommand("rg%20TODO").blocked, true);

assert.equal(inspectReleaseAction("flutter build apk --release").blocked, true);
assert.equal(inspectReleaseAction("xcrun altool --upload-app").blocked, true);
assert.equal(inspectReleaseAction("run unit tests").blocked, false);

assert.equal(inspectSensitiveChange("android/app/src/main/AndroidManifest.xml").blocked, true);
assert.equal(inspectSensitiveChange("ios/App/App.entitlements").blocked, true);
assert.equal(inspectSensitiveChange("lib/features/home/home_screen.dart").blocked, false);
assert.equal(inspectSensitiveChange("..\\signing\\release.keystore").blocked, true);

console.log("guard-tests passed");
