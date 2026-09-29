# Question 1: Greet the User
# THis program asks the user for their name
# and prints a greeting.

# Create a fuction that takes the user's name.
def greet_user(name): 
  print("Hello,", name + "! Welcome aboard.")

# Ask the user to enter their name.
name = input("Enter your name: ")

# Call the fuction using the name the user entered.
greet_user(name) 
