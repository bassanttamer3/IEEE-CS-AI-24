##This code has been modified to allow the user to enter numbers
class Solution(object):
    def get_numbers(self):
        while True:
            try:
                number_input = input("Enter the numbers separated by commas: ")
                numbers_as_strings = number_input.split(',')
                numbers_inlist = list(map(int, numbers_as_strings))
                return numbers_inlist
            except ValueError:
                print("Please enter valid integers separated by commas.")

    def find_min(self, numbers_inlist):
        return min(numbers_inlist)

    def find_max(self, numbers_inlist):
        return max(numbers_inlist)

    def find_mean(self, numbers_inlist):
        total_sum = sum(numbers_inlist)
        total_count = len(numbers_inlist)
        return total_sum / float(total_count)

    def find_mode(self, numbers_inlist):
        frequency_dict = {}
        for number in numbers_inlist:
            frequency_dict[number] = frequency_dict.get(number, 0) + 1

        max_frequency = max(frequency_dict.values())
        modes = [number for number, frequency in frequency_dict.items() if frequency == max_frequency]

        return modes[0]

    def find_median(self, numbers_inlist):
        numbers_inlist.sort()
        count_number = len(numbers_inlist)
        if count_number % 2 != 0:
            median_index = count_number // 2
            median = numbers_inlist[median_index]
        else:
            median_index1 = count_number // 2 - 1
            median_index2 = count_number // 2
            median = (numbers_inlist[median_index1] + numbers_inlist[median_index2]) / 2.0
        return median

def main():
    try:
        solution = Solution()
        numbers = solution.get_numbers()
        print("Minimum:", solution.find_min(numbers))
        print("Maximum:", solution.find_max(numbers))
        print("Mean:", solution.find_mean(numbers))
        print("Mode:", solution.find_mode(numbers))
        print("Median:", solution.find_median(numbers))
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()

# This code was run in Leetcode

#################
# class Solution(object):
#     def sampleStats(self, count):
#         def find_min(numbers_inlist):
#             return min(numbers_inlist)
#
#         def find_max(numbers_inlist):
#             return max(numbers_inlist)
#
#         def find_mean(numbers_inlist):
#             total_sum = sum(numbers_inlist)
#             total_count = len(numbers_inlist)
#             return total_sum / float(total_count)
#
#         def find_mode(numbers_inlist):
#             frequency_dict = {}
#             for number in numbers_inlist:
#                 frequency_dict[number] = frequency_dict.get(number, 0) + 1
#
#             max_frequency = max(frequency_dict.values())
#             modes = [number for number, frequency in frequency_dict.items() if frequency == max_frequency]
#
#             return modes[0]
#
#         def find_median(numbers_inlist):
#             numbers_inlist.sort()
#             count_number = len(numbers_inlist)
#             if count_number % 2 != 0:
#                 median_index = count_number // 2
#                 median = numbers_inlist[median_index]
#             else:
#                 median_index1 = count_number // 2 - 1
#                 median_index2 = count_number // 2
#                 median = (numbers_inlist[median_index1] + numbers_inlist[median_index2]) / 2.0
#
#             return median
#
#         if not count:
#             raise ValueError("Input list 'count' cannot be empty.")
#
#         if any(num < 0 for num in count):
#             raise ValueError("Input list 'count' cannot contain negative values.")
#
#         numbers_inlist = []
#         for number, frequency in enumerate(count):
#             numbers_inlist.extend([number] * frequency)
#         return [find_min(numbers_inlist), find_max(numbers_inlist), find_mean(numbers_inlist),
#                 find_median(numbers_inlist), find_mode(numbers_inlist)]
#
