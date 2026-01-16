# AI NDA Evaluation Project

This project evaluates AI-assisted Non-Disclosure Agreement (NDA) drafting through systematic comparison of prompt versions across multiple business scenarios. The evaluation demonstrates a structured workflow for assessing legal AI outputs using human-centered review criteria, focusing on completeness, clarity, and risk identification rather than legal correctness.

## Repository Navigation

- **`prompts/`** - Contains versioned AI prompts (v1: baseline, v2: structured)
- **`templates/`** - Reference NDA template and source documentation  
- **`rubric/`** - Evaluation criteria in markdown and JSON formats
- **`examples/`** - Three business scenarios with AI-generated drafts
- **`evaluation/`** - Scoring results and analysis for each scenario
  - See [`rubric_coverage_summary.md`](evaluation/rubric_coverage_summary.md) for cross-scenario comparison
- **`report/`** - Comprehensive case study and findings
- **`scripts/`** - Optional automation tools for draft generation and critique

## Methodology

1. **Draft Generation**: Apply prompt versions to business scenarios using AI
2. **Systematic Evaluation**: Score outputs against structured rubric (0-2 scale)
3. **Comparative Analysis**: Identify improvements between prompt versions
4. **Documentation**: Capture findings and workflow insights

## Key Findings

- Structured prompts (v2) consistently improved clause completeness and legal precision
- AI outputs require systematic human review for risk identification and context validation
- Evaluation rubrics enable reproducible assessment of legal AI tools
- Workflow integration with existing legal technology platforms shows promise for professional adoption
- Critical gaps remain in nuanced risk assessment and jurisdiction-specific requirements

## Limitations and Responsible Use

This evaluation is designed for educational and research purposes only. AI-generated legal documents require professional legal review and should never be used without qualified attorney oversight. The project demonstrates evaluation methodologies rather than providing legal advice or production-ready software.

## Connection to Legal AI Tools

The workflow demonstrated here aligns with emerging legal AI drafting tools such as LexisNexis Protégé, providing a framework for evaluating and improving AI assistance in legal document preparation while maintaining necessary human oversight and professional responsibility.

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