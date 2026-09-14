nums = list(sorted(map(int, input().split())))

new_nums = []

for i in range(1, 6):
    lst = []
    for num in nums:
        if num == i:
            lst.append(num)
    new_nums.append(lst)

print(new_nums)
