import json
import csv
import os

STOCK_FILE = 'stock_data.json'
LOW_STOCK_THRESHOLD = 5

def load_stock():
    if os.path.exists(STOCK_FILE):
        with open(STOCK_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_stock(stock):
    with open(STOCK_FILE, 'w') as f:
        json.dump(stock, f, indent=4)

def display_stock(stock):
    print("\nCurrent Stock:")
    for item, qty in stock.items():
        warning = " [LOW STOCK!]" if qty < LOW_STOCK_THRESHOLD else ""
        print(f"{item}: {qty}{warning}")
    print()

def add_item(stock):
    item = input("Enter item name: ").strip()
    if item in stock:
        print("Item already exists.")
        return
    qty = int(input("Enter initial quantity: "))
    stock[item] = qty
    print("Item added.")

def stock_in(stock):
    item = input("Enter item name: ").strip()
    if item not in stock:
        print("Item not found.")
        return
    qty = int(input("Enter quantity to add: "))
    stock[item] += qty
    print("Stock updated.")

def stock_out(stock):
    item = input("Enter item name: ").strip()
    if item not in stock:
        print("Item not found.")
        return
    qty = int(input("Enter quantity to remove: "))
    if qty > stock[item]:
        print("Not enough stock.")
        return
    stock[item] -= qty
    print("Stock updated.")

def export_to_csv(stock):
    filename = 'stock_export.csv'
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Item", "Quantity"])
        for item, qty in stock.items():
            writer.writerow([item, qty])
    print(f"Stock exported to {filename}")

def main():
    stock = load_stock()
    while True:
        print("""
--- Warehouse Stock Manager ---
1. Display Stock
2. Add New Item
3. Stock In
4. Stock Out
5. Export to CSV
6. Exit
""")
        choice = input("Select an option: ").strip()
        if choice == '1':
            display_stock(stock)
        elif choice == '2':
            add_item(stock)
        elif choice == '3':
            stock_in(stock)
        elif choice == '4':
            stock_out(stock)
        elif choice == '5':
            export_to_csv(stock)
        elif choice == '6':
            save_stock(stock)
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
