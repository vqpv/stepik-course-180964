nums = list(map(int, input().split()))

new_nums = reversed(sorted(nums))
num = next(new_nums)
count = 0

for i in nums:
    if i == num:
        count += 1

print(f"Самая высокая оценка: {num}")
print(f"Количество: {count} шт")
