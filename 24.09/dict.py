# добавление случаев, где слоарь состоит из менее чем трех элементов

n = input('введите строку: ').lower()
char_count = {}
for char in n:
    if char in char_count.keys():
        char_count[char] += 1
    else:
        char_count[char] = 1
char_list = []
for key, item in char_count.items():
    char_list.append((key, item))


char_list = sorted(char_list, key =lambda x: x[1], reverse = True)

if len(char_list) >= 3:
    for i in range(3):
        char, count = char_list[i]
        print(f"{i + 1}) {char}: {count}")

elif len(char_list) == 2:
    for i in range(2):
        char, count = char_list[i]
        print(f"{i + 1}) {char}: {count}")

else:
    char, count = char_list[0]
    print(f"{char}: {count}")
