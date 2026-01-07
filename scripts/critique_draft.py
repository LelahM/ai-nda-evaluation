#!/usr/bin/env python3
"""
Critique NDA Draft Script

This script applies the evaluation rubric to assess NDA draft quality
systematically. It demonstrates automated scoring and analysis of 
AI-generated legal documents for research and educational purposes.

Usage: python critique_draft.py --file <path_to_draft> [--format json]

Requirements:
- Python 3.7+
- Standard library only (no additional packages required)

Disclaimer: This automated evaluation is for research purposes only.
Professional legal review is required for all legal documents regardless 
of automated scoring results.
"""

import json
import argparse
import re
from pathlib import Path
from typing import Dict, List, Tuple, Any
from dataclasses import dataclass

@dataclass
class EvaluationCriterion:
    name: str
    weight: float
    description: str
    components: List[str]

@dataclass
class EvaluationResult:
    criterion: str
    score: int
    max_score: int
    notes: List[str]
    missing_components: List[str]

class NDAEvaluator:
    """Automated NDA draft evaluator using the project rubric."""
    
    def __init__(self):
        self.rubric = self._load_rubric()
        self.scoring_scale = {
            0: "Inadequate or missing",
            1: "Present but incomplete or unclear", 
            2: "Comprehensive and well-structured"
        }
    
    def _load_rubric(self) -> Dict[str, EvaluationCriterion]:
        """Load evaluation rubric from JSON file."""
        rubric_file = Path(__file__).parent.parent / "rubric" / "rubric.json"
        
        try:
            with open(rubric_file, 'r') as f:
                data = json.load(f)
            
            rubric = {}
            for key, criterion in data['rubric']['criteria'].items():
                rubric[key] = EvaluationCriterion(
                    name=criterion['name'],
                    weight=criterion['weight'],
                    description=criterion['description'],
                    components=criterion['components']
                )
            return rubric
            
        except FileNotFoundError:
            print(f"Warning: Rubric file not found at {rubric_file}")
            return self._default_rubric()
    
    def _default_rubric(self) -> Dict[str, EvaluationCriterion]:
        """Fallback rubric if file not found."""
        return {
            "completeness": EvaluationCriterion(
                "Completeness", 0.25, "Essential NDA clauses",
                ["Party identification", "Confidential information definition", 
                 "Use restrictions", "Obligations", "Exceptions", "Return provisions",
                 "Term", "Remedies"]
            ),
            "legal_structure": EvaluationCriterion(
                "Legal Structure", 0.20, "Professional formatting",
                ["Section organization", "Legal terminology", "Numbering", "Formatting"]
            ),
            "clarity_precision": EvaluationCriterion(
                "Clarity and Precision", 0.20, "Understandability",
                ["Plain language", "Defined terms", "Specific timeframes", "Clear obligations"]
            ),
            "risk_mitigation": EvaluationCriterion(
                "Risk Mitigation", 0.20, "Legal risk management",
                ["Confidentiality scope", "Injunctive relief", "Governing law", "Severability"]
            ),
            "business_alignment": EvaluationCriterion(
                "Business Alignment", 0.15, "Scenario appropriateness",
                ["Business relevance", "Industry considerations", "Enforceability", "Balance"]
            )
        }
    
    def evaluate_draft(self, draft_text: str) -> Dict[str, EvaluationResult]:
        """Evaluate NDA draft against rubric criteria."""
        results = {}
        
        for key, criterion in self.rubric.items():
            if key == "completeness":
                result = self._evaluate_completeness(draft_text, criterion)
            elif key == "legal_structure":
                result = self._evaluate_structure(draft_text, criterion)
            elif key == "clarity_precision":
                result = self._evaluate_clarity(draft_text, criterion)
            elif key == "risk_mitigation":
                result = self._evaluate_risk_mitigation(draft_text, criterion)
            elif key == "business_alignment":
                result = self._evaluate_business_alignment(draft_text, criterion)
            else:
                result = self._basic_evaluation(draft_text, criterion)
            
            results[key] = result
        
        return results
    
    def _evaluate_completeness(self, text: str, criterion: EvaluationCriterion) -> EvaluationResult:
        """Evaluate completeness of essential clauses."""
        essential_patterns = {
            "Party identification": r"between.*(?:corporation|LLC|Inc|Ltd)",
            "Confidential information definition": r"[Cc]onfidential [Ii]nformation.*means",
            "Use restrictions": r"(?:shall not|prohibited|restricted).*use",
            "Obligations": r"(?:agrees to|shall|obligations?)",
            "Exceptions": r"(?:exceptions?|does not apply|excluded)",
            "Return provisions": r"(?:return|destroy|destruction)",
            "Term": r"(?:term|duration|effective.*period)",
            "Remedies": r"(?:injunctive|remedy|remedies|damages)"
        }
        
        present = []
        missing = []
        notes = []
        
        for component, pattern in essential_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                present.append(component)
                notes.append(f"✓ Found: {component}")
            else:
                missing.append(component)
                notes.append(f"✗ Missing: {component}")
        
        # Score based on completeness
        completion_rate = len(present) / len(essential_patterns)
        if completion_rate >= 0.8:
            score = 2
        elif completion_rate >= 0.5:
            score = 1
        else:
            score = 0
        
        return EvaluationResult(
            criterion=criterion.name,
            score=score,
            max_score=2,
            notes=notes,
            missing_components=missing
        )
    
    def _evaluate_structure(self, text: str, criterion: EvaluationCriterion) -> EvaluationResult:
        """Evaluate legal document structure."""
        structure_indicators = {
            "Section numbering": r"^\s*\d+\.",
            "Professional headers": r"NON-DISCLOSURE AGREEMENT|AGREEMENT",
            "Signature blocks": r"IN WITNESS WHEREOF",
            "Proper formatting": r"^\s*[A-Z][A-Z\s]+:?\s*$"
        }
        
        present = []
        missing = []
        notes = []
        
        for indicator, pattern in structure_indicators.items():
            if re.search(pattern, text, re.MULTILINE | re.IGNORECASE):
                present.append(indicator)
                notes.append(f"✓ Found: {indicator}")
            else:
                missing.append(indicator)
                notes.append(f"✗ Missing: {indicator}")
        
        score = 2 if len(present) >= 3 else (1 if len(present) >= 2 else 0)
        
        return EvaluationResult(
            criterion=criterion.name,
            score=score,
            max_score=2,
            notes=notes,
            missing_components=missing
        )
    
    def _evaluate_clarity(self, text: str, criterion: EvaluationCriterion) -> EvaluationResult:
        """Evaluate clarity and precision."""
        clarity_indicators = {
            "Specific timeframes": r"\d+\s*(?:days?|months?|years?)",
            "Defined terms": r'"[^"]+"\s+means',
            "Clear obligations": r"(?:shall|must|agrees? to)",
            "Specific procedures": r"(?:upon|within|prior to|after)"
        }
        
        present = []
        missing = []
        notes = []
        
        for indicator, pattern in clarity_indicators.items():
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                present.append(indicator)
                notes.append(f"✓ Found {len(matches)} instances of: {indicator}")
            else:
                missing.append(indicator)
                notes.append(f"✗ Missing: {indicator}")
        
        score = 2 if len(present) >= 3 else (1 if len(present) >= 2 else 0)
        
        return EvaluationResult(
            criterion=criterion.name,
            score=score,
            max_score=2,
            notes=notes,
            missing_components=missing
        )
    
    def _evaluate_risk_mitigation(self, text: str, criterion: EvaluationCriterion) -> EvaluationResult:
        """Evaluate risk mitigation provisions."""
        risk_indicators = {
            "Injunctive relief": r"injunctive|irreparable harm|equitable relief",
            "Governing law": r"governed by.*law|jurisdiction",
            "Severability": r"severab|unenforceable.*remain",
            "Scope definition": r"broad|reasonable|includes.*but not limited"
        }
        
        present = []
        missing = []
        notes = []
        
        for indicator, pattern in risk_indicators.items():
            if re.search(pattern, text, re.IGNORECASE):
                present.append(indicator)
                notes.append(f"✓ Found: {indicator}")
            else:
                missing.append(indicator)
                notes.append(f"✗ Missing: {indicator}")
        
        score = 2 if len(present) >= 3 else (1 if len(present) >= 2 else 0)
        
        return EvaluationResult(
            criterion=criterion.name,
            score=score,
            max_score=2,
            notes=notes,
            missing_components=missing
        )
    
    def _evaluate_business_alignment(self, text: str, criterion: EvaluationCriterion) -> EvaluationResult:
        """Evaluate business context alignment."""
        # This is more subjective and would typically require human review
        business_indicators = {
            "Purpose statement": r"purpose|exploring|evaluating",
            "Business context": r"consulting|vendor|partnership|joint venture",
            "Appropriate scope": r"limited to|solely for|purpose of",
            "Practical terms": r"reasonable|practical|business"
        }
        
        present = []
        missing = []
        notes = []
        
        for indicator, pattern in business_indicators.items():
            if re.search(pattern, text, re.IGNORECASE):
                present.append(indicator)
                notes.append(f"✓ Found: {indicator}")
            else:
                missing.append(indicator)
                notes.append(f"✗ Missing: {indicator}")
        
        score = 2 if len(present) >= 3 else (1 if len(present) >= 1 else 0)
        
        return EvaluationResult(
            criterion=criterion.name,
            score=score,
            max_score=2,
            notes=notes,
            missing_components=missing
        )
    
    def _basic_evaluation(self, text: str, criterion: EvaluationCriterion) -> EvaluationResult:
        """Basic evaluation for unknown criteria."""
        return EvaluationResult(
            criterion=criterion.name,
            score=1,
            max_score=2,
            notes=["Basic evaluation applied"],
            missing_components=[]
        )
    
    def calculate_overall_score(self, results: Dict[str, EvaluationResult]) -> Dict[str, Any]:
        """Calculate weighted overall score."""
        total_score = 0
        max_possible = 0
        
        for key, result in results.items():
            weight = self.rubric[key].weight
            weighted_score = result.score * weight
            weighted_max = result.max_score * weight
            
            total_score += weighted_score
            max_possible += weighted_max
        
        percentage = (total_score / max_possible) * 100 if max_possible > 0 else 0
        
        return {
            "total_score": round(total_score, 2),
            "max_possible": round(max_possible, 2),
            "percentage": round(percentage, 1),
            "grade": self._assign_grade(percentage)
        }
    
    def _assign_grade(self, percentage: float) -> str:
        """Assign letter grade based on percentage."""
        if percentage >= 90:
            return "A (Professional Grade)"
        elif percentage >= 80:
            return "B (Good with Minor Issues)"
        elif percentage >= 70:
            return "C (Adequate but Needs Improvement)"
        elif percentage >= 60:
            return "D (Significant Issues)"
        else:
            return "F (Inadequate for Professional Use)"

def load_draft(file_path: str) -> str:
    """Load draft text from file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        exit(1)
    except Exception as e:
        print(f"Error loading file: {e}")
        exit(1)

def format_results(results: Dict[str, EvaluationResult], overall: Dict[str, Any], 
                  output_format: str = "text") -> str:
    """Format evaluation results for output."""
    
    if output_format == "json":
        output_data = {
            "overall_score": overall,
            "detailed_results": {}
        }
        
        for key, result in results.items():
            output_data["detailed_results"][key] = {
                "criterion": result.criterion,
                "score": f"{result.score}/{result.max_score}",
                "notes": result.notes,
                "missing_components": result.missing_components
            }
        
        return json.dumps(output_data, indent=2)
    
    else:  # text format
        output = []
        output.append("=" * 60)
        output.append("NDA DRAFT EVALUATION RESULTS")
        output.append("=" * 60)
        output.append("")
        
        # Overall score
        output.append(f"OVERALL SCORE: {overall['total_score']:.1f}/{overall['max_possible']:.1f} ({overall['percentage']:.1f}%)")
        output.append(f"GRADE: {overall['grade']}")
        output.append("")
        
        # Detailed results
        output.append("DETAILED EVALUATION:")
        output.append("-" * 40)
        
        for key, result in results.items():
            output.append(f"\n{result.criterion.upper()}: {result.score}/{result.max_score}")
            for note in result.notes:
                output.append(f"  {note}")
            
            if result.missing_components:
                output.append("  CRITICAL MISSING COMPONENTS:")
                for missing in result.missing_components:
                    output.append(f"    - {missing}")
        
        output.append("")
        output.append("=" * 60)
        output.append("DISCLAIMER:")
        output.append("This automated evaluation is for research purposes only.")
        output.append("Professional legal review is required for all legal documents.")
        output.append("=" * 60)
        
        return "\n".join(output)

def main():
    parser = argparse.ArgumentParser(description="Evaluate NDA draft quality using project rubric")
    parser.add_argument("--file", required=True, help="Path to NDA draft file")
    parser.add_argument("--format", choices=["text", "json"], default="text",
                       help="Output format (default: text)")
    parser.add_argument("--output", help="Output file path (optional)")
    
    args = parser.parse_args()
    
    # Load draft
    draft_text = load_draft(args.file)
    
    # Evaluate
    evaluator = NDAEvaluator()
    results = evaluator.evaluate_draft(draft_text)
    overall = evaluator.calculate_overall_score(results)
    
    # Format output
    formatted_output = format_results(results, overall, args.format)
    
    # Output results
    if args.output:
        with open(args.output, 'w') as f:
            f.write(formatted_output)
        print(f"Results saved to: {args.output}")
    else:
        print(formatted_output)

if __name__ == "__main__":
    main()
