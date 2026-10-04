def buy():
    def check_balance():
        return balance >= price
    if check_balance():
        print("Покупка совершена")
    else:
        print("Недостаточно средств")


# Код ниже не меняйте, проанализируйте, и используйте для создания функций:
balance = int(input())  # баланс покупателя
price = int(input())    # цена за товар
buy()                   # процесс покупки
