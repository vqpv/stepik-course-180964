def super_minus(**kwargs):
    nums = tuple(kwargs.values())
    result = nums[0]
    for i in nums[1:]:
        result -= i
    return result

# ваша функция будет использована вот так:
num1 = super_minus(n1=10, n2=2, n3=5)  # 10-2-5 = 3
num2 = super_minus(n1=100, n2=20, n3=50, n4=10, n5=10, n6=5)  # 100-20-50-10-10-5 = 5
num3 = super_minus(n1=700, n2=100, n3=300, n4=200)  # 700-100-300-200 = 100

# результат: print(num1 + num2 + num3)  # 108
