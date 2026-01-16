# AI NDA Evaluation Project

AI-generated legal documents require systematic evaluation to identify risks, gaps, and inconsistencies that could expose clients to legal liability. This project evaluates AI-generated legal drafts using a structured rubric rather than trusting output quality.

**Disclaimer:** This repository is educational and does not provide legal advice.

## Problem Statement

Legal AI tools can generate contract drafts quickly, but outputs vary widely in quality, completeness, and enforceability. Without structured evaluation criteria, legal professionals cannot consistently assess whether an AI-generated draft is suitable as a starting point for review. This project addresses that gap by applying measurable, reproducible criteria to AI-generated NDAs.

## Workflow

This project follows a five-step evaluation process:

1. Generate NDA draft using baseline (v1) and structured (v2) prompts
2. Compare AI output to human-drafted template
3. Score each draft using 0/1/2 rubric (0 = missing, 1 = weak/risky, 2 = acceptable)
4. Flag high-risk omissions in critical categories
5. Document findings with quoted evidence and version comparison

## Repository Navigation

- **`prompts/`** - Baseline (v1) and structured (v2) prompts demonstrating prompt engineering impact
- **`templates/`** - Reference NDA template showing expected clause structure
- **`rubric/`** - Evaluation criteria (0 = missing, 1 = weak/risky, 2 = acceptable) in Markdown and JSON
- **`examples/`** - Three business scenarios with scenario metadata, AI outputs, and inline scoring
- **`evaluation/`** - Cross-scenario analysis, risk flag summaries, and pattern identification
  - See [`rubric_coverage_summary.md`](evaluation/rubric_coverage_summary.md) for comparative results
- **`report/`** - Case study analyzing methodology, results, and workflow implications
- **`scripts/`** - Python tools for automated draft generation and critique (educational use)

## Key Findings

- Eliminated critical omissions: Baseline prompts missed exclusions in 100% of drafts (0/3), structured prompts included them in 100% (3/3)
- Improved enforceability: All baseline outputs lacked injunctive relief provisions; structured prompts included them in all scenarios
- Reduced ambiguity: Baseline drafts averaged 5/22 points on clarity and completeness; structured prompts averaged 22/22 points
- Still missing: Even improved drafts require attorney review for jurisdiction-specific provisions and business-specific risk allocation

### Example: Why Scoring Matters

From Scenario 1, Draft 1 (Baseline):

> "Obligations do not apply to information that: Is publicly available through no breach of this Agreement"

**Score: 1** (Present but incomplete)  
**Why not 2**: This exclusion clause covers public information but omits independent development, prior knowledge, and lawful third-party disclosure, which increases enforceability risk and may prevent parties from using their own independently developed information.

Draft 2 (Structured) addressed this by including all five standard exclusions, earning a score of 2.

## Limitations and Responsible Use

This evaluation is designed for educational and research purposes only. AI-generated legal documents require professional legal review and should never be used without qualified attorney oversight. The project demonstrates evaluation methodologies rather than providing legal advice or production-ready software.

## Connection to Legal AI Tools

This evaluation framework aligns with the draft-review workflow used in legal AI platforms such as LexisNexis Protégé and Lexis+ AI. Those tools generate initial contract drafts based on user inputs and templates, which attorneys then review and customize. This project demonstrates how structured prompts improve initial draft quality and how rubric-based evaluation can systematically identify gaps requiring attorney review. The methodology supports integration of AI assistance into professional legal workflows while maintaining necessary human oversight and quality control.

## How to Add a New Scenario

To maintain consistency and reproducibility, new scenario evaluations should follow this structure:

1. **Scenario Metadata** - Parties, relationship type, NDA type, purpose, governing law
2. **Scenario Input** - Detailed business context and key considerations
3. **Prompt Used** - Reference to v1 and v2 prompt versions
4. **AI Outputs** - Complete Draft 1 (v1) and Draft 2 (v2) text
5. **Evaluation & Scoring** - Score each rubric category (0/1/2) with quoted evidence
6. **Risk Flags** - Highlight any high-risk missing clauses (score = 0)
7. **Version Comparison** - Summary of key improvements from v1 to v2
8. **Reproducibility Checklist** - Confirm all required elements are documented

See [`examples/scenario_1_startup_consulting.md`](examples/scenario_1_startup_consulting.md) for a complete reference implementation.