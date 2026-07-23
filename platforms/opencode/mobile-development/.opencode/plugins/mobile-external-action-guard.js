"use strict";

const externalActionPattern = /\b(fastlane\s+(deliver|pilot|supply|upload|release)|gradle(w)?\s+.*(publish|upload|deploy|bundleRelease|assembleRelease)|\.\/gradlew\s+.*(publish|upload|deploy|bundleRelease|assembleRelease)|xcodebuild\s+.*(archive|-exportArchive)|notarytool|altool|firebase\s+(deploy|appdistribution|crashlytics:symbols:upload)|sentry-cli\s+(releases|upload)|eas\s+(submit|build|update)|appcenter\s+distribute|npm\s+publish|yarn\s+npm\s+publish|pod\s+trunk\s+push)\b/i;
const signingPattern = /\b(codesign|security\s+import|keytool\s+-genkey|jarsigner|apksigner\s+sign|xcodebuild\b.*CODE_SIGN_IDENTITY=|--signing-key|--keystore|--provisioning-profile)\b/i;
const networkWritePattern = /\b(curl|wget|http|gh|git)\b.*\b(-X\s*(POST|PUT|PATCH|DELETE)|--request\s*(POST|PUT|PATCH|DELETE)|upload|release|deploy|publish|submit)\b/i;

function commandText(output) {
  const args = output && output.args;
  if (!args || typeof args !== "object") return "";
  return String(args.command || args.cmd || args.script || "");
}

exports.MobileExternalActionGuard = async () => ({
  "tool.execute.before": async (input, output) => {
    if ((input && input.tool) !== "bash") return;

    const command = commandText(output);
    if (externalActionPattern.test(command) || signingPattern.test(command) || networkWritePattern.test(command)) {
      throw new Error("Blocked publishing, signing, upload, deployment, credential, or external write command.");
    }
  }
});
