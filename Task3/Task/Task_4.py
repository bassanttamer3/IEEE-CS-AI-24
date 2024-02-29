import math
def get_numbers():
    while True:
        try:
            number_input = input("Enter the numbers separated by commas: ")
            numbers_as_strings = number_input.split(',')
            numbers_inlist = list(map(int, numbers_as_strings))
            return numbers_inlist
        except ValueError:
            print("Please enter valid integers separated by commas.")
def find_min(numbers_inlist):
    min_number = numbers_inlist[0]
    for number in numbers_inlist:
        if number < min_number:
            min_number = number
    return min_number

def find_max(numbers_inlist):
    max_number = numbers_inlist[0]
    for number in numbers_inlist:
        if number > max_number:
            max_number = number
    return max_number

def find_mean(numbers_inlist):
    sum_number = 0
    count_number = len(numbers_inlist)
    for number in numbers_inlist:
        sum_number += number
    mean =sum_number /count_number
    return mean


def find_mode(numbers_inlist):
    frequency_dict = {}
    for number in numbers_inlist:
        if number in frequency_dict:
            frequency_dict[number] += 1
        else:
            frequency_dict[number] = 1

    max_frequency = max(frequency_dict.values())
    modes = [number for number, frequency in frequency_dict.items() if frequency == max_frequency]

    return modes


def find_median(numbers_inlist):
    numbers_inlist.sort()
    count_number = len(numbers_inlist)
    if count_number % 2 != 0:
        median_index = count_number // 2
        median = numbers_inlist[median_index]
    else:
        median_index1 = count_number // 2 - 1
        median_index2 = count_number // 2
        median = (numbers_inlist[median_index1] + numbers_inlist[median_index2]) / 2
    return median


def find_range(numbers_inlist):
    return find_max(numbers_inlist) - find_min(numbers_inlist)

def find_variance(numbers_inlist):
    mean = find_mean(numbers_inlist)
    count_number = len(numbers_inlist)
    denominator = count_number
    numerator = 0
    for number in numbers_inlist:
        numerator += (number - mean) ** 2
    variance = numerator / denominator
    return variance



def find_STD(numbers_inlist):
    variance =find_variance(numbers_inlist)
    std = math.sqrt(variance)
    return std


def find_Quartiles(numbers_inlist):
    numbers_inlist.sort()
    n = len(numbers_inlist)

    Q1_index = int(n * 0.25)
    Q2_index = int(n * 0.5)
    Q3_index = int(n * 0.75)

    Q1 = numbers_inlist[Q1_index]
    Q2 = numbers_inlist[Q2_index]
    Q3 = numbers_inlist[Q3_index]

    return Q1, Q2, Q3


def find_IQR(numbers_inlist):
    Q1, _, Q3 = find_Quartiles(numbers_inlist)
    return Q3 - Q1

def main():
    while True:
        try:
            numbers = get_numbers()
            print("Minimum:", find_min(numbers))
            print("Maximum:", find_max(numbers))
            print("Mean:", find_mean(numbers))
            print("Mode:", find_mode(numbers))
            print("Median:", find_median(numbers))
            print("Range:", find_range(numbers))
            print("Variance:", find_variance(numbers))
            print("Standard Deviation:", find_STD(numbers))
            print("Quartiles:", find_Quartiles(numbers))
            print("Interquartile Range:", find_IQR(numbers))
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            break
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
