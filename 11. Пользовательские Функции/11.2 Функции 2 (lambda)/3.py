def sort_two_key(d: dict) -> tuple:
    ''' Функция для сортировки по двум ключам: bad habits и age'''
    return d['bad_habits'], -d['age']

sorted_data = sorted(persons, key=sort_two_key)
for i in sorted_data:
    print(i)
