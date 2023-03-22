import math

print("Welcome to the Calculator App\n")


num1 = float(input("Enter the first number: "))


num2 = float(input("Enter the second number: "))


print("\nArithmetic Operations")
print("+ Addition: ", num1 + num2)
print("- Subtraction: ", num1 - num2)
print("* Multiplication: ", num1 * num2)
print("/ Division: ", num1 / num2)


print("\nSquare Root and Exponential Operations")
print("√ Square Root of ", num1, "is", math.sqrt(num1))
print(num1, "raised to the power of", num2, "is", num1 ** num2)
