# Performance, Capacity and Efficiency Workflows

## performance-readiness
1. Capture targets, workload, dependencies, telemetry, capacity, autoscaling, and regression criteria.
2. Identify missing assumptions and evidence without running tests.

## load-test-design
1. Define scenario, load profile, data shape, safety limits, environment assumptions, success criteria, and approvals.
2. Do not execute tests.

## capacity-review
1. Review demand forecast, uncertainty, seasonality, failure headroom, saturation points, and owner.
2. Return gaps and static recommendations.

## autoscaling-review
1. Review signals, min/max, stabilization, cooldown, limits, failure modes, and rollback.
2. Do not change autoscaling policies.

## performance-regression-analysis
1. Define baseline evidence, change context, regression threshold, suspected bottlenecks, and unverified assumptions.
2. Do not invent benchmark results.

## resource-efficiency-improvement
1. Review requests, limits, utilization assumptions, scaling, caching, queueing, and graceful degradation.
2. Hand financial optimization to FinOps when primary.
