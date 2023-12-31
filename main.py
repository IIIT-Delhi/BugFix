# Bug Fix Practice - Solution Branch

# Fixed add_numbers function
def add_numbers(a, b):
    result = a + b  # Fixed: addition instead of multiplication
    return result

# Fixed multiply_numbers function
def multiply_numbers(a, b):
    result = a * b  # Fixed: multiplication instead of addition
    return result

# Fixed fibonacci_sequence function
def fibonacci_sequence(n):
    sequence = [0, 1]
    if n <= 1: # Fixed: return the first 2 elements
        return sequence[:n + 1] # Fixed: return the first n + 1 elements

    for i in range(2, n + 1): # Fixed: Adjust the loop range to include n
        sequence.append(sequence[i - 1] + sequence[i - 2]) # Fixed: add the previous 2 elements

    return sequence

# Fixed factorial_recursive function
def factorial_recursive(n):
    if n == 0:
        return 1  # Fixed: should be 1 for factorial
    else:
        return n * factorial_recursive(n - 1)

# Fixed is_prime function
def is_prime(num):
    if num < 2:
        return False  # Fixed: should be False for non-prime numbers
    for i in range(2, num):
        if num % i == 0:
            return False
    return True  # Fixed: should be True for prime numbers

# Fixed calculate_average function
def calculate_average(x, y, z):
    total = add_numbers(x, y)  # Fixed: remove extra argument for add_numbers()
    total = add_numbers(total, z)  # Fixed: remove extra argument for add_numbers()
    average = total / 3
    return average

# Fixed print_primes function
def print_primes(n):
    count = 0
    i = 2 # Fixed: start at 2 for prime numbers
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