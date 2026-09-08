s = input()

words = ["Эээ", "Типа", "Короче", "Ну", "Как бы"]
result = "Слов паразитов не обнаружено"

for word in words:
    if word.lower() in s.lower():
        result = "Слова паразиты обнаружены"
        break

print(result)
