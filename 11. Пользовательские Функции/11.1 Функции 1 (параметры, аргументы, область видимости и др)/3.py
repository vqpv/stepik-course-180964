l = input()
p = input()

def check_login_password(login, password, true_login="admin", true_password="admin"):
    return login == true_login and  password == true_password

print(check_login_password(l, p))
