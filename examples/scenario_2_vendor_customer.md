# Scenario 2: Vendor-Customer Relationship

## Scenario Metadata
- Parties: MedDevice Corp (Delaware corporation), CloudSoft Solutions Inc. (Texas corporation)
- Relationship: Vendor evaluation
- NDA Type: Primarily unilateral (MedDevice → CloudSoft)
- Purpose: Vendor evaluation for custom software platform development for medical device data management
- Governing Law: Delaware

## Scenario Input
MedDevice Corp, a medical device manufacturer, is evaluating CloudSoft Solutions as a potential vendor for a custom software platform to manage patient data and device monitoring. The evaluation process requires CloudSoft to access MedDevice's existing system architecture, regulatory requirements, patient data schemas, and clinical workflow specifications. This is primarily a unilateral disclosure from MedDevice to CloudSoft, with potential for limited reciprocal sharing of CloudSoft's development methodologies.

**Key Considerations:**
- Primarily unilateral confidentiality (MedDevice → CloudSoft)
- Healthcare data and regulatory compliance requirements
- Vendor evaluation context with potential for competitive bidding
- HIPAA and medical device regulatory considerations

---

## Prompt Used
- Version 1: Baseline (see prompts/prompt_v1.txt)
- Version 2: Structured (see prompts/prompt_v2.txt)

---

## AI Output: Draft 1 (Prompt v1)

**NON-DISCLOSURE AGREEMENT**

This agreement is between MedDevice Corp and CloudSoft Solutions for software evaluation.

**Confidential Information**: All information shared by MedDevice Corp including technical specifications, patient data requirements, and system details.

**Use Restrictions**: CloudSoft Solutions agrees to use the information only for preparing their software proposal and will not share it with competitors or other parties.

**Duration**: This agreement lasts for 180 days from signing.

**Legal Action**: If CloudSoft Solutions breaches this agreement, MedDevice Corp can take legal action.

Both parties sign below to agree to these terms.

---

## AI Output: Draft 2 (Prompt v2)

**NON-DISCLOSURE AGREEMENT**

This Non-Disclosure Agreement ("Agreement") is entered into on [DATE] between MedDevice Corp, a Delaware corporation ("MedDevice"), and CloudSoft Solutions Inc., a Texas corporation ("CloudSoft").

**1. PURPOSE**
MedDevice seeks to evaluate CloudSoft as a potential vendor for custom software development services for medical device data management, requiring disclosure of confidential technical and regulatory information.

**2. DEFINITION OF CONFIDENTIAL INFORMATION**
"Confidential Information" means all non-public information disclosed by MedDevice, including but not limited to: system architecture specifications, patient data schemas, clinical workflow requirements, regulatory compliance documentation, existing software configurations, security protocols, and any healthcare-related data or processes. CloudSoft may also share limited proprietary development methodologies, which shall be treated as Confidential Information.

**3. PERMITTED AND PROHIBITED USES**
CloudSoft may use MedDevice's Confidential Information solely for:
- Evaluating the technical requirements for the proposed software platform
- Preparing proposals and technical specifications
- Conducting feasibility analysis for the engagement

CloudSoft shall not use Confidential Information for any other purpose or disclose it to third parties without MedDevice's prior written consent.

**4. OBLIGATIONS OF RECEIVING PARTY**
CloudSoft agrees to:
- Maintain strict confidentiality of all MedDevice information
- Implement appropriate safeguards consistent with healthcare data protection standards
- Limit access to employees directly involved in the evaluation process
- Ensure all personnel sign individual confidentiality agreements
- Comply with applicable healthcare privacy regulations including HIPAA where relevant

**5. EXCEPTIONS TO CONFIDENTIALITY**
Standard exceptions apply for information that is:
- Publicly available without breach of this Agreement
- Previously known to CloudSoft without confidentiality restrictions
- Received from third parties without breach of their confidentiality obligations
- Required to be disclosed by law (with advance written notice to MedDevice)
- Independently developed without access to Confidential Information

**6. RETURN OR DESTRUCTION OF INFORMATION**
Upon completion of the evaluation process or upon request, CloudSoft shall:
- Promptly return all materials containing Confidential Information
- Destroy all copies, notes, and derivative materials
- Provide written certification of such return and destruction

**7. TERM AND TERMINATION**
This Agreement shall remain in effect for one (1) year from execution, with confidentiality obligations continuing for five (5) years post-termination to address the sensitive nature of healthcare-related information.

**8. REMEDIES AND ENFORCEMENT**
Both parties acknowledge that breach would cause irreparable harm to MedDevice, particularly given healthcare regulatory requirements. MedDevice shall be entitled to injunctive relief and monetary damages. This Agreement shall be governed by Delaware law with exclusive jurisdiction in Delaware courts.

**9. GENERAL PROVISIONS**
This Agreement represents the complete understanding between parties regarding confidentiality. Modifications require written consent from both parties. Severability provisions apply if any clause is deemed unenforceable.

IN WITNESS WHEREOF, the parties execute this Agreement.

**MEDDEVICE CORP**                    **CLOUDSOFT SOLUTIONS INC.**

_________________________           _________________________
Name: [Name]                         Name: [Name]
Title: [Title]                       Title: [Title]
Date: [Date]                         Date: [Date]

---

## Evaluation & Scoring

### Parties and Purpose
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2 clearly identifies parties with legal form ("MedDevice Corp, a Delaware corporation... CloudSoft Solutions Inc., a Texas corporation") and states vendor evaluation purpose. Draft 1: "between MedDevice Corp and CloudSoft Solutions for software evaluation" (no legal form, minimal purpose).

### Confidential Information Definition
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2 provides comprehensive definition specific to healthcare context ("system architecture specifications, patient data schemas, clinical workflow requirements, regulatory compliance documentation..."). Draft 1: "All information shared by MedDevice Corp including technical specifications, patient data requirements, and system details" (vague).

### Exclusions
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2 includes standard exceptions ("publicly available... previously known... received from third parties... required to be disclosed by law..."). Draft 1: no exclusions clause.

### Obligations (Use and Care)
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2 details healthcare-specific obligations ("implement appropriate safeguards consistent with healthcare data protection standards... comply with applicable healthcare privacy regulations including HIPAA"). Draft 1: "use the information only for preparing their software proposal" (basic, no care standard).

### Permitted Disclosures
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: "limit access to employees directly involved... ensure all personnel sign individual confidentiality agreements". Draft 1: "will not share it with competitors or other parties" (no detail on permitted internal disclosure).

### Term and Survival
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: "remain in effect for one (1) year... confidentiality obligations continuing for five (5) years post-termination" (appropriate for healthcare data). Draft 1: "lasts for 180 days from signing" (no survival provision).

### Return/Destruction
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: "promptly return all materials... destroy all copies, notes, and derivative materials... provide written certification". Draft 1: no return/destruction provision.

### Remedies
- Score: 2 (Draft 2), 1 (Draft 1)
- Notes: Draft 2: "breach would cause irreparable harm... entitled to injunctive relief and monetary damages" with healthcare context noted. Draft 1: "MedDevice Corp can take legal action" (vague, no injunctive relief).

### Governing Law and Venue
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: "governed by Delaware law with exclusive jurisdiction in Delaware courts". Draft 1: no governing law or venue clause.

### No License / No Partnership / Assignment
- Score: 1 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: "complete understanding between parties... modifications require written consent" (partial). Draft 1: no such language.

### Clarity and Consistency
- Score: 2 (Draft 2), 0 (Draft 1)
- Notes: Draft 2: clear numbered sections, healthcare-specific terminology, consistent structure. Draft 1: informal bullet format, lacks professional structure.

---

## Risk Flags
- ⚠️ High Risk: Exclusions (Draft 1 = 0)
- ⚠️ High Risk: Return/Destruction (Draft 1 = 0)
- ⚠️ High Risk: Governing Law and Venue (Draft 1 = 0)
- ⚠️ High Risk: HIPAA Compliance Gap (Draft 1 has no healthcare regulatory awareness)

---

## Version Comparison Summary
- Draft 2 demonstrates healthcare industry awareness with HIPAA compliance language and extended survival periods appropriate for sensitive medical data.
- Draft 1 is inadequate for healthcare vendor relationships, lacking regulatory compliance considerations and essential legal protections.
- Risk flags in Draft 1 could expose both parties to regulatory violations and unprotected sensitive information disclosure.

---

## Reproducibility Checklist
- [x] Scenario input documented
- [x] Prompt version and text referenced
- [x] AI outputs included
- [x] Rubric applied with quoted evidence
- [x] Risk flags present if needed