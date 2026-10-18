"""Static policy-wiring check only; not a product test or independent acceptance."""
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent
REQUIRED={"AGENTS.md":("ENGINEERING_CONTRACT.md","REVIEW PENDING"),"docs/ENGINEERING_CONTRACT.md":("Project-specific non-negotiables","REVIEW PENDING"),"docs/ACCEPTANCE_TEMPLATE.md":("Acceptance cases","Evidence ledger"),".github/pull_request_template.md":("Independent review","Open gates"),".cursor/rules/engineering-contract.mdc":("alwaysApply: true","ENGINEERING_CONTRACT.md"),".cursor/skills/review-code/SKILL.md":("SELF-REVIEW","REQUEST CHANGES"),".agents/skills/review-code/SKILL.md":("SELF-REVIEW","REVIEW PENDING"),"CLAUDE.md":("ENGINEERING_CONTRACT.md",),"GEMINI.md":("ENGINEERING_CONTRACT.md",),".github/copilot-instructions.md":("ENGINEERING_CONTRACT.md",)}
errors=[]
for name, tokens in REQUIRED.items():
 p=ROOT/name
 if not p.is_file(): errors.append(f"Missing: {name}");continue
 body=p.read_text(encoding="utf-8-sig")
 for token in tokens:
  if token not in body: errors.append(f"Missing reference in {name}: {token}")
if errors:
 print("\n".join(errors));raise SystemExit(1)
print("Agent contract wiring present. Does NOT verify runtime, semantic quality, real integrations, independent review or release approval.")
