def get_numeric(num):
    while True:
        userinput = input(num)
        if userinput.strip().replace('.', '', 1).isdigit():
            return float(userinput)
        else:
            print("Please enter a valid numeric value.")


if __name__ == "__main__":
    numeric_value = get_numeric("Please enter a numeric value: ")
    print("You entered:", numeric_value)
