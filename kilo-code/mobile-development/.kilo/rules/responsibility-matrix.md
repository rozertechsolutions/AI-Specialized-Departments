# Responsibility Matrix

| Responsibility | Owner | Reviewer | Native component |
| --- | --- | --- | --- |
| Architecture, modules, dependency direction, state, navigation, shared/platform boundaries, migrations | `mobile-architect` | `mobile-code-reviewer` | `.kilo/agents/mobile-architect.md` |
| Android Kotlin, SDK, Compose/Views, lifecycle, resources, manifests, permissions, Gradle, Android tests | `android-engineer` | `mobile-test-engineer`, `mobile-code-reviewer` | `.kilo/agents/android-engineer.md` |
| Swift, SwiftUI/UIKit, Apple APIs, lifecycle, Xcode, schemes, entitlements, resources, localization, iOS tests | `ios-engineer` | `mobile-test-engineer`, `mobile-code-reviewer` | `.kilo/agents/ios-engineer.md` |
| KMP source sets, shared logic, targets, dependency placement, `expect`/`actual`, interoperability | `kmp-engineer` | `mobile-architect`, `mobile-code-reviewer` | `.kilo/agents/kmp-engineer.md` |
| Dart, widgets, navigation, platform channels, packages, flavors, Flutter tests | `flutter-engineer` | `mobile-test-engineer`, `mobile-code-reviewer` | `.kilo/agents/flutter-engineer.md` |
| React Native, TypeScript/JavaScript, navigation, Metro, package manager, native bridges, RN tests | `react-native-engineer` | `mobile-test-engineer`, `mobile-code-reviewer` | `.kilo/agents/react-native-engineer.md` |
| Test strategy, test levels, fixtures, determinism, regression coverage, synchronization, flakiness, evidence | `mobile-test-engineer` | `mobile-code-reviewer` | `.kilo/agents/mobile-test-engineer.md` |
| Authentication, authorization, secure storage, network security, privacy, permissions, cryptography, WebViews, deep links, logging, telemetry, dependency risk | `mobile-security-reviewer` | `mobile-code-reviewer` | `.kilo/agents/mobile-security-reviewer.md` |
| Accessibility, adaptive layouts, orientations, dynamic text, focus, traversal, localization, interaction conventions, complete UI states | `mobile-ui-accessibility-reviewer` | `mobile-code-reviewer` | `.kilo/agents/mobile-ui-accessibility-reviewer.md` |
| Startup, rendering, memory, leaks, battery, background work, network/storage efficiency, binary size, profiling | `mobile-performance-reviewer` | `mobile-code-reviewer` | `.kilo/agents/mobile-performance-reviewer.md` |
| Versioning, variants, flavors, schemes, reproducibility, package preparation, signing prerequisites, store readiness | `mobile-release-engineer` | `mobile-security-reviewer`, `mobile-code-reviewer` | `.kilo/agents/mobile-release-engineer.md` |
| Independent final review of correctness, maintainability, regression risk, error handling, conventions, and evidence | `mobile-code-reviewer` | Human reviewer | `.kilo/agents/mobile-code-reviewer.md` |

No owner may perform independent final review of its own implementation.

