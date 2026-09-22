s_1 = set(input().split())
s_2 = set(input().split())
s_3 = set(input().split())
s_4 = set(input().split())

a = s_1.intersection(s_4)
b = s_2.intersection(s_3)

print(len(a) + len(b))
