# Enter -1 to terminate
largest = None
smallest = None

while True:
    num = input("Enter a number: ")

    if num == '-1':
        break

    num = int(num)

    if largest is None or num > largest:
        largest = num
    if smallest is None or num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)
