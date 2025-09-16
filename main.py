# Starter file for the Smoothie Shop Calculator exercise

print("Welcome to the Smoothie Shop!")
 # TODO: Ask the user for their name using input()
name = input("what is your name ")
 
 # TODO: Ask how many smoothies they want to buy
smoothies_str = input("how many smoothies would you want to buy ")
 
 # TODO: Convert the number of smoothies to an integer
smoothies_int = int(smoothies_str)

 # TODO: Calculate the total cost (each smoothie costs £3.50)
cost = 3.50
total_cost = smoothies_int * cost
 # TODO: Display a message using a formatted string
print(f"Thank you, {name } your total is {total_cost } enjoy your smoothies")

# OPTIONAL CHALLENGE:
 # Ask if the customer wants a reusable cup for £1.00 extra

extra = input("would you like a reusable cup for an extra £1.00 ")
if extra == "yes":
 total_cost += 1.00
else:
    print ("no cup added ")
print (f" your total is {total_cost}")
