import random

# ВИСЕЛИЦА

words = ["компьютер", "компуктер", "дрындулет", "терминатор"]

def hangman():
    word = random.choice(words)
    guessed = ["_"] * len(word) 
    att = 10                 
    used_letters = set()

    print("слово:", " ".join(guessed))

    while att > 0 and "_" in guessed:
        letter = input("введи букву: ")
        if letter in used_letters:
            print("буква уже была")
            continue
        used_letters.add(letter)
        if letter in word:
            for i in range(len(word)):
                if word[i] == letter:
                    guessed[i] = letter
            print("есть попадание")
        else:
            attempts -= 1
            print(f"мимо. осталось попыток: {attempts}")

        print("слово:", " ".join(guessed))

    if "_" not in guessed:
        print("ты выйграл")
    else:
        print(f"проиграл, слово было: {word}")

print(hangman())




