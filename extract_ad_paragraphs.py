import re
from collections import OrderedDict

# Read Peter's founding affidavit
with open('/home/ubuntu/canima/affidavits/Peter_Founding_Affidavit.md', 'r') as f:
    content = f.read()

# Extract all paragraph headings (### Paragraph X.X.X...)
pattern = r'^### Paragraph ([\d.]+)$'
matches = re.findall(pattern, content, re.MULTILINE)

# Create ordered list of AD paragraph numbers
ad_paragraphs = OrderedDict()
for match in matches:
    ad_paragraphs[match] = None

# Print results
print("AD Paragraph Numbers from Peter's Founding Affidavit (in order):")
print("=" * 70)
for i, para in enumerate(ad_paragraphs.keys(), 1):
    print(f"{i:3d}. AD {para}")

print(f"\nTotal AD paragraphs: {len(ad_paragraphs)}")
