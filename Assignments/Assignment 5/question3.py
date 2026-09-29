# Question 3: Simple Number Checker
# This program checks if a whole number is even or odd.

# Create function that takes a number.
def check_number(number):
  # Divide the number by 2.
  half = number / 2

# Multiply the result by 2.
check = half * 2

# Check if the result is the same as the original number.
if check == number:
  return "even"
else:
  return "odd"

# Ask the user to enter a whole number.
number = int(input("Enter a whole number: "))

# Call the fuction and store the returned result.
result = check_number(number)

# Print the result using an f-string
print(number, "is an", result, "number.")
