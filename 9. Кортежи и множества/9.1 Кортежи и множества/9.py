s_1 = set(input().split())
s_2 = set(input().split())
s_3 = set(input().split())

print(f"Склад 1: {sorted(s_3.difference(s_1))}")
print(f"Склад 2: {sorted(s_3.difference(s_2))}")
