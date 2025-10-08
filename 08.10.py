# домашка номер 3 08.10


# упражнение 1
import random
from typing import List

a = random.randint(0, 100)
for i in range(3):
    try:
        n = int(input("введите число:  "))
        if n < a:
            print("зашаданное число больше")
        elif n > a:
            print("загаданное число меньше")
        else:
            print("вы угадали число")
            exit()
        if i == 1:
            if n%2:
                print('число нечетное')
            else:
                print('число четное')

    except:
        print("вы ввели не число")
print("\nвы не угадали число")
    
# упражнение 2
vowels = 'aeyuio'
not_vowels = set('zaqxswcdevfrbgtnhymjukilop') - set(vowels)
us_word = input('введите предложение: ').lower()

def f(s: str) -> List[str]:
    s_vowels = sum(1 for x in s if x in vowels)
    s_not_vowels = sum(1 for x in s if x in not_vowels)
    space = s.count(' ')
    words = len(s.split(' '))
    sl = {x: 0 for x in set(s)}
    for i in s:
        sl[i] += 1
    sorted_letters = sorted(sl.items(), key = lambda x: x[1], reverse=True)[:3]
    return s_vowels, s_not_vowels, space, words, sorted_letters

s_vowels, s_not_vowels, space, words, sorted_letters = f(us_word)

print(f"количество гласных символов: {s_vowels}")
print(f"количество соггласных символов: {s_not_vowels}")
print(f"количество пробелов: {space}")
print(f"три наиболее встречающихся символа: {sorted_letters}")
print(f"количество слов: {words}")


# упражнение 3
tools = ['камень', 'ножницы', 'бумага']
moves = {'камень': 'ножницы', 'ножницы': 'бумага', 'бумага': 'камень'}

def game() -> str:
    score = [0, 0]
    for _ in range(1, 4):
        user_move = input('ваш ход: [камень\ножницы\бумага]: \n')
        comp_move = random.choice(tools)

        if moves[user_move] == comp_move:
            score[0] += 1
        else:
            score[1] += 1

        if score[0] == 2:
            return 'ты победил'
        elif score[1] == 2:
            return 'компьтер победил'
        
        print(score)

print(game())

# упражнение 4
