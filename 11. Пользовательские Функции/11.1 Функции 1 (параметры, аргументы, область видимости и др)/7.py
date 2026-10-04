def buy():
    def check_balance():
        return balance >= price
    
    def change_balance():
        global balance
        balance -= price

    def show_balance():
        print("Ваш баланс:", balance)
    if check_balance():
        print("Покупка совершена")
        change_balance()
        show_balance()
    else:
        print("Недостаточно средств")


# Код ниже не меняйте, проанализируйте, и используйте для создания функций:
balance = int(input())  # баланс покупателя
price = int(input())    # цена за товар
buy()                   # процесс покупки
