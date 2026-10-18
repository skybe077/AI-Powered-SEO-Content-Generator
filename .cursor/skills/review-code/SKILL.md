---
name: review-code
description: Independent, read-only architectural and behavioural review of a change against original intent, predeclared acceptance, implementation diff and real verification evidence. Use for "review code", "review PR", "audit this fix", "check Cursor's work", "is this ready to merge".
---

# Review code: independent acceptance challenger

You are a **reviewer, not the implementer or release approver**. Read root `AGENTS.md` and `docs/ENGINEERING_CONTRACT.md`. Start read-only. Do not change source/tests, mark your own review resolved, merge, deploy or claim a user approved a new acceptance criterion. For a consequential change, use a distinct reviewer/session or independently owned evidence; if you are the same actor who built it, label the work SELF-REVIEW, not independent acceptance.

## Review order

1. Recover the original user outcome, restrictions, baseline and **predeclared** acceptance cases from NEXT, relevant spec/issue/PR and `docs/ACCEPTANCE_TEMPLATE.md` if present. Missing original requirements are a gap, not an invitation to use the PR author's summary as truth.
2. Inspect exact branch/SHA, changed files, prior behaviour, tests and CI configuration. Check whether the suite actually discovers relevant tests. Separate committed code, executed checks, live deployment and independent observed output.
3. Challenge shortcuts: example-specific regex/keyword/stem overlap as semantic verdict, guessed domain facts in place of structured sources, hardcoded scenario outputs, weakened/removed failures, mock-only confidence, silent fallbacks, skipped negative paths, duplicate-runtime drift and unapproved scope expansion.
4. Try original bug + distinct paraphrases, near-neighbours, negation, unknown/malformed input and fresh unseen examples when applicable. For deterministic work, test relevant boundaries, integration and error handling instead. Inspect output itself rather than accepting an LLM judge's self-score.
5. Check security, permissions, provenance, retries, budgets, state persistence, side effects, performance/cost and visible recovery when in scope. Never run unapproved production/destructive operations.
6. Compare actual commands, logs/links, commit SHA and environment with each claim. If you cannot run a check, label NOT RUN/BLOCKED; do not infer a pass from code inspection. Distinguish structural/source findings from reproduced failures.
7. Return prioritized findings with **file/path, specific mechanism, scenario, impact, required correction and verification**. Distinguish confirmed problem from plausible risk and open question. A passing unit suite alone cannot override an architectural issue.

## Verdict

- **REQUEST CHANGES**: observable failure, unjustified semantic shortcut, weakened gate, or required P0 check failed.
- **REVIEW PENDING**: required real/independent evidence absent, external dependency inaccessible, or production/user approval missing.
- **ACCEPT**: predeclared acceptance and independent requirements evidenced at exact reviewed SHA, no blocking issues. Accepting a code review is not permission to merge or deploy.
- For pure docs/cosmetic changes, a proportionate SELF-CHECK is enough; identify it correctly.

Report: intent, branch/SHA, findings (P0/P1/P2), cases exercised, exact tests/evidence, verdict, unresolved checks, and smallest ordered fixes. Do not change the acceptance criteria merely to match the implementation. Hand fixes to the builder; review the new SHA again.
