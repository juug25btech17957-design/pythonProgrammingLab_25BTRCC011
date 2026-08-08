print(" Welcome to Smart Shopping!")
print("-" * 30)

customer_name = input("Customer Name: ")
items = []
total_amount = 0
for i in range(1, 4):
    name = input(f"\nItem {i} Name: ")
    price = float(input(f"Item {i} Price (Rs.): "))
    items.append((name, price))
    total_amount += price
if total_amount > 3000:
    discount = total_amount * 0.10
else:
    discount = 0.0

final_payable = total_amount - discount
print("\n" + "=" * 35)
print(f"       RECEIPT - {customer_name.upper()}")
print("=" * 35)

for name, price in items:
    print(f"{name:<20} Rs. {price:>8.2f}")

print("-" * 35)
print(f"{'Total Amount:':<20} Rs. {total_amount:>8.2f}")
print(f"{'Discount (10%):':<20}-Rs. {discount:>8.2f}")
print("-" * 35)
print(f"{'Final Payable:':<20} Rs. {final_payable:>8.2f}")
print("=" * 35)
print("  Thank you for shopping with us!")
print("=" * 35)