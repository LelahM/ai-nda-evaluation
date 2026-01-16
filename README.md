# AI NDA Evaluation Project

AI-generated legal documents require systematic evaluation to identify risks, gaps, and inconsistencies that could expose clients to legal liability. This project demonstrates a rubric-based methodology for assessing AI-drafted Non-Disclosure Agreements (NDAs) by comparing baseline prompts against structured, constraint-driven prompts across three business scenarios.

## Problem Statement

Legal AI tools can generate contract drafts quickly, but outputs vary widely in quality, completeness, and enforceability. Without structured evaluation criteria, legal professionals cannot consistently assess whether an AI-generated draft is suitable as a starting point for review. This project addresses that gap by applying measurable, reproducible criteria to AI-generated NDAs.

## Workflow

This project follows a four-step evaluation process:

1. **Draft**: Generate NDAs using baseline (v1) and structured (v2) prompts
2. **Evaluate**: Score each draft against a standardized rubric (0-2 scale per category)
3. **Compare**: Identify improvements and remaining gaps between prompt versions
4. **Document**: Record findings with quoted evidence and risk flags for high-impact omissions

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

- Baseline prompts consistently omitted critical clauses: exclusions (0/3 drafts), return/destruction (0/3 drafts), and governing law (0/3 drafts)
- Structured prompts eliminated high-risk gaps in 100% of scenarios, improving average scores from 5/22 to 22/22 points
- All baseline outputs lacked injunctive relief provisions, creating unenforceable confidentiality obligations
- Industry-specific requirements (HIPAA compliance, international arbitration) appeared only when explicitly prompted
- Even improved drafts require attorney review for business-specific customization and jurisdiction-specific requirements

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