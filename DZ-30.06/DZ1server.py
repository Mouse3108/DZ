# Задание 1.
# Реализуйте клиент — серверное приложение, позволяющее двум людям играть в игру крестики — нолики.
# Один из игроков инициирует игру, если второй игрок подтверждает, то игра начинается.
# Игру можно прекратить, тот кто прекратил игру считается проигравшим.
# После завершения игры, можно инициировать повторный матч.

import socket
import threading
import random
import time


clients = {}
players = {'first_player': [], 'second_player': []}


def handle_new_connection(client):
    try:
        while True:
            username = client.recv(1024).decode()
            if username in clients:
                client.send('Игрок с таким именем уже существует. Введите другое имя'.encode())
                continue
            else:
                client.send(f'Добро пожаловать, {username}! Хотите сыграть в "Крестики-Нолики"?'.encode())
                clients[username] = client
                game_mode_selection(client, username)
                break
    except ConnectionAbortedError:
        print(f'Произошла ошибка соединения с {username}.')
    finally:
        print(f'Разорвано соединение с {username}.')
        if username in clients:
            del clients[username]
    client.close()


def game_mode_selection(client, username):
    client.send('1 - с другим игроком\n'
                '2 - с сервером\n'
                '3 - выход\n'
                'Выбор сделайте цифрой (1-3)'.encode())
    while True:
        game_mode = client.recv(1024).decode()
        if game_mode == '3':
            client.send('До новых встреч!'.encode())
            break
        elif game_mode == '1':
            if len(players['first_player']) == 0:
                players['first_player'].append(username)
                players['first_player'].append(client)
                players['first_player'][1].send('...Ожидайте второго игрока...'.encode())
                start = time.time()
                while True:
                    end = time.time() - start
                    if len(players['second_player']) != 0:
                        break
                    if end > 60:
                        players['first_player'][1].send('Ожидание длится больше минуты.\n'
                                                        '1 - ждать\n'
                                                        '2 - выйти\n'
                                                        'Выбор сделайте цифрой (1 или 2)'.encode())
                        answer = players['first_player'][1].recv(1024).decode()
                        if answer == '2':
                            players['first_player'][1].send('Новая игра:'.encode())
                            players['first_player'] = []
                            game_mode_selection(client, username)
                            break
                        elif answer == '1':
                            players['first_player'][1].send('...Ожидайте второго игрока...'.encode())
                            start = time.time()
                            continue
                        else:
                            players['first_player'][1].send('Такого варианта нет!'.encode())
                            continue
            else:
                players['second_player'].append(username)
                players['second_player'].append(client)
            game_board = {'1': '   ', '2': '   ', '3': '   ',
                          '4': '   ', '5': '   ', '6': '   ',
                          '7': '   ', '8': '   ', '9': '   '}
            game_two_players(players['first_player'], players['second_player'], game_board)
            players['first_player'] = []
            players['second_player'] = []
            break
        elif game_mode == '2':
            player_server = {'first_player': [username, client], 'second_player': ['Сервер']}
            first_player = player_server['first_player']
            second_player = player_server['second_player']
            game_board = {'1': '   ', '2': '   ', '3': '   ',
                          '4': '   ', '5': '   ', '6': '   ',
                          '7': '   ', '8': '   ', '9': '   '}
            game_one_players(first_player, second_player, game_board)
            break
        else:
            client.send('Такого варианта нет!'.encode())
            continue


def print_board(board):
    return (f"{board['1']}|{board['2']}|{board['3']}\n"
            f"---+---+---\n"
            f"{board['4']}|{board['5']}|{board['6']}\n"
            f"---+---+---\n"
            f"{board['7']}|{board['8']}|{board['9']}\n")


def victory(board):
    winning_combinations = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                            ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                            ['1', '5', '9'], ['3', '5', '7']]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != '   ':
            return True
    return False


def game_over(board):
    values = []
    for key, value in board.items():
        if value != '   ':
            values.append(value)
        if len(values) == 9:
            return True
    return False


def game_one_players(first_player, second_player, game_board):
    first_player[1].send(f'{first_player[0]}, игра началась!'.encode())
    first_player[1].send(print_board(game_board).encode())
    while True:
        first_player[1].send('Ваш ход. Выберите клетку цифрой от 1 до 9, или 0 для выхода.'.encode())
        position = first_player[1].recv(1024).decode()
        if position == '0':
            first_player[1].send(f'{first_player[0]}, Вы вышли до окончания игры. Вы проиграли!'.encode())
            first_player[1].send('Начать новую игру?\n'.encode())
            break
        elif int(position) in range(1, 10):
            move = ' X '
            if game_board[position] == '   ':
                game_board[position] = move
                first_player[1].send(print_board(game_board).encode())
                if victory(game_board):
                    first_player[1].send(f'{first_player[0]}, поздравляю! Вы выиграли!\n'
                                         f'Начать новую игру?\n'.encode())
                    break
                elif not victory(game_board) and game_over(game_board):
                    first_player[1].send(f'{first_player[0]}, игра окончена. Ничья!\n'
                                         f'Начать новую игру?\n'.encode())
                    break
                else:
                    first_player[1].send(f'Сейчас ходит {second_player[0]}\n'.encode())
                    move = ' 0 '
                    while True:
                        position = str(random.randint(1, 9))
                        if game_board[position] == '   ':
                            game_board[position] = move
                            break
                        else:
                            continue
                    first_player[1].send(print_board(game_board).encode())
                    if victory(game_board):
                        first_player[1].send(f'{first_player[0]}, к сожалению, Вы проиграли :(\n'
                                             f'Начать новую игру?\n'.encode())
                        break
            else:
                first_player[1].send('Эта клетка уже занята'.encode())
            continue
        else:
            first_player[1].send('Такого варианта нет!'.encode())
            continue
    game_mode_selection(first_player[1], first_player[0])


def game_two_players(first_player, second_player, game_board):
    player = first_player
    move = ' X '
    first_player[1].send(f'{first_player[0]}, игра началась\n!'.encode())
    second_player[1].send(f'{second_player[0]}, игра началась! Ожидайте свой ход\n'.encode())
    while True:
        player[1].send(print_board(game_board).encode())
        player[1].send('Ваш ход. Выберите клетку цифрой от 1 до 9, или 0 для выхода.'.encode())
        position = player[1].recv(1024).decode()
        if position == '0':
            player[1].send(f'{first_player[0]}, Вы вышли до окончания игры. Вы проиграли!'.encode())
            player[1].send('Начать новую игру?\n'.encode())
            if player == first_player:
                second_player[1].send(f'Игрок {first_player[0]}, вышел из игры. Вы выиграли!'.encode())
                second_player[1].send('Начать новую игру?\n'.encode())
                break
            else:
                first_player[1].send(f'Игрок {second_player[0]}, вышел из игры. Вы выиграли!'.encode())
                first_player[1].send('Начать новую игру?\n'.encode())
                break
        elif int(position) in range(1, 10):
            if game_board[position] == '   ':
                game_board[position] = move
                player[1].send(print_board(game_board).encode())
                if victory(game_board):
                    player[1].send(f'{first_player[0]}, поздравляю! Вы выиграли!\n'
                                   f'Начать новую игру?\n'.encode())
                    if player == first_player:
                        second_player[1].send(print_board(game_board).encode())
                        second_player[1].send(f'{second_player[0]}, к сожалению, Вы проиграли :(\n'
                                              f'Начать новую игру?\n'.encode())
                        break
                    else:
                        first_player[1].send(print_board(game_board).encode())
                        first_player[1].send(f'{first_player[0]}, к сожалению, Вы проиграли :(\n'
                                             f'Начать новую игру?\n'.encode())
                        break
                elif not victory(game_board) and game_over(game_board):
                    first_player[1].send(f'{first_player[0]}, игра окончена. Ничья!\n'
                                         f'Начать новую игру?\n'.encode())
                    second_player[1].send(f'{second_player[0]}, игра окончена. Ничья!\n'
                                          f'Начать новую игру?\n'.encode())
                    break
                else:
                    if player == first_player:
                        player = second_player
                        move = ' 0 '
                        continue
                    else:
                        player = first_player
                        move = ' X '
                        continue
            else:
                player[1].send('Эта клетка уже занята'.encode())
            continue
        else:
            player[1].send('Такого варианта нет!'.encode())
            continue
    game_mode_selection(first_player[1], first_player[0])
    game_mode_selection(second_player[1], second_player[0])


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 3108
server.bind((host, port))
server.listen()

print(f'Сервер запущен. Используется порт {port}')

while True:
    client_socket, client_address = server.accept()
    print(f'Установлено соединение с {client_address}')
    client_handler = threading.Thread(target=handle_new_connection, args=(client_socket,))
    client_handler.start()
