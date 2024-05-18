import re

# Задание 4. Напишите регулярное выражение, которое найдет все ссылки в тексте,
# включая ссылки на веб-сайты (http/https), электронные адреса и ссылки на файлы.
# Затем оберните его в функцию, которая возвращает данные в виде словаря:
# {"Ссылки": [...], "Почты": [...], "Файлы": [...]}


def all_links(text):
    link_pattern = r'https?://(?:www\.)?[a-zA-Z\d.-]+\.(?:com|ru)'
    email_pattern = r'[a-zA-Z\d.-_]+@[a-zA-Z\d.-]{2,}\.(?:ru|com)'
    file_pattern = r'[\w\d!@$%&()-_.,]+\.(?:pdf|doc|docx|xlsx|txt|py)'
    links_dictionary = {
        'Ссылки': re.findall(link_pattern, text),
        'Почты': re.findall(email_pattern, text),
        'Файлы': re.findall(file_pattern, text)
    }
    return links_dictionary


text = ('Домашнее задание можно отправить в виде ссылки: https://github.com на сайт https://journal.top-academy.ru. '
        'Или отправить файлы DZ.py или DZ.txt на электронную почту: boboshko_k@t.top-academy.ru')
print(all_links(text))