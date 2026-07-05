

#Task 4

# Create catalog list of tuples
catalog = [
    ("Laptop", 65000, "Electronics"),
    ("Mouse", 850, "Accessories"),
    ("Keyboard", 1500, "Accessories"),
    ("Monitor", 12000, "Electronics"),
    ("Speaker", 3000, "Audio"),
    ("Webcam", 2500, "Camera")
]

category_to_products = {}

for product, price, category in catalog:

    if category not in category_to_products:
        category_to_products[category] = []

    category_to_products[category].append(product)

print("\nCategory to Products:")
print(category_to_products)

max_category = ""

for category in category_to_products:
    if max_category == "":
        max_category = category
    elif len(category_to_products[category]) > len(category_to_products[max_category]):
        max_category = category

print(max_category)

print("Products:")
print(category_to_products[max_category])