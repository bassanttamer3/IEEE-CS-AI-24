n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid value, please enter a positive integer.")
else:
    divisor_sum = 0

    for num in range(1, n):
        if n % num == 0:
            divisor_sum += num
    
    if divisor_sum == n:
        print(f"{n} is a perfect number.")
    else:
        print(f"{n} is not a perfect number.")
