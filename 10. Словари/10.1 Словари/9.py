names = list(students.keys())

for i in range(len(names)):
    m, p, c = map(int, input().split())
    name = names[i]
    students[name]["математика"].append(m)
    students[name]["физика"].append(p)
    students[name]["химия"].append(c)

print(students)
