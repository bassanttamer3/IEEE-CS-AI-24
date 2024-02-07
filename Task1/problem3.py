def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        res = 1
        for i in range(1, x + 1):
            res *= i
        return res

x = int(input('Enter a positive number: '))
print("The factorial of", x, "is", factorial(x))
