right_answer = tuple(input().split())
person_answer = tuple(input().split())

result = 0

for i in right_answer:
    if i in person_answer:
        result += 1

print(result)
