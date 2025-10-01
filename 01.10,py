import random


# шифр цезаря
alf1 = 'abcdefghijklmnopqrstuvwxyz'
alf2 = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
digits = '1234567890'
special_symbols = '!"#$%&''()*+,-./:;<=>?@[\]^_`{|}'

def shifr(ch: str, n: int) -> str:
  res = ''
  for i in range(len(ch)):
    if ch[i] in alf2:
      res += alf2[(alf2.index(ch[i]) + n) % 32]
    elif ch[i] in alf1:
      res += alf1[(alf1.index(ch[i]) + n) % 25]
  return res

def de_shifr(ch: str, n: int) -> str:
    res = ''
    for i in range(len(ch)):
      if ch[i] in alf2:
        res += alf2[(alf2.index(ch[i]) - n) % 32]
      elif ch[i] in alf1:
        res += alf1[(alf1.index(ch[i]) - n) % 25]
    return res

ch =  input('введите слово: ').lower()
n = int(input('на какое количество знаков сдвиг: '))
if not n or n > 36:
  print("некоректный ввод")
  exit()

do = input("шифровать или дешифровать?: ")
if do == 'шифровать':
  print(f"ваша строка: {shifr(ch, n)}")
elif do == 'дешифровать':
  print(f"ваша строка: {de_shifr(ch, n)}")
else:
  print("не правильный ввод")




def check_winner(scores: list, student_score: int) -> str:
  scores.sort()
  if len(scores) <= 3:
    'стас молодец'
  return 'стас молодец' if student_score in score[-3:] else 'стас не молодец'



def print_pack_report(n: int) -> str:
  for i in range(n, 0, -1):
    if i % 5 == 0 and i % 3 == 0:
      print(f'{i}, расфасуем и по 3 и по 5')
    elif i % 5 == 0:
      print(f'{i}, расфасуем по 5')
    elif i % 3 == 0:
      print(f'{i}, расфасуем по 3')
    else:
      print(f'{i}, не сможем нормально расфасовать')
  return 'конец'
print(print_pack_report(10))


# создание пароля
def f(s: str) -> int:
  if s == 'Y':
    return 1
  return 0

print('Настройки пароля:')
add_lower_registr = f(input('Нижний регистр Y/N '))
add_upper_registr = f(input('Верхний регистр Y/N '))
add_special_symbols = f(input('Специальные символы Y/N '))
add_digits = f(input('Цифры Y/N '))
len_parol = int(input('Длина пароля: '))
def parol(add_digits, add_lower_registr, add_special_symbols, add_upper_registr, len_parol):
  curr_parol = list((alf1.upper() * add_upper_registr + alf1 * add_lower_registr + special_symbols * add_special_symbols
                + digits * add_digits))
  if curr_parol == []:
    return 'пароля не будет'
  a = random.shuffle(curr_parol)
  res_parol = "".join(curr_parol[: len_parol - 1])
  return res_parol
print(parol(add_digits, add_lower_registr, add_special_symbols,add_upper_registr, len_parol))


# конвертация римских цифр
def convertation(n: int) -> str:
  sl = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: "L", 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
  res = []
  for val, key in sl.items():
    while n >= val:
      res.append(key)
      n -= val
  return "".join(res)



def anti_conversation(ch: str) -> int:
  sl = {'M': 1000,'D': 500, 'C': 100, "L": 50, 'X': 10, 'V': 5, 'I': 1}
  res = 0
  for i in range(len(ch) - 1):
    if sl[ch[i]] < sl[ch[i + 1]]:
      res -= sl[ch[i]]
    else:
      res += sl[ch[i]]
  res += sl[ch[-1]]
  return res





