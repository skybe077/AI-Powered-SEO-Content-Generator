# Behavioural acceptance record (copy for a meaningful change)

Use for semantic logic, consequential code changes, integrations and release work. Keep it short for small changes. Predeclare expected results **before** fixing the code; do not retroactively rewrite expected outcomes to fit implementation.

## Goal and boundary
- User outcome:
- Non-goals / authority boundary:
- Changed environment/runtime:
- What failure looks like, and visible recovery:

## Acceptance cases
| ID | Input / scenario | Expected observed outcome | Why it discriminates | Result / evidence |
| --- | --- | --- | --- | --- |
| A1 | Original failure / primary case | | | NOT RUN |
| A2 | Different formulation, same intent | | | NOT RUN |
| A3 | Different formulation, same intent | | | NOT RUN |
| A4 | Different formulation, same intent | | | NOT RUN |
| N1 | Similar words, different intent | | | NOT RUN |
| N2 | Similar words, different intent | | | NOT RUN |
| E1 | Negation / distracting words / ambiguity | | | NOT RUN |
| F1 | Failure, missing data or unavailable dependency | | | NOT RUN |
| U1 | Fresh unseen example, reviewer-selected | | | NOT RUN |

For deterministic/nonsemantic tasks, replace this matrix with relevant edge, boundary and integration cases. If a row is genuinely inapplicable, say why; do not create artificial tests solely to tick a box.

## Evidence ledger
| Check | Environment / actual command or observation | Commit SHA / deployed version | PASS / FAIL / NOT RUN / BLOCKED | Link or saved result |
| --- | --- | --- | --- | --- |
| Unit / typecheck / lint | | | NOT RUN | |
| Integration (real dependency where required) | | | NOT RUN | |
| E2E / real user path | | | NOT RUN | |
| Failure / recovery | | | NOT RUN | |
| Cost / latency (if relevant) | | | NOT RUN | |
| Independent output review | Reviewer identity or independent check | | REVIEW PENDING | |

## Design review
- Which facts use deterministic/authoritative checks?
- Which judgments genuinely require semantics, and where is their bounded contract?
- Are regex/keywords only guardrails? For any gate: objective property, false positives/negatives, reason to avoid semantic judgment:
- Could this change pass because the test's exact sentence was hardcoded?
- Existing behaviour at risk, including other runtimes and negative cases:
- Any test weakened, removed or changed? Why and who approved the acceptance change?
- Unknowns / skipped real checks / safety or authority implications:

## Decision
- Implementation status: DEFINED / IMPLEMENTED / TESTED / INTEGRATED / LIVE-VERIFIED / ACCEPTED / BLOCKED
- Reviewer verdict: ACCEPT / REQUEST CHANGES / REVIEW PENDING (evidence):
- Merge or deployment gate: PASS / FAIL / PENDING, and why:
- Explicit human approval where required:
- Bounded next action / owner:
