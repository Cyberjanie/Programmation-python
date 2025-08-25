Items = [
    {"item": "apple", "price": 0.59, "sku": "A123"},
    {"item": "banana", "price": 0.39, "sku": "B456"},
    {"item": "orange", "price": 0.79, "sku": "O789"}
     
]
item = input("search for an item: ")
for entry in Items:
    if entry["item"].lower() == item.lower():
        print(f"Price: {entry['price']}$, SKU: {entry['sku']}")
        break
else:
     print("Item not found.")
        