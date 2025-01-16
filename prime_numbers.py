import os

""" 
Python script to find prime numbers between 1 and 250,
save the results to a file, add debugging output, and print the absolute path of the results.
"""

def is_prime(num):
    """Check if a number is a prime number."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is divisible by {i}. Not prime.")
            return False
    print(f"{num} is prime.")
    return True

# List to store prime numbers
prime_numbers = []

# Loop through numbers from 1 to 250
for num in range(1, 251):
    if is_prime(num):
        prime_numbers.append(num)

# Save the prime numbers to a file
with open("results.txt", "w") as file:
    for prime in prime_numbers:
        file.write(f"{prime}\n")

print("Prime numbers between 1 and 250 have been saved to results.txt.")
file_path = os.path.abspath("results.txt")
print(f"The file is saved at: {file_path}")