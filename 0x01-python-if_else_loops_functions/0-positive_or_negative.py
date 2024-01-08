#!/usr/bin/python3
import random

# Generate a random signed number
number = random.randint(-10, 10)

# Print the randomly generated number
print(f"{number} ", end="")

# Check if the number is positive, zero, or negative
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")

