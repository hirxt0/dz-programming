accounts = {}  

def create_account(name: str):
    if name in accounts:
        print("такой счёт уже существует")
    else:
        accounts[name] = 0
        print(f"счёт '{name}' создан")


def deposit(name: str, amount: float):
    if name not in accounts:
        print("такого счёта нет")
        return
    
    accounts[name] += amount
    print(f"на счёт '{name}' внесено {amount}")


def withdraw(name: str, amount: float):
    if name not in accounts:
        print("такого счёта нет")
        return
    
    if accounts[name] < amount:
        print("недостаточно средств")
        return
    
    accounts[name] -= amount
    print(f"со счёта '{name}' списано {amount}")


def check_balance(name: str):
    if name not in accounts:
        print("такого счёта нет")
        return
    
    print(f"баланс счёта '{name}': {accounts[name]}")


def transfer(sender: str, receiver: str, amount: float):
    if sender not in accounts or receiver not in accounts:
        print("один из счетов не существует")
        return
    if accounts[sender] < amount:
        print("недостаточно средств для перевода")
        return
    accounts[sender] -= amount
    accounts[receiver] += amount
    print(f"переведено {amount} со счёта '{sender}' на '{receiver}'")