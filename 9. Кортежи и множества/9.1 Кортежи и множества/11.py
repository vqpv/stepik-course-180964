s_1 = set(input().split())
s_2 = set(input().split())

print(*sorted(s_1.symmetric_difference(s_2)))
