import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
amb = 'il1Lo0O'
counter = 0
print('Какое количество паролей для генерации?')
number_of_passwords = int(input())
print('Какая длина одного пароля?')
password_length = int(input())
print('Включать ли цифры', digits, '? да или нет')
numbers = input()
if numbers == 'да':
    chars += digits
print('Включать ли прописные буквы', uppercase_letters, '? да или нет')
uppercase = input()
if uppercase == 'да':
    chars += uppercase_letters
print('Включать ли строчные буквы', lowercase_letters, '? да или нет')
lowercase = input()
if lowercase == 'да':
    chars += lowercase_letters
print('Включать ли символы', punctuation, '? да или нет')
symbols = input()
if symbols == 'да':
    chars += punctuation
print('Включать ли неоднознаные символы', amb, '? да или нет')
ambiguous = input()
if ambiguous == 'нет':
    for c in amb:
        chars = chars[:int(chars.find(c))] + chars[int(chars.find(c)):]
while counter != number_of_passwords:
    counter += 1
    password = ''
    for i in range(password_length):
        password += random.choice(chars)
    print(password)
        
