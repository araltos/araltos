cart = []

while True:
    print("\nWelcome to the Shopping Cart Program!")
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")

    action = input("Please enter an action: ")

    if action == '1':
        item_name = input("What item would you like to add? ").capitalize()
        item_price = float(input(f"What is the price of '{item_name}'? "))
        discount_applied = False

        # Check if the item is 'Milk' or 'Cheese' for discount
        if item_name.capitalize() in ['Milk', 'Cheese']:
            discount_applied = True
            print("You've received a 10% discount for '{}'!".format(item_name))

        cart.append((item_name, item_price, discount_applied))
        print(f"'{item_name}' has been added to the cart.")

    elif action == '2':
        print("The contents of the shopping cart are:")
        for i, (item, price, _) in enumerate(cart, start=1):
            print(f"{i}. {item} - ${price:.2f}")

    elif action == '3':
        if not cart:
            print("The cart is empty. Nothing to remove.")
        else:
            item_to_remove = int(input("Which item would you like to remove? ")) - 1
            if 0 <= item_to_remove < len(cart):
                removed_item = cart.pop(item_to_remove)
                print(f"{removed_item[0]} removed.")
            else:
                print("Invalid item number. Please try again.")

    elif action == '4':
        total_price = sum(price for _, price, _ in cart)
        print(f"The total price of the items in the shopping cart is ${total_price:.2f}")

        # Calculate total with 10% discount for 'Cheese' and 'Milk'
        total_with_discount = sum(price * 0.90 if discount_applied else price for _, price, discount_applied in cart)
        print(f"The total price with a 10% discount for 'Cheese' and 'Milk' is ${total_with_discount:.2f}")

    elif action == '5':
        print("Thank you. Goodbye.")
        break

    else:
        print("Invalid action. Please enter a number between 1 and 5.")
