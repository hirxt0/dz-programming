vowels = 'aeyuio'
consonants = set('zaqxswcdevfrbgtnhymjukilop') - set(vowels)
us_word = input('введите предложение: ').lower()

def string_processing(s: str):
    s_vowels = sum(1 for x in s if x in vowels)

    s_consonants = sum(1 for x in s if x in consonants)

    space = s.count(' ')

    words = len(s.split(' '))

    sl = {x: 0 for x in set(s)}
    for i in s:
        sl[i] += 1
    sorted_letters = sorted(sl.items(), key = lambda x: x[1], reverse=True)[:3]

    return s_vowels, s_consonants, space, words, sorted_letters

s_vowels, s_consonants, space, words, sorted_letters = string_processing(us_word)

print(f"количество гласных символов: {s_vowels}")
print(f"количество согласных символов: {s_consonants}")
print(f"количество пробелов: {space}")
print(f"три наиболее встречающихся символа: {sorted_letters}")
print(f"количество слов: {words}")