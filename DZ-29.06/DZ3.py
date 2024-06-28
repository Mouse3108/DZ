# Задание 3.
# Пользователь с клавиатуры вводит путь к существующей директории и к новой директории.
# После чего запускается поток, который должен скопировать содержимое директории в новое место.
# Необходимо сохранить структуру директории.
# На экран необходимо отобразить статистику выполненных операций.

import os
import shutil
import threading


def copy_dir(existing_directory, new_directory):
    if not os.path.exists(new_directory):
        os.makedirs(new_directory)
    for item in os.listdir(existing_directory):
        existing_path = os.path.join(existing_directory, item)
        new_path = os.path.join(new_directory, item)
        if os.path.isdir(existing_path):
            os.makedirs(new_path)
            copy_dir(existing_path, new_path)
        else:
            shutil.copy(existing_path, new_path)
        print(f'В директорию {new_directory}  скопировано: {item}')


existing_directory = input('Введите путь к существующей директории, которую необходимо скопировать: ')
new_directory = input('Введите путь к новой директории, куда скопировать информацию: ')


t = threading.Thread(target=copy_dir, args=(existing_directory, new_directory))
t.start()

