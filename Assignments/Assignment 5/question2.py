# Question2: Rectangle Calculator
# This program calculates the area and the perimeter of a rectangle.

# Createa fuction that takes the length and width.
def rectangle_stats(length, width):
  # Calculate the area.
  area = length * width

  # Calculate the perimeter.
  perimeter = 2 * (length + width)

  # Return both results.
  return area, perimeter

# Ask the user for the length.
length = int(input("Enter the length: "))

# ASk the user for the width.
width = int(input("Enter the width: "))

# Call the fuction the store both results.
area, perimeter = rectangle_stats(length, width)

# Print the results.
print("Area: ", area)
print("Perimeter: ", perimeter)
