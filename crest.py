
board = [1,2,3,4,5,6,7,8,9]

def game_board():
    # Функция печати поля
    print('_' * 13)
    for i in range(3):
        print((('|' + ' ' * 3) * 3)+'|')
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print((('|'+'_' * 3) * 3)+'|')

def step_control(user_input: int ,current_player) -> bool:
    # Функция корректности ввода
    if user_input > 9 or user_input < 1 or board[user_input - 1] in ('X', 'O'):
        # если введен некорректный номер поля или поле занято
        return False
    board[user_input - 1] = current_player
    return True

def check_win():
    # Функция проверки завершенности игры
    win = False
    win_combinations = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_combinations:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            win = board[i[0]]
    return win

def start_game():
    # первым ходит игрок X
    current_player = 'X'
    step = 1
    game_board()
    while step < 10 and check_win() == False:
        user_input = input('Ход игрока ' + current_player + '. Введите номер поля (1-9). Для выхода нажмите 0:')

        if int(user_input) == 0:
            break

        if user_input.isdigit():
            print(f'Выбрано поле {int(user_input)}')
        else:
            print('Необходимо ввести номер поля: 1-9')
            continue

        if step_control(int(user_input),current_player):
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

            game_board()
            step += 1
        else:
            print('Неверный ход, повторите:')
    if step == 10:
        print('Игра окончена, ничья')
    elif check_win() != False:
        print('Выиграл ' + check_win())

print('Welcome')
start_game()
