a, b = map(int, input().split())

lst = []
c = 1

while c <= a:
    if c % b == 0:
        lst.append(c)
    c += 1

print(lst)
