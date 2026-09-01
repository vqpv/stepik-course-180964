login = input()
password = input()

if login == "admin":
    if password == "read":
        print("Редактор в режиме чтения")
    elif password == "edit":
        print("Редактор в режиме редактирования")
    else:
        print("Неправильный пароль")
else:
    print(f"Пользователь {login}")
