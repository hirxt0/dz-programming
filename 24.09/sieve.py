def eratosphene(n: int):

    arr = list(range(2, n + 1))
    for i in arr:
        arr = [x for x in arr if (x % i != 0 or x == i)]
    return arr


print(eratosphene(50))

# решение чуть быстрее

def eratosphen_2(n: int):

    arr = [True] * n
    arr[0] = arr[1] = False
    for i in range(2, len(arr)):
        if arr[i]:
            for j in range(i*i, len(arr), i):
                arr[j] = False
    return [i for i, status in enumerate(arr) if status]


print(eratosphen_2(50))