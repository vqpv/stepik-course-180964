word = input()

word = word.lower()

lst = list(word)
lst.sort()

result = "".join(lst)

print(result)
