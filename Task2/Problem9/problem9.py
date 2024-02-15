def find_common_elements(set1, set2):
    return set1.intersection(set2)


if __name__ == "__main__":
    set1_input = input("Enter elements of the first set separated by spaces: ")
    set1 = set(map(int, set1_input.split()))

    set2_input = input("Enter elements of the second set separated by spaces: ")
    set2 = set(map(int, set2_input.split()))

    common_elements = find_common_elements(set1, set2)
    print("Common Elements:", common_elements)
