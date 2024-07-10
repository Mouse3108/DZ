# Задание 2.
# Реализуйте клиент — серверное приложение, позволяющее передавать файлы.
# Один пользователь инициирует передачу файла, второй подтверждает.
# После подтверждения начинается отправка.
# Если отправка была удачной необходимо сообщить об этом отправителю.

import socket
import threading

clients = {}
client_states = {}


def handle_new_connection(client):
    try:
        while True:
            username = client.recv(1024).decode()
            if username in clients:
                client.send('Пользователь с таким именем уже существует. Введите другое имя'.encode())
                continue
            else:
                client.send(f'Добро пожаловать в приложение для передачи файлов, {username}!'.encode())
                clients[username] = client
                file_transfer(client, username)
                break
    except ConnectionAbortedError:
        print(f'Произошла ошибка соединения с {username}.')
    finally:
        print(f'Разорвано соединение с {username}.')
        if username in clients:
            del clients[username]
        if username in client_states:
            del client_states[username]
        client.close()


def file_transfer(client, username):
    while True:
        client_states[username] = 'free'
        client.send('Для передачи файла введите "файл"\n'
                    'Для выхода из приложения введите "выход"'.encode())
        try:
            message = client.recv(1024).decode()
        except ConnectionResetError:
            print(f'Произошла ошибка соединения с {username}.')
            break
        if message.lower() == 'выход':
            client.send('До новых встреч!'.encode())
            break
        elif message.lower() == 'файл':
            client_states[username] = 'busy'
            client.send('Пользователи:'.encode())
            for key in clients:
                client.send(f'{key}\n'.encode())
            client.send('Введите имя пользователя, которому хотите передать файл'.encode())
            user = client.recv(1024).decode()
            if user not in clients:
                client.send('Такого пользователя нет'.encode())
            elif user == username:
                client.send('Вы не можете отправить файл самому себе'.encode())
            else:
                client.send('Введите имя файла'.encode())
                file_name = client.recv(1024).decode()
                if file_name == 'отмена':
                    continue
                client.send(f'Ожидайте ответ от пользователя {user}'.encode())
                while True:
                    if client_states[user] == 'busy':
                        continue
                    else:
                        clients[user].send(f'Пользователь {username} передает Вам файл {file_name}.\n'
                                           f'Принять? Введите "да" или "нет"'.encode())
                        answer = clients[user].recv(1024).decode()
                        if answer.lower() == 'да':
                            receive_file(client, 'new_' + file_name)
                            clients[user].send(f'new_{file_name}'.encode())
                            send_file(clients[user], 'new_' + file_name)
                            client.send(f'Файл {file_name} успешно передан пользователю {user}'.encode())
                        else:
                            client.send(f'Пользователь {user} отказался принимать файл {file_name}'.encode())
                        break
                continue
        else:
            client.send('Такого варианта нет!'.encode())
            continue


def receive_file(send_socket, file_name):
    with open(file_name, "wb") as file:
        while True:
            bytes_read = send_socket.recv(4096)
            if not bytes_read:
                break
            file.write(bytes_read)


def send_file(receiver_socket, file_name):
    with open(file_name, "rb") as file:
        while True:
            bytes_read = file.read(4096)
            if not bytes_read:
                break
            receiver_socket.sendall(bytes_read)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 1812
server.bind((host, port))
server.listen()

print(f'Сервер запущен. Используется порт {port}')

while True:
    client_socket, client_address = server.accept()
    print(f'Установлено соединение с {client_address}')
    client_handler = threading.Thread(target=handle_new_connection, args=(client_socket,))
    client_handler.start()
