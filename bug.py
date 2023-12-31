# BugFix Python - Main Branch

# Buggy add_numbers function
def add_numbers(a, b):
    result = a * b
    return result

# Buggy multiply_numbers function
def multiply_numbers(a, b):
    result = a + b
    return result

# Buggy fibonacci_sequence function
def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[i + 1] * sequence[i])

    return sequence

# Buggy factorial_recursive function
def factorial_recursive(n):
    if n == 1:
        return 0
    else:
        return n * factorial_recursive(n - 1)

# Buggy is_prime function
def is_prime(num):
    if num < 2:
        return True
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

# Buggy calculate_average function
def calculate_average(x, y, z):
    total = add_numbers(x, y, z)
    average = total / 3
    return average

# Buggy print_primes function
def print_primes(n):
    count = 0
    i = 3
    while count < n:
        if is_prime(i):
            print(i, end=" ")
            count += 1
        i += 1

# Test the functions
num1 = 10
num2 = 5
num3 = 8

result_sum = add_numbers(num1, num2)
result_product = multiply_numbers(num1, num3)
result_average = calculate_average(num1, num2, num3)
fibonacci_result = fibonacci_sequence(10)
factorial_result = factorial_recursive(5)

# Print Results
print(f"Sum: {result_sum}")
print(f"Product: {result_product}")
print(f"Average: {result_average}")
print("Fibonacci Sequence:", fibonacci_result)
print("Factorial:", factorial_result)
print("First 5 Prime Numbers:")
print_primes(5)