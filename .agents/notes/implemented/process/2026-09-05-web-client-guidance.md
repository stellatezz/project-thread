# Add web client guidance

Status: implemented

The user's request adds web as the twelfth public skill. This extends the [original suite decision](2026-09-05-engineering-ios-suite.md) and preserves its shared engineering and record ownership. The [plan](../../../../docs/roadmaps/skill-suite/plans/web-client.md) owns acceptance and distribution status.

Web guidance adapts to an existing framework and uses four conditional references for architecture/navigation, interaction quality, browser data/lifecycle, and verification/performance. A universal framework or global state library would impose choices without project evidence. Backend services and publishing retain their own scope.

The installer adds the new skill with the complete bundle. Legacy migration continues to target only the original eleven Project Thread names; no historical web skill is assumed. Existing evaluation artifacts remain unchanged. Implementation of this guidance does not establish that an adopting web application has passed browser, accessibility, device, or production checks.

The [evaluation result](../../../../evals/results/2026-09-05-web.md) records the bounded scenario review and bundle verification. The twelve-skill user installation is verified; app execution remains outside this task.
