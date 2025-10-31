import random
import string

def generate_password(length=12, use_digits=True, use_lowercase=True, 
                     use_uppercase=False, use_special=False):
    charset = '' 
    if use_digits:
        charset += string.digits 
    if use_lowercase:
        charset += string.ascii_lowercase
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_special:
        charset += string.punctuation
    if not charset:
        raise ValueError("необходимо выбрать хотя бы один тип символов")
    
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

try:
    length = int(input("длина пароля (4-32): "))
except ValueError:
    print('неправильный ввод')
use_digits = input("использовать цифры? (y/n): ").lower() == 'y'
use_lowercase = input("использовать строчные буквы? (y/n): ").lower() == 'y'
use_uppercase = input("использовать заглавные буквы? (y/n): ").lower() == 'y'
use_special = input("использовать специальные символы? (y/n): ").lower() == 'y'

custom_password = generate_password(length, use_digits, use_lowercase, 
                                   use_uppercase, use_special)
print(f"\nваш пароль: {custom_password}")