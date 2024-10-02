child_meal, adult_meal, num_childre, num_adult, sale_tx, = 4, 5, 3, 5, 6

child_meal = float (input("What is the price of a child's meal? "))
adult_meal = float (input("What is the price of an adult's meal? "))
num_childre = int (input("How many children are there? "))
num_adult = int (input("How many adults are there? "))
sale_tx = float(input("What is the sales tax rate? "))

# meal's subtotal
meal_sub = num_childre * child_meal
meal_sub2 = num_adult * adult_meal
sub_g = meal_sub + meal_sub2
print (f"\nSubtotal: {sub_g:.2f}")

#sales tax
sales_tx = sub_g * sale_tx/100
print (f"Sales Tax: {sales_tx:.2f}")

#discount and total
discount = num_childre
if num_childre >= 2:
    dis_percentage = 10
    dis_amount = (dis_percentage / 100) * child_meal
    dis_price = child_meal - dis_amount
    total = sub_g + sales_tx - dis_price
    print (f"Total: {total:.2f}")
else:
    total = sub_g + sales_tx
    print (f"Total: {total:.2f}")

#payment
payment = float(input("\nWhat is the payment amount? "))
process = payment - total
print(f"Change: {process:.2f}")