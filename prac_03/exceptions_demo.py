"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when the program gets an input from the user that is the correct type but incorrect value
2. When will a ZeroDivisionError occur?
When the user inputs a denominator of 0 into the program
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
use an if statement to check to see if the value being used as the denominator is a zero or not
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
