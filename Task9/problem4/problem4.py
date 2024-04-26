# Ask the user for a number n. Then, use broadcasting
# to create a n x n ndarray that has its first column full of ones,
# its second column full of twos, its third column full of threes, etc…
import numpy as np
while True:
    try:
        n = int(input("Enter a positive integer value for n: "))
        if n <= 0:
            raise ValueError("n must be a positive integer")
        break  # Exit loop if input is valid
    except ValueError:
        print("Invalid input. Please enter a valid positive integer.")

try:
    array = np.zeros((n, n))
    for i in range(n):
        array[:, i] = i + 1

    print("n x n array with each column containing consecutive integers:")
    print(array)

except Exception as e:
    print("An error occurred:", e)


