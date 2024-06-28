# Задание 4.
# Пользователь с клавиатуры вводит путь к существующей директории и слово для поиска.
# После чего запускаются два потока. Первый должен найти файлы, содержащие искомое слово
# и слить их содержимое в один файл. Второй поток ожидает завершения работы первого потока.
# После чего проводит вырезание всех запрещенных слов (список этих слов нужно считать из файла
# с запрещенными словами) из полученного файла.
# На экран необходимо отобразить статистику выполненных операций.


import os
import threading
import re


class FilesThread(threading.Thread):
    def __init__(self, func, args):
        super().__init__()
        self.func = func
        self.args = args
        self.result = None

    def run(self):
        self.result = self.func(*self.args)
        print(self.result)


def find_files_with_word(directory, word):
    text = ''
    for root, i, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='windows-1251', errors='ignore') as f:
                content = f.read()
                if word in content:
                    text += content + '\n'
                    print(f'Слово {word} найдено в {file_path}')
    with open('all_text.txt', 'w') as f:
        f.write(text)
    return f'Содержимое всех файлов со словом "{word}" записано в "all_text.txt"'


def filter_forbidden_words(file_with_text, file_with_words):
    with open(file_with_words, 'r') as f:
        forbidden_words = f.read().split()
    with open(file_with_text, 'r') as f:
        content = f.read()
    for word in forbidden_words:
        pattern = r'\b' + re.escape(word) + r'\b'
        content = re.sub(pattern, '***', content)
    with open(file_with_text, 'w') as f:
        f.write(content)
    return f'Запрещенные слова {forbidden_words} в файле "file_with_text" заменены на ***'


directory = input("Введите путь к существующей директории: ")
word = input("Введите слово для поиска: ")

thread1 = FilesThread(find_files_with_word, (directory, word))
thread1.start()
thread1.join()

thread2 = FilesThread(filter_forbidden_words, ('all_text.txt', 'forbidden_words.txt'))
thread2.start()
