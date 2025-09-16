# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")

# TODO: Ask the user for their name using input()
name = input("What is your name? ")

# TODO: Ask how many smoothies they want to buy
smoothies = input("How many smoothies would you like to buy? ")

# TODO: Convert the number of smoothies to an integer
smoothies_int = int(smoothies)

# Ask if the customer wants a reusable cup
cup_choice = input("Would you like a reusable cup for £1.00 extra? (yes/no): ")

# TODO: Calculate the total cost (each smoothie costs £3.50)
cost_per_smoothie = 3.50
if cup_choice.lower() == 'yes':
    cup_cost = 1.00 
else:
    0.00

total_cost = smoothies_int * cost_per_smoothie + cup_cost

# TODO: Display a message using a formatted string
print(f"Thank you, {name}! Your total for {smoothies_int} smoothies is £{total_cost:.2f}.")


# OPTIONAL CHALLENGE:
# Ask if the customer wants a reusable cup for £1.00 extra
# Add the cost if they say yes
