student = []

student.append(5)
student.extend([2, 3, 4])
student.insert(student.index(2), 1)
student.remove(2)
student.remove(3)
student.remove(4)

print(student)
