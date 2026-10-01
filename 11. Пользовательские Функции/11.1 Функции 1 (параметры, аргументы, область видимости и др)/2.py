s = input()

def is_float(x):
    if x.isdigit():
        return float(x)
    elif x.count(".") == 1:
        if x.replace(".", "").isdigit():
            return float(x)

print(is_float(s))
