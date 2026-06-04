import csv

input_file = "sample_data.csv"
output_file = "flagged_orders.csv"

flagged_orders = []

with open(input_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        reasons = []

        amount_text = row["amount"].strip()

        if amount_text == "":
            reasons.append("Missing amount")
            amount = 0
        else:
            amount = float(amount_text)

        if row["delivery_date"].strip() == "":
            reasons.append("Missing delivery date")

        if amount >= 5000:
            reasons.append("High value order")

        if row["payment_status"] in ["unpaid", "partial"]:
            reasons.append("Payment not completed")

        if row["priority"] == "urgent":
            reasons.append("Urgent priority")

        if reasons:
            row["flag_reason"] = "; ".join(reasons)
            flagged_orders.append(row)

with open(output_file, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "order_id",
        "customer",
        "product",
        "region",
        "order_date",
        "delivery_date",
        "amount",
        "status",
        "payment_status",
        "priority",
        "notes",
        "flag_reason"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(flagged_orders)

print("Order screening completed.")
print("Flagged orders:", len(flagged_orders))
print("Output file:", output_file)
