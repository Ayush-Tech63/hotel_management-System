menu = {
    'Pizza': 150,
    'Pasta': 100,
    'Burger': 80,
    'Nudels': 120,
    'Coffee': 80,
    'Salad': 70,
}

print("Welcome to Banarasi Restaurant:")
print("Pizza: Rs150\nPasta: Rs100\nBurger: Rs80\nNudels: Rs120\nCoffee: Rs80\nSalad: Rs70")

order_total = 0

item = input("Enter the item you want to order = ")

if item in menu:
    order_total += menu[item]
    print(f"Your item {item} has been added.")
else:
    print(f"Sorry, {item} is not available.")

another_item = input("Do you want to add another item (yes/no)? ")

while another_item != "no":

    item = input("Enter the name of another item = ")

    if item in menu:
        order_total += menu[item]
        print(f"Item {item} has been added.")
    else:
        print(f"Sorry, {item} is not available.")

    another_item = input("Do you want to add another item (yes/no)? ")

print(f"Your total bill is Rs.{order_total}")
print("Thank you for visiting Banarasi Restaurant!")