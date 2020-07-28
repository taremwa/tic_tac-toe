import itertools
from colorama import Fore, Back, Style, init
init()

# python Basics___ Tic_Tac_Toe_Game---


def win(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # Horizontal winner
    for row in game:
        print(row)
        if all_same(row):
            print("Winner horizontally (--)!")
            return True

    # Vertical Winner
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])

        if all_same(check):
            print("Winner vertically (|)!!")
            return True

    # Diagonal Winner
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print("Winner diagonally (/)!")
        return True

    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print("Winner diagonally (\\)")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position is occupied! choose another!")
            return game_map, False
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player

        for count, row in enumerate(game_map):
            # Applying colorama
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
            print(count, colored_row)

        return game_map, True
    except IndexError as e:
        print("Input not Valid!, input row/column as 0 1 or 2", e)
        return game_map, False

    except Exception as e:
        print("Something went very wrong!!", e)
        return game_map, False


play = True
players = [1, 2]
while play:
    '''
            # Dynamic game size
    game_size = int(input("Choose your game size for tic tac toe"))
    game = [[0 for in range(game-size)] for i in range(game_size)]
    '''

    game = [[0,  0,  0],
            [0,  0,  0],
            [0,  0,  0]]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            column_choice = int(input("Choose a column to play on (0, 1, 2): "))
            row_choice = int(input("Choose a row to play on (0, 1, 2): "))
            game, played = game_board(game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Game Over!! Would you like to play again? (y/n) ")
            if again.lower() == "y":
                print("Restarting..... ")
            elif again.lower() == "n":
                print("Thank you for playing, See you next time! ")
                play = False
            else:
                print("invalid input, Try again..")
                play = False
