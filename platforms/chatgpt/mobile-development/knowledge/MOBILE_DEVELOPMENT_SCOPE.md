# Mobile Development Scope

## Supported Technologies

- Android: Kotlin or Java, Android SDK, Jetpack Compose or Views, resources, manifests, permissions, Gradle, Android tests.
- iOS: Swift or Objective-C, SwiftUI or UIKit, Apple APIs, lifecycle, Xcode projects/workspaces, schemes, entitlements, resources, localization, iOS tests.
- Kotlin Multiplatform: source sets, shared logic, targets, dependency placement, `expect`/`actual`, interoperability, Compose Multiplatform only when present.
- Flutter: Dart, widgets, navigation, platform channels, packages, flavors, state management conventions, Flutter tests.
- React Native: TypeScript or JavaScript, navigation, Metro, package manager, native bridges, host projects, React Native tests.

## Platform Detection Evidence

Use supplied files and user context. Do not infer a platform from intent alone.

- Android evidence: `settings.gradle`, `build.gradle`, `build.gradle.kts`, `AndroidManifest.xml`, `src/main`, Gradle wrapper, Android resources.
- iOS evidence: `.xcodeproj`, `.xcworkspace`, `Package.swift`, schemes, `Info.plist`, entitlements, Swift or Objective-C sources.
- KMP evidence: Kotlin Multiplatform Gradle plugin, `kotlin {}` targets, `commonMain`, `androidMain`, `iosMain`, `expect`/`actual`.
- Flutter evidence: `pubspec.yaml`, `lib/`, `android/`, `ios/`, `flutter_test`, generated plugin registrants.
- React Native evidence: `package.json`, Metro config, `android/`, `ios/`, React Native dependencies, TypeScript or JavaScript app entry points.

If multiple technologies coexist, partition ownership by runtime and file boundary before giving advice.

## Native ChatGPT Capabilities

- Project instructions and uploaded project sources.
- Custom GPT instructions, conversation starters, and knowledge uploads.
- Eligible ChatGPT Skills created or uploaded through native ChatGPT interfaces.
- Optional Workspace Agents in eligible Business or Enterprise workspaces.
- Optional apps/connectors/custom MCP configured through ChatGPT with human approval.
- Web search only when enabled and needed for current official documentation.
- Code Interpreter and Data Analysis only when enabled and appropriate for non-sensitive supplied files.

## Unsupported In This Repository Package

- Automatic ChatGPT installation from repository folders.
- Repository-discovered `agents/`, `subagents/`, `hooks/`, `mcp/`, or `workflows/` directories.
- Fake GPT export JSON.
- Active app, connector, action, custom MCP, Slack, schedule, API trigger, or publication configuration.
- Shell, local builds, package-manager installation, simulators, devices, signing, notarization, store submission, deployment, or artifact upload without a separately enabled native tool and direct evidence.
- Executable source guards or hooks. ChatGPT instructions can require review, but cannot enforce repository-local command guards by themselves.

## Fail-Safe Rule

When capability, platform, ownership, tool access, or validation status is uncertain, classify it as unavailable or unknown, ask for the missing evidence, and do not simulate the capability.
