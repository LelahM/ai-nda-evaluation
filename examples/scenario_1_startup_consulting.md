# Scenario 1: Startup Consulting

## Scenario Metadata
- Parties: TechStart Inc. (Delaware corporation), BizAdvisors LLC (California LLC)
- Relationship: Consulting engagement
- NDA Type: Mutual
- Purpose: Go-to-market strategy development, requiring mutual exchange of confidential information
- Governing Law: California

## Scenario Input
TechStart Inc., an early-stage software startup, is seeking strategic consulting services from BizAdvisors LLC to develop their go-to-market strategy. The consulting engagement will require TechStart to share proprietary product roadmaps, customer data, financial projections, and technical specifications. BizAdvisors will also share their proprietary methodologies and market analysis techniques. Both parties need protection for their confidential information during the 6-month consulting engagement.

**Key Considerations:**
- Mutual confidentiality requirements
- Technology and business strategy information
- Limited engagement duration
- Need for information sharing with consulting team members

---

## Prompt Used
- Version 1: Baseline (see prompts/prompt_v1.txt)
- Version 2: Structured (see prompts/prompt_v2.txt)

---

## AI Output: Draft 1 (Prompt v1)

**NON-DISCLOSURE AGREEMENT**

This Non-Disclosure Agreement is made between TechStart Inc. and BizAdvisors LLC.

**Confidential Information**: Any information shared between the parties including business plans, customer lists, financial data, and proprietary methods.

**Obligations**: Both parties agree to keep all shared information confidential and not disclose it to third parties. Information should be used only for the consulting engagement.

**Term**: This agreement is effective for one year from signing.

**Remedies**: Breach of this agreement may result in legal action for damages.

The parties agree to the terms above.

_Signature lines for both parties_

---

## AI Output: Draft 2 (Prompt v2)

**NON-DISCLOSURE AGREEMENT**

This Non-Disclosure Agreement ("Agreement") is entered into on [DATE] between TechStart Inc., a Delaware corporation ("TechStart"), and BizAdvisors LLC, a California limited liability company ("BizAdvisors").

**1. PURPOSE**
The parties wish to explore a strategic consulting engagement for go-to-market strategy development and require mutual exchange of confidential information.

**2. DEFINITION OF CONFIDENTIAL INFORMATION**
"Confidential Information" means any non-public information disclosed by either party, including but not limited to: product roadmaps, technical specifications, customer data, financial projections, business strategies, proprietary methodologies, market analysis techniques, and any information marked as confidential or that would reasonably be considered confidential.

**3. PERMITTED AND PROHIBITED USES**
Each party may use Confidential Information solely for evaluating and conducting the consulting engagement. Neither party may disclose Confidential Information to third parties without prior written consent.

**4. OBLIGATIONS OF RECEIVING PARTY**
Each party agrees to:
- Maintain strict confidentiality of received information
- Use the same degree of care as for its own confidential information, but no less than reasonable care
- Limit access to employees and agents with a legitimate need to know
- Ensure such individuals are bound by confidentiality obligations

**5. EXCEPTIONS TO CONFIDENTIALITY**
Obligations do not apply to information that:
- Is publicly available through no breach of this Agreement
- Was rightfully known prior to disclosure
- Is received from a third party without breach
- Is required by law to be disclosed (with advance notice)
- Is independently developed without use of Confidential Information

**6. RETURN OR DESTRUCTION OF INFORMATION**
Upon termination or request, each party shall promptly return or destroy all Confidential Information and copies thereof.

**7. TERM AND TERMINATION**
This Agreement shall remain effective for two (2) years from the date of execution, with confidentiality obligations surviving termination.

**8. REMEDIES AND ENFORCEMENT**
Both parties acknowledge that breach would cause irreparable harm warranting injunctive relief in addition to monetary damages. This Agreement shall be governed by California law, with disputes resolved in California courts.

**9. GENERAL PROVISIONS**
This Agreement constitutes the entire understanding between parties. Amendments must be in writing. If any provision is unenforceable, the remainder shall remain in effect.

IN WITNESS WHEREOF, the parties execute this Agreement.

**TECHSTART INC.**                    **BIZADVISORS LLC**

_________________________           _________________________
Name: [Name]                         Name: [Name]
Title: [Title]                       Title: [Title] 
Date: [Date]                         Date: [Date]

---

## Evaluation & Scoring

### Parties and Purpose
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2 clearly identifies both parties and the consulting purpose ("entered into on [DATE] between TechStart Inc., a Delaware corporation... and BizAdvisors LLC..."). Draft 1 only lists names, not legal form or purpose.

### Confidential Information Definition
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2 provides a detailed definition ("means any non-public information disclosed by either party, including but not limited to: product roadmaps, technical specifications..."). Draft 1 is vague ("any information shared between the parties including business plans...").

### Exclusions
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2 lists standard exclusions ("publicly available... rightfully known... required by law..."). Draft 1 has no exclusions section.

### Obligations (Use and Care)
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2 details care and access ("maintain strict confidentiality... same degree of care... limit access..."). Draft 1: "agree to keep all shared information confidential" (no detail).

### Permitted Disclosures
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: "may not disclose... without prior written consent" and details on agents. Draft 1: "not disclose to third parties" (no exceptions or process).

### Term and Survival
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: "effective for two (2) years... obligations surviving termination". Draft 1: "effective for one year" (no survival language).

### Return/Destruction
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: "return or destroy all Confidential Information...". Draft 1: no mention of return or destruction.

### Remedies
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: "irreparable harm warranting injunctive relief...". Draft 1: "legal action for damages" (no injunctive relief).

### Governing Law and Venue
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: "governed by California law, with disputes resolved in California courts". Draft 1: no governing law or venue.

### No License / No Partnership / Assignment
- Score: 1 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: "entire understanding... amendments must be in writing..." (partial coverage). Draft 1: no such language.

### Clarity and Consistency
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: clear, numbered sections, defined terms, and consistent structure. Draft 1: basic, lacks structure.

---

## Risk Flags
- ⚠️ High Risk: Exclusions (Draft 1 = 0)
- ⚠️ High Risk: Return/Destruction (Draft 1 = 0)
- ⚠️ High Risk: Governing Law and Venue (Draft 1 = 0)
- ⚠️ High Risk: Term and Survival (Draft 1 = 1, not fully compliant)

---

## Version Comparison Summary
- Draft 2 (structured prompt) is complete, clear, and covers all rubric categories.
- Draft 1 (baseline prompt) is missing exclusions, return/destruction, governing law, and other key protections.
- Risk flags are present in Draft 1 for high-impact omissions.

---

## Reproducibility Checklist
- [x] Scenario input documented
- [x] Prompt version and text referenced
- [x] AI outputs included
- [x] Rubric applied with quoted evidence
- [x] Risk flags present if needed