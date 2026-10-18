---
name: review-code
description: Read-only independent code/PR review that challenges an implementer's interpretation against original user intent, counterexamples, architecture, tests and observed acceptance. Use for "review code", "review PR", "audit this fix", "check Cursor's work" and merge-readiness review.
---

# Review code

Apply root `AGENTS.md` and `docs/ENGINEERING_CONTRACT.md`. Act as reviewer, not the implementing agent; do not silently edit, merge, deploy or approve consequential actions. If this is the same actor that implemented the change, report SELF-REVIEW, not independent acceptance.

1. Read original requirement, scope/constraints, predeclared acceptance (`docs/ACCEPTANCE_TEMPLATE.md` if used), current handoff and branch/PR. An implementer's recap is not a substitute for original intent.
2. Inspect full relevant diff and code path at exact SHA, old behaviour, tests and CI test discovery. Separate source-level reasoning from actual execution and deployment proof.
3. Challenge shortcuts: semantic verdict by regex/keywords/fuzzy overlap, output tailored to tests, guessed domain classifications, weakened gates, incomplete failure recovery, hidden stubs/fallbacks, tests mirroring implementation, runtime drift, permission/provenance/cost issues.
4. Exercise original failure, positive and counterexamples, new unseen and negated cases if semantic; otherwise proportional boundaries/integration/error cases. Compare raw observable output against expected behaviour. Do not let a model self-grade its output into acceptance.
5. Verify commands, environment/SHA, logs and real dependencies where required and authorized. Mark skipped work NOT RUN/BLOCKED, and distinguish TESTED, INTEGRATED, LIVE-VERIFIED and ACCEPTED. Do not run unsafe production changes.
6. Report prioritized findings with path, cause, scenario, impact, smallest fix and check. Verdict is REQUEST CHANGES for blocking failures, REVIEW PENDING for unobserved required gates, or ACCEPT only when independently supported at reviewed SHA. A code-review ACCEPT does not itself authorize merge/deploy. Lightweight SELF-CHECK is sufficient for trivial docs/cosmetic edits; label it.

Deliver one concise evidence-led review and bounded execution order, without altering criteria just to pass.
