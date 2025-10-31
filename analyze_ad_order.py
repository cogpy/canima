#!/usr/bin/env python3
"""
Analyze AD paragraph order compliance in answering affidavits
"""

import re
from pathlib import Path

# Load the reference AD order
def load_ad_order():
    """Load the reference AD paragraph order from the text file"""
    ad_order_file = Path("/home/ubuntu/canima/AD_Paragraph_Order_Reference.txt")
    ad_order = []
    
    with open(ad_order_file, 'r') as f:
        for line in f:
            # Extract AD paragraph numbers (e.g., "AD 1", "AD 1.3", etc.)
            match = re.search(r'AD\s+([\d.]+)', line)
            if match:
                ad_order.append(f"AD {match.group(1)}")
    
    return ad_order

# Extract AD paragraphs from affidavit
def extract_ad_paragraphs(affidavit_file):
    """Extract AD paragraph references from an affidavit file"""
    ad_refs = []
    
    with open(affidavit_file, 'r') as f:
        content = f.read()
        
        # Find all AD paragraph references in headers
        # Pattern: ### AD PARAGRAPH(S) ... or ### AD PARAGRAPHS ...
        pattern = r'###\s+AD\s+PARAGRAPH[S]?\s+([\d.,\s&]+):'
        matches = re.finditer(pattern, content, re.IGNORECASE)
        
        for match in matches:
            # Extract the paragraph numbers
            para_text = match.group(1)
            # Split by commas, ampersands, or "and"
            paras = re.split(r'[,&]|\s+and\s+', para_text)
            for para in paras:
                para = para.strip()
                if para:
                    ad_refs.append(f"AD {para}")
    
    return ad_refs

# Check order compliance
def check_order_compliance(reference_order, affidavit_order, affidavit_name):
    """Check if affidavit follows the reference order"""
    print(f"\n{'='*80}")
    print(f"ANALYZING: {affidavit_name}")
    print(f"{'='*80}\n")
    
    # Create a mapping of AD paragraphs to their position in reference order
    ref_positions = {ad: idx for idx, ad in enumerate(reference_order)}
    
    # Track issues
    issues = []
    missing = []
    out_of_order = []
    
    # Check each AD in affidavit
    prev_position = -1
    for idx, ad in enumerate(affidavit_order):
        if ad not in ref_positions:
            issues.append(f"  ⚠️  {ad} - NOT FOUND in reference order")
        else:
            current_position = ref_positions[ad]
            if current_position < prev_position:
                out_of_order.append(f"  ❌ {ad} (position {current_position}) comes AFTER AD {affidavit_order[idx-1]} (position {prev_position})")
            prev_position = current_position
    
    # Check for missing AD paragraphs
    affidavit_set = set(affidavit_order)
    for ad in reference_order:
        if ad not in affidavit_set:
            missing.append(f"  ⚠️  {ad} - NOT ADDRESSED in affidavit")
    
    # Print results
    print(f"Total AD paragraphs in reference: {len(reference_order)}")
    print(f"Total AD paragraphs addressed in affidavit: {len(affidavit_order)}")
    print(f"Missing AD paragraphs: {len(missing)}")
    print(f"Out of order AD paragraphs: {len(out_of_order)}")
    print(f"Other issues: {len(issues)}")
    
    if out_of_order:
        print(f"\n{'─'*80}")
        print("OUT OF ORDER PARAGRAPHS:")
        print(f"{'─'*80}")
        for issue in out_of_order:
            print(issue)
    
    if missing:
        print(f"\n{'─'*80}")
        print("MISSING PARAGRAPHS:")
        print(f"{'─'*80}")
        for miss in missing[:20]:  # Show first 20
            print(miss)
        if len(missing) > 20:
            print(f"  ... and {len(missing) - 20} more")
    
    if issues:
        print(f"\n{'─'*80}")
        print("OTHER ISSUES:")
        print(f"{'─'*80}")
        for issue in issues:
            print(issue)
    
    if not out_of_order and not issues:
        print(f"\n✅ COMPLIANT: All addressed AD paragraphs follow the correct order")
    
    return {
        'total_reference': len(reference_order),
        'total_addressed': len(affidavit_order),
        'missing': len(missing),
        'out_of_order': len(out_of_order),
        'issues': len(issues)
    }

def main():
    # Load reference order
    reference_order = load_ad_order()
    print(f"Loaded reference AD order: {len(reference_order)} paragraphs")
    
    # Analyze Daniel's affidavit
    daniel_file = Path("/home/ubuntu/canima/affidavits_refined/Daniel_Answering_Affidavit_Refined.md")
    daniel_order = extract_ad_paragraphs(daniel_file)
    daniel_results = check_order_compliance(reference_order, daniel_order, "Daniel's Answering Affidavit (Refined)")
    
    # Analyze Jacqueline's affidavit
    jax_file = Path("/home/ubuntu/canima/affidavits_refined/Jacqueline_Answering_Affidavit_Refined.md")
    jax_order = extract_ad_paragraphs(jax_file)
    jax_results = check_order_compliance(reference_order, jax_order, "Jacqueline's Answering Affidavit (Refined)")
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}\n")
    print(f"Daniel's Affidavit:")
    print(f"  - Addressed: {daniel_results['total_addressed']}/{daniel_results['total_reference']}")
    print(f"  - Missing: {daniel_results['missing']}")
    print(f"  - Out of order: {daniel_results['out_of_order']}")
    print(f"  - Issues: {daniel_results['issues']}")
    
    print(f"\nJacqueline's Affidavit:")
    print(f"  - Addressed: {jax_results['total_addressed']}/{jax_results['total_reference']}")
    print(f"  - Missing: {jax_results['missing']}")
    print(f"  - Out of order: {jax_results['out_of_order']}")
    print(f"  - Issues: {jax_results['issues']}")

if __name__ == "__main__":
    main()
