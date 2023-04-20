# Pizza prices
large_price = 6.00
extra_large_price = 10.00
topping_price = {
    1: 1.00,
    2: 1.75,
    3: 2.50,
    4: 3.35
}

# HST tax rate
tax_rate = 0.13

# Get pizza size from user
pizza_size = input("Enter pizza size (L for large, XL for extra large): ")
if pizza_size.upper() == "L":
    pizza_cost = large_price
elif pizza_size.upper() == "XL":
    pizza_cost = extra_large_price
else:
    print("Invalid size entered.")
    exit()

# Get number of toppings from user
num_toppings = int(input("Enter number of toppings (1-4): "))
if num_toppings < 1 or num_toppings > 4:
    print("Invalid number of toppings entered.")
    exit()

# Calculate cost of toppings
topping_cost = topping_price[num_toppings]

# Calculate subtotal
subtotal = pizza_cost + topping_cost

# Calculate tax
tax = subtotal * tax_rate

# Calculate final cost
total_cost = subtotal + tax

# Display costs
print("Subtotal: ${:.2f}".format(subtotal))
print("Tax: ${:.2f}".format(tax))
print("Total: ${:.2f}".format(total_cost))
