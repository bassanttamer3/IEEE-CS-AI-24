if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    students.sort(key=lambda x: x[1])

    second_lowest_grade = students[1][1]

    for name, score in sorted(students):
        if score == second_lowest_grade:
            print(name)