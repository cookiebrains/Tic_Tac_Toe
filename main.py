import time as t


def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


def directions(player_1, player_2):
    print(f'\n Hello {player_1} & {player_2}!\n{player_1} is "X" and {player_2} is "O"')
    print(f'\n Players select where to play by entering the numbers 1 though 9 according to the following layout.')
    demo_values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print_tic_tac_toe(demo_values)
    print('Game will begin in 5 seconds.')
    t.sleep(5)


def new_input_loop(player_1, player_2, turn, values):
    print_tic_tac_toe(values)
    if turn % 2 == 0:
        move = int(input(f"{player_1}'s turn. Select an available square by typing a number between 1 and 9.")) - 1
    else:
        move = int(input(f"{player_2}'s turn. Select an available square by typing a number between 1 and 9.")) - 1
    return move


def check_for_winner(values):
    if values[0] == 'X' and values[1] == 'X' and values[2] == 'X' or \
            values[3] == 'X' and values[4] == 'X' and values[5] == 'X' or \
            values[6] == 'X' and values[7] == 'X' and values[8] == 'X' or \
            values[0] == 'X' and values[3] == 'X' and values[6] == 'X' or \
            values[1] == 'X' and values[4] == 'X' and values[7] == 'X' or \
            values[2] == 'X' and values[5] == 'X' and values[8] == 'X' or \
            values[0] == 'X' and values[4] == 'X' and values[8] == 'X' or \
            values[2] == 'X' and values[4] == 'X' and values[6] == 'X':
        return 'X'

    elif values[0] == 'O' and values[1] == 'O' and values[2] == 'O' or \
            values[3] == 'O' and values[4] == 'O' and values[5] == 'O' or \
            values[6] == 'O' and values[7] == 'O' and values[8] == 'O' or \
            values[0] == 'O' and values[3] == 'O' and values[6] == 'O' or \
            values[1] == 'O' and values[4] == 'O' and values[7] == 'O' or \
            values[2] == 'O' and values[5] == 'O' and values[8] == 'O' or \
            values[0] == 'O' and values[4] == 'O' and values[8] == 'O' or \
            values[2] == 'O' and values[4] == 'O' and values[6] == 'O':
        return 'O'
    elif ' ' not in values:
        return 'tie'


def game():
    player_1 = input(f'What is the name of Player 1?')
    player_2 = input(f'What is the name of Player 2?')
    directions(player_1, player_2)
    turn = 0
    values = [' ' for val in range(9)]
    while True:
        new_input = new_input_loop(player_1, player_2, turn, values)
        if turn % 2 == 0:
            values[new_input] = "X"
        else:
            values[new_input] = "0"
        if check_for_winner(values) == 'X':
            print_tic_tac_toe(values)
            print(f'{player_1} wins!')
            break

        if check_for_winner(values) == 'O':
            print_tic_tac_toe(values)
            print(f'{player_2} wins!')
            break

        if check_for_winner(values) == 'tie':
            print_tic_tac_toe(values)
            print('Tie Game!')
            break


        turn += 1
    print(f'Good Game {player_1} and {player_2}!')
    new_game = input("To play again type 'y'. To quit type 'q'.")
    if new_game == 'y':
        game()
    else:
        print("Goodbye!")


game()
