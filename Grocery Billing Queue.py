# ================================
# GROCERY BILLING QUEUE
# ================================

print("=== Grocery Billing Queue ===\n")

# ---------- PART 1: the five counters ----------
low_price_items = 0
medium_price_items = 0
high_price_items = 0
customers_served = 0
total_sales = 0
billing = True


# ---------- PART 2: the OUTER while loop — one customer per repeat ----------
while billing:
    name=input("What is your name? ")
    item_count=int(input("How many items are you buying? "))
    if item_count <=0:
        print("You must buy at least one item!")
        continue
    customer_total = 0
    item_number = 1
    
    
    while item_number <= item_count:
        item_name=input("Enter the name of the item: ")
        price=int(input("Enter the price of the item: "))
        quantity=int(input("Enter the quantity of the item: "))
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than 0. Please re-enter the item.")
            continue
        item_total = price * quantity
        print(f"{item_name}: {quantity} x {price} = {item_total}")
        customer_total += item_total
        if quantity < 50:
            low_price_items += 1
        elif quantity <= 100:
            medium_price_items += 1
        else:
            high_price_items += 1
            
        item_number += 1

    customers_served += 1
    total_sales += customer_total
    print(f"{name}, your total is: {customer_total}")
    next_customer = input("Next customer? (yes/no): ")

    if next_customer.lower()!= "yes":
        billing = False
   
categories = ["Low Price Items", "Medium Price Items", "High Price Items"]
star_counts = [low_price_items, medium_price_items, high_price_items]

print("\n=== Sales Summary ===")

for i in range(3):
    print(categories[i], end=": ")
    for j in range(star_counts[i]):
        print("*", end="")
    print()

total_items = low_price_items + medium_price_items + high_price_items

print(f"Total Items: {total_items}")
print(f"Total Customers Served: {customers_served}")
print(f"Total Sales: {total_sales}")
