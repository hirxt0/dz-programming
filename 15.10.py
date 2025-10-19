from datetime import datetime, date
from decimal import Decimal

goods = {
    'Пельмени Универсальные': [
        # Первая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('0.5'), 'expiration_date': date(2023, 7, 15)},
        # Вторая партия продукта 'Пельмени Универсальные':
        {'amount': Decimal('2.0'), 'expiration_date': date(2023, 8, 1)},
    ],
    'Вода': [
        {'amount': ('1.5 л'), 'expiration_date': None}
    ],
}

def is_valid_date(date, date_format):
    try: 
        datetime.strptime(date, date_format)
        return True
    except:
        return False



def add(good: str):
    parts = [x.strip() for x in good.split(",")]
    name = parts[0]
    amount = Decimal(parts[1].strip().split(' ')[0])
    date = parts[2] if len(parts[2]) > 2 else None
    
    if date and is_valid_date(date, '%Y-%m-%d'):
        expiration = datetime.strptime(date, '%Y-%m-%d').date()
    else:
        expiration = None
    if name in goods:
        goods[name].append({'amount': amount, 'expiration_date': expiration})
    else:
        goods[name] = ({'amount': amount, 'expiration_date': expiration})


def find(path: str):
    res = []   
    for key in goods.keys():
        if path.lower() in key.lower():
            res.append(key)
    return res


def amount(path: str):
    total = Decimal('0')
    for key in find(path):
        for item in goods[key]:
            total += item['amount']
    return total



if __name__ == "__main__":
    while True:
        n = input("Введите - название продукта, объем(0.0), срок годности(год-месяц-день): ")
        add(n)
        print(goods)