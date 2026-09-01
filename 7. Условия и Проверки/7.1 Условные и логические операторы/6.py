s_1 = input()
s_2 = input()

lst_1 = s_1.split()
lst_2 = s_2.split()

if lst_1[2] != lst_2[1] and int(lst_1[0]) <= int(lst_2[0]) < int(lst_1[1]):
    print("Открыто")
else:
    print("Закрыто")
