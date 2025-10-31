
import re

with open("Shopify_Invoices_RegimA_2016-2025.txt", "r") as f:
    lines = f.readlines()

invoices = []
i = 0
while i < len(lines):
    if lines[i].strip() == "Select invoice":
        date = lines[i+1].strip()
        bill_number = lines[i+2].strip()
        amount_str = lines[i+6].strip().replace("$", "").replace(",", "")
        try:
            amount = float(amount_str)
            invoices.append((date, bill_number, amount))
            i += 9  # Move to the next potential invoice block
        except (ValueError, IndexError):
            # Handle cases where the structure is not as expected
            i += 1
    else:
        i += 1


with open("Shopify_Invoice_Summary.md", "w") as f:
    f.write("# Shopify Invoice Summary (2016-2025)\n\n")
    f.write("| Date | Bill Number | Amount (USD) |\n")
    f.write("|---|---|---:|\n")
    total_amount = 0
    for date, bill_number, amount in invoices:
        f.write(f"| {date} | {bill_number} | {amount:.2f} |\n")
        total_amount += amount
    f.write("\n")
    f.write(f"**Total Amount Paid:** ${total_amount:,.2f}\n")

print("Shopify invoice summary generated successfully.")
