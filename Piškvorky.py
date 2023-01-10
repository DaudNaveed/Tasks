from random import randint
import argparse
import sys


board = [['', '', ''], ['', '', ''], ['', '', '']]  # The TicTacToe board
win_board = [['', '', ''], ['', '', ''], ['', '', '']]  # Traces the win (if any) of 'board'

X = 'X'  # Character for player 1
O = 'O'  # Character for player 2

player = X # Player name
computer = O
size = 3  # Size of 'board'


def countWins(p1, p2):
    count = 0  # Keeps count of wins possible

    for i in range(size):
        for j in range(size):
            if board[i][j] != p1 and board[i][j] != p2:
                copy = board[i][j]  # A dummy variable to restore 'board[i][j]'
                board[i][j] = p1

                if win(p1) == 1:
                    count += 1

                board[i][j] = copy

    return count

def ai_move(ai, pl, x=0, name=''):
    l = 0
    possible = [[i, j] for i in range(size) for j in range(size)]

    available = []

    for i in range(len(possible)):
        x = possible[i][0]
        y = possible[i][1]

        if board[x][y] != ai and board[x][y] != pl:
            available.append(possible[i])
            l += 1

    r = available[randint(1, 1000) % l]
    board[r[0]][r[1]] = ai

    if x:
        move = name + ' Moved To Grid', r[0] * size + r[1] + 1
        sys.stdout.write(str(move))
        print('\n')
    return

def get_user_move(p1, p2):
    print(f'Please Enter Grid Number (1 ~ {size * size}): ')
    g = int(sys.stdin.readline()) - 1

    x = g // size
    y = g % size

    if x >= size or y >= size or board[x][y] == p1 or board[x][y] == p2:
        sys.stdout.write('Please Enter A Valid Move')
        get_user_move(p1, p2)
        return
    pl_move = player + ' Moved To Grid', g + 1
    sys.stdout.write(str(pl_move))
    board[x][y] = p1
    print('\n')

def get_win(p):
    for i in range(size):
        # Rows
        if all(board[i][j] == p for j in range(size)):
            for j in range(size):
                win_board[i][j] = p
            return

        # Columns
        if all(board[j][i] == p for j in range(size)):
            for j in range(size):
                win_board[j][i] = p
            return

    # Diagonals
    if all(board[i][i] == p for i in range(size)):
        for i in range(size):
            win_board[i][i] = p
        return

    if all(board[i][-(i + 1)] == p for i in range(size)):
        for i in range(size):
            win_board[i][-(i + 1)] = p
        return

def printBoard():
    for i in range(size - 1):
        for j in range(size - 1):
            print(board[i][j], end=' | ')
        print(board[i][-1])
        print('---' * size + '-' * (size - 3))

    for j in range(size - 1):
        print(board[-1][j], end=' | ')

    print(board[-1][-1])
    print()

def printWin(p):
    get_win(p)

    for i in range(size - 1):
        for j in range(size - 1):
            print(win_board[i][j], end=' | ')
        print(win_board[i][-1])
        print('---' * size + '-' * (size - 2))

    for j in range(size - 1):
        print(win_board[-1][j], end=' | ')

    print(win_board[-1][-1])
    print()

def main_menu(x,y):
    global size
    size = x
    print('Q for exit')
    print('1. Play')
    print('Please Enter Your Option: ')
    option = sys.stdin.readline()
    if option.rstrip() == '1':
        initialize()
        play('0', 'X')

    if option.rstrip() == 'q' or option.rstrip() == 'Q':
        print('Thanks For Playing!\n')
        return

def play(p1, p2):
    initialize()
    print( player + ' VS ' + computer)
    print('type start if you want the AI to take first move')
    turn = sys.stdin.readline()
    turn = turn.rstrip().lower()
    if turn == 'start':
        c = 0
    else: 
        c = 1
    pl = p1
    ai = p2

    if c == 0:
        ai = p1
        pl = p2
        print('\n' + computer + ' Goes First!\n')
    else:
        print('\n' + player + ' Goes First!\n')
        printBoard()

    d = 0

    while True:
        t = d % 2

        if t == c:
            ai_move(ai, pl, 1, computer)
            printBoard()

            if win(ai):
                print(computer + ' Wins!\n')
                print('Below Is How ' + computer + ' Won\n\n')
                printWin(ai)
                break

        else:
            get_user_move(pl, ai)
            printBoard()
            if win(pl):
                print(player + ' Wins!')
                print('Below Is How ' + player + ' Won\n')
                printWin(pl)
                break

        if tie():
            print('Tie!')
            break

        d += 1


def initialize():
    """ Resets the board """
    global board, win_board
    board = [[' ' for _ in range(size)] for __ in range(size)]
    win_board = [[' ' for _ in range(size)] for __ in range(size)]

def win(p):
    """ Checks for win """

    if any(all(board[i][j] == p for j in range(size)) for i in range(size)):
        return True
    if any(all(board[j][i] == p for j in range(size)) for i in range(size)):
        return True
    if all(board[i][i] == p for i in range(size)):
        return True
    if all(board[i][-(i + 1)] == p for i in range(size)):
        return True

    return False

def tie():
    """ Checks for tie """

    return all(all(j in [X, O] for j in i) for i in board)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('x', type=int)
    parser.add_argument('y', type=int)
    args = parser.parse_args()
    main_menu(args.x,args.y)