# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Get user input
number = int(input("Enter a number: "))

# Calculate factorial
result = factorial(number)

# Display the result
print(f"The factorial of {number} is {result}")
