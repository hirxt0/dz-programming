import random

hidden_number = random.randint(0, 100)
for i in range(3):
    try:
        user_number = int(input("введите число:  "))
        if user_number < hidden_number:
            print("зашаданное число больше")
        elif user_number > hidden_number:
            print("загаданное число меньше")
        else:
            print("вы угадали число")
            exit()
        if i == 1:
            if user_number%2:
                print('число нечетное')
            else:
                print('число четное')

    except:
        print("вы ввели не число")
print("\nвы не угадали число")
    