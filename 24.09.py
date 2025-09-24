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


# решето эратосфена

def eratosphene(n):
    arr = list(range(2, n + 1))
    for i in arr:
        arr = [x for x in arr if (x % i != 0 or x == i)]
    return arr
print(eratosphene(100))

# решение чуть быстрее

def eratosphen(n)
    arr = [True] * n
    arr[0] = arr[1] = False
    for i in range(2, len(arr)):
        if arr[i]:
            for j in range(i*i, len(arr), i):
                arr[j] = False
    return [i for i, status in enumerate(arr) if status]
print(eratosphen(100))

             


