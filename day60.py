if __name__ == '__main__':
    students = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    grades = sorted(set([s[1] for s in students]))
    second_lowest = grades[1]

    names = []

    for s in students:
        if s[1] == second_lowest:
            names.append(s[0])

    names.sort()

    for n in names:
        print(n)