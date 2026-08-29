s = input()

city_1, city_2 = s.split()

if city_1[-1] == city_2[0].lower():
    print("Слово подходит")
else:
    print("Слово не подходит")
