import re

# Задание 1.
# Напишите регулярное выражение, которое соответствует всем строкам,
# начинающимся с гласной и заканчивающимся на согласную.
print('Задание 1:')
strings = ('а напишите регулярное выраж', 'ение которое соответствует', 'всем строкам начинающимся с гласной',
          'И заканчивающимся на согласн', 'ую. Это первое задание')
pattern1 = r'[аАеЕёЁиИоОуУэЭюЮяЯ].*[бБвВгГдДжЖзЗкКлЛмМнНпПрРсСтТфФхХцЦчЧшШщЩьЬъЪ]$'
for vowels_consonants in strings:
    if re.findall(pattern1, vowels_consonants):
        print(vowels_consonants)

print()
# Задание 2.
# Напишите регулярное выражение, которое соответствует всем URL-адресам.
print('Задание 2:')


def verification_URL_address(URL_address):
    pattern2 = r'https?://(www.)?[a-zA-Z0-9.-/]+.[com|ru].*?'
    if re.findall(pattern2, URL_address):
        print(f'{URL_address} - соответствует URL-адресам')
    else:
        print(f'{URL_address} - не соответствует URL-адресам')


verification_URL_address('https://journal.top-academy.ru/ru/main/homework/')
verification_URL_address('https:/journal.top-academy')
verification_URL_address('www.journal.top-academy.ru/ru/main/homework/')
verification_URL_address('http://www.google.com')

print()
# Задание 3. Напишите регулярное выражение, которое соответствует всем строкам,
# содержащим хотя бы одно слово, начинающееся с заглавной буквы.
print('Задание 3:')
strings2 = ('напишите регулярное Выражение', 'которое соотвЕтствует всем строкам,',
           'содержащим Хотя бы одно слово,', 'начинаЮщееся с зАглавной буквы.')
pattern3 = r'\b[А-Я][а-я]+\b'
for capital_letter in strings2:
    if re.findall(pattern3, capital_letter):
        print(capital_letter)

print()
# Задание 4. Напишите регулярное выражение, которое соответствует всем строкам,
# содержащим повторяющуюся букву (например, "book" или "letter").
print('Задание 4:')
strings3 = ('Напишите регулярное выражение, которое соответствует всем строкам, '
            'содержащим повторяющуюся букву (например, "book" или "letter"')
pattern4 = r'\b(\w*?)(\w)\2(\w*)\b'
words = re.finditer(pattern4, strings3)
for word in words:
    print(word.group(0))