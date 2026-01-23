# Copilot Prompt: Generate Additional NDA Evaluation Scenarios

## Copy-Paste This Prompt into Copilot

```
Generate 20 additional NDA evaluation scenarios following the exact structure and quality standards of the existing scenarios in examples/.

REQUIRED STRUCTURE FOR EACH SCENARIO:

1. Scenario Metadata
   - Parties (with legal entity form: Corp, LLC, Partnership, etc.)
   - Relationship (consulting, vendor, partnership, employment, etc.)
   - NDA Type (mutual, unilateral)
   - Purpose (specific business context)
   - Governing Law (specific US state or country)

2. Scenario Input
   - 2-3 paragraph business context
   - Key Considerations (4-5 bulleted items)

3. Prompt Used
   - Version 1: Baseline (reference prompts/prompt_v1.txt)
   - Version 2: Structured (reference prompts/prompt_v2.txt)

4. AI Output: Draft 1 (Prompt v1)
   - Complete NDA text generated from baseline prompt
   - Should be 5-8 paragraphs, minimally structured
   - Missing key legal provisions (no exclusions, no governing law, vague obligations)

5. AI Output: Draft 2 (Prompt v2)
   - Complete NDA text generated from structured prompt
   - Should be 9-12 numbered sections with clear headings
   - Includes all standard NDA elements

6. Evaluation & Scoring
   - Score all 11 rubric categories (0/1/2)
   - Provide quoted evidence from drafts
   - Compare Draft 1 vs Draft 2 scores

7. Risk Flags
   - Flag high-risk omissions with ⚠️ symbol
   - Focus on: Exclusions, Return/Destruction, Governing Law, Term/Survival

8. Version Comparison Summary
   - 2-3 sentences on key improvements

9. Reproducibility Checklist
   - [x] checkboxes confirming all elements present

REQUIREMENTS:

- Use distinct company names (no repetition across 20 scenarios)
- Vary industries: tech, healthcare, finance, education, media, AI/ML, retail, manufacturing, real estate, legal services, consulting, biotech, energy, entertainment, SaaS, hardware, nonprofit
- Vary NDA types: mutual (60%), unilateral (40%)
- Vary complexity: simple 2-party (40%), multi-stakeholder (30%), international (20%), regulated industry (10%)
- Use different US states for governing law: NY, CA, DE, TX, MA, WA, IL, FL, VA, PA
- Draft 1 should consistently score low (0-3 out of 22 points)
- Draft 2 should consistently score high (18-22 out of 22 points)
- Keep language concise and professional (no marketing fluff)
- All dates should be 2025-2026

NAMING CONVENTION:
- scenario_4_[short_descriptor].md
- scenario_5_[short_descriptor].md
- ... through scenario_23_[short_descriptor].md

Example descriptors:
- employee_onboarding
- saas_vendor_evaluation
- merger_acquisition_diligence
- research_collaboration
- contractor_freelance
- manufacturing_supplier
- real_estate_development
- biotech_licensing
- media_production

OUTPUT FORMAT:
Create 20 separate markdown files in the examples/ directory, following the exact formatting of scenario_1_startup_consulting.md.

DO NOT:
- Add commentary outside the scenario structure
- Use vague language like "comprehensive" or "robust"
- Create unrealistic business contexts
- Repeat company names or party names
- Skip any required sections
- Generate scores inconsistent with draft quality (Draft 1 should score low, Draft 2 high)
```

## After Generation: Quality Check

Run these checks:

1. **Uniqueness**: `grep -r "Party Name" examples/*.md | sort | uniq -d` (should be empty)
2. **Structure**: Confirm all 20 files have 9 required sections
3. **Scoring**: Verify Draft 1 averages 0-3/22, Draft 2 averages 18-22/22
4. **Risk Flags**: Each scenario has 3-4 ⚠️ flags for Draft 1

## Notes

- This will generate scenarios 4-23, giving you 23 total scenarios
- Each scenario will take ~5-10 minutes for Copilot to generate properly
- You may want to generate in batches of 5 scenarios at a time
- Review each batch before proceeding to ensure quality consistency
