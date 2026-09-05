password = input()

s = input()
c = 0

while True:
    if s == password:
        print("вошли в почту")
        break
    else:
        c += 1
        if c % 3 == 0:
            print("три раза уже неправильно, соберись!")
        else:
            print("неправильный пароль")
        s = input()
