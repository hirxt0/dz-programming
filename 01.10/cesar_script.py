alf1 = 'abcdefghijklmnopqrstuvwxyz'
alf2 = 'абвгдеёжзийклмнопрстуфхцчшщьыъэюя'
digits = '1234567890'
special_symbols = '!"#$%&''()*+,-./:;<=>?@[\]^_`{|}'

def shifr(ch: str, n: int) -> str:
  res = ''
  for i in range(len(ch)):
    if ch[i] in alf2:
      res += alf2[(alf2.index(ch[i]) + n) % 33]
    elif ch[i] in alf1:
      res += alf1[(alf1.index(ch[i]) + n) % 26]
  return res

def de_shifr(ch: str, n: int) -> str:
    res = ''
    for i in range(len(ch)):
      if ch[i] in alf2:
        res += alf2[(alf2.index(ch[i]) - n) % 33]
      elif ch[i] in alf1:
        res += alf1[(alf1.index(ch[i]) - n) % 26]
    return res

ch =  input('введите слово: ').lower()
n = int(input('на какое количество знаков сдвиг: '))
if n <= 0 or n > 36:
  print("некоректный ввод")
  exit()

do = input("шифровать или дешифровать?: ")
if do == 'шифровать':
  print(f"ваша строка: {shifr(ch, n)}")
elif do == 'дешифровать':
  print(f"ваша строка: {de_shifr(ch, n)}")
else:
  print("не правильный ввод")