# Задание 1.
# Реализуйте клиент — серверное приложение, позволяющее двум людям играть в игру крестики — нолики.
# Один из игроков инициирует игру, если второй игрок подтверждает, то игра начинается.
# Игру можно прекратить, тот кто прекратил игру считается проигравшим.
# После завершения игры, можно инициировать повторный матч.

import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 3108
client_socket.connect((host, port))

try:
    while True:
        username = input('Введите Ваше имя: ')
        client_socket.send(username.encode())
        message_server = client_socket.recv(1024).decode()
        print(message_server)
        if message_server == 'Игрок с таким именем уже существует. Введите другое имя':
            continue
        else:
            break

    while True:
        message = client_socket.recv(1024).decode()
        print(message)
        if 'цифрой' in message:
            while True:
                choice = input('Ваш выбор: ')
                client_socket.send(choice.encode())
                message = client_socket.recv(1024).decode()
                if message:
                    print(message)
                if message != 'Такого варианта нет!':
                    break
                else:
                    continue
        if message == 'До новых встреч!':
            break
except ConnectionResetError:
    print('Что-то пошло не так...\nСоединение с сервером потеряно...')
finally:
    client_socket.close()
    print('*** Вы вышли из игры ***')
