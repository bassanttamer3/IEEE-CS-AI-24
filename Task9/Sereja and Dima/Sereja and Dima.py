import numpy as np
Sereja_score = 0
Dima_score = 0
def create_array(n, numbers):
    array = np.array(numbers)
    return array
def who_win(array):
    global Sereja_score
    global Dima_score
    for i in range(n):
        if i % 2 == 0:
            max_value = np.max(array)
            max_value_index = np.where(array == max_value)[0][0]
            Sereja_score += max_value
            array = np.delete(array, max_value_index)
        elif i % 2 == 1:
            max_value = np.max(array)
            max_value_index = np.where(array == max_value)[0][0]
            Dima_score += max_value
            array = np.delete(array, max_value_index)

n = int(input())
numbers_input = input().split()
numbers = [int(num) for num in numbers_input]
result_array = create_array(n, numbers)
who_win(result_array)
print(Sereja_score, Dima_score)


######----------------------------------------------------------------###
##code in codeforces
##------------------------###
def who_win(n, array):
    Sereja_score = 0
    Dima_score = 0
    left = 0
    right = n - 1
 
    for i in range(n):
        if i % 2 == 0:
            if array[left] > array[right]:
                Sereja_score += array[left]
                left += 1
            else:
                Sereja_score += array[right]
                right -= 1
        else:
            if array[left] > array[right]:
                Dima_score += array[left]
                left += 1
            else:
                Dima_score += array[right]
                right -= 1
 
    return Sereja_score, Dima_score
 
n = int(input())
numbers_input = input().split()
numbers = [int(num) for num in numbers_input]
Sereja_score, Dima_score = who_win(n, numbers)
print(Sereja_score, Dima_score)
