---
name: testing-browser-compatibility
description: Define and assess risk-based tests and browser compatibility.
---

# Testing Browser Compatibility

Use this skill when mapping acceptance criteria to verification, browser coverage, regression risk, or unexecuted checks. Do not use it to claim tests passed without direct command or browser evidence.

1. Map acceptance criteria to unit, integration, contract, component, end-to-end, accessibility, security, and regression checks as applicable.
2. Use the repository's existing tools and supported browser policy; do not invent coverage thresholds.
3. Include negative paths, authorization boundaries, race conditions, retries, time zones, localization, and responsive states where relevant.
4. Do not claim tests passed unless direct evidence is available.
5. Return the test matrix, evidence status, gaps, residual risk, and evidence gates.
