# Demand vs Stock Calculation

# Sample data (you can later read from Excel/CSV)
products = [
    {"Product": "A", "Demand": 500, "Stock": 300},
    {"Product": "B", "Demand": 200, "Stock": 250},
    {"Product": "C", "Demand": 800, "Stock": 600},
    {"Product": "D", "Demand": 150, "Stock": 150},
]

# Calculation
for item in products:
    item["Gap"] = item["Stock"] - item["Demand"]
    if item["Gap"] < 0:
        item["Status"] = "Shortage"
    elif item["Gap"] > 0:
        item["Status"] = "Excess"
    else:
        item["Status"] = "Balanced"

# Display results
# Heading
print(f"{'Product':<10}{'Demand':<10}{'Stock':<10}{'Gap':<10}{'Status':<10}")
# Line creation
print("-" * 50)
# Rows to add
for item in products:
    print(f"{item['Product']:<10}{item['Demand']:<10}{item['Stock']:<10}{item['Gap']:<10}{item['Status']:<10}")
