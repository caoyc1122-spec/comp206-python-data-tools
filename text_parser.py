input_file = "sample_text.txt"

records = []
current_record = {}

with open(input_file, "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line == "":
            if current_record:
                records.append(current_record)
                current_record = {}
        elif line.startswith("Customer:"):
            current_record["customer"] = line.replace("Customer:", "").strip()
        elif line.startswith("Contact Name:"):
            current_record["contact_name"] = line.replace("Contact Name:", "").strip()
        elif line.startswith("Email:"):
            current_record["email"] = line.replace("Email:", "").strip()
        elif line.startswith("Phone:"):
            current_record["phone"] = line.replace("Phone:", "").strip()
        elif line.startswith("Product Interest:"):
            current_record["product_interest"] = line.replace("Product Interest:", "").strip()
        elif line.startswith("Priority:"):
            current_record["priority"] = line.replace("Priority:", "").strip()

if current_record:
    records.append(current_record)

print("Text parsing completed.")
print("Total records:", len(records))

for record in records:
    print(record)
