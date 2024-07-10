# Задание 2.
# Реализуйте клиент — серверное приложение, позволяющее передавать файлы.
# Один пользователь инициирует передачу файла, второй подтверждает.
# После подтверждения начинается отправка.
# Если отправка была удачной необходимо сообщить об этом отправителю.

import socket
import os


def send_file(file_name):
    with open(file_name, "rb") as file:
        while True:
            bytes_read = file.read(4096)
            if not bytes_read:
                break
            client_socket.sendall(bytes_read)


def receive_file(file_name):
    with open(file_name, "wb") as file:
        while True:
            bytes_read = client_socket.recv(4096)
            if not bytes_read:
                break
            file.write(bytes_read)
    print(f'Файл {file_name} успешно получен')


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1812
client_socket.connect((host, port))

try:
    while True:
        username = input('Введите Ваше имя: ')
        client_socket.send(username.encode())
        message_server = client_socket.recv(1024).decode()
        print(message_server)
        if message_server == 'Пользователь с таким именем уже существует. Введите другое имя':
            continue
        else:
            break

    while True:
        message = client_socket.recv(1024).decode()
        if message:
            print(message)
        if message == 'До новых встреч!':
            break
        elif message == 'Введите имя файла':
            file_name = input('Ваш выбор: ')
            if os.path.isfile(file_name):
                client_socket.send(file_name.encode())
                send_file(file_name)
            else:
                print('Файл не найден!')
                client_socket.send('отмена'.encode())
            continue
        elif 'Принять?' in message:
            choice = input('Ваш выбор: ')
            if choice == 'да':
                file_name = client_socket.recv(1024).decode()
                receive_file(file_name)
            continue
        elif 'введите' in message.lower():
            choice = input('Ваш выбор: ')
            client_socket.send(choice.encode())
            continue
except ConnectionAbortedError:
    print('Что-то пошло не так...\nСоединение с сервером потеряно...')
finally:
    client_socket.close()
    print('*** Вы вышли из приложения ***')
