import random
def disboard(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def pl_ip():
    marker=' '
    while not (marker=='x' or marker=='o'):
        marker=input('player 1, choose x or o:').lower()
    if marker=='x':
        return ('x','o')
    else:
        return ('o','x')

def place_mrk(board,mrk,position):
    board[position]=mrk

def win_check(board,mrk):
    return ((board[1]==board[2]==board[3]==mrk or
             board[4]==board[5]==board[6]==mrk or
             board[7]==board[8]==board[9]==mrk or
             board[1]==board[4]==board[7]==mrk or
             board[2]==board[5]==board[8]==mrk or
             board[3]==board[6]==board[9]==mrk or
             board[1]==board[5]==board[9]==mrk or
             board[3]==board[5]==board[7]==mrk))

def choosefirst():
    flip=random.randint(0,1)
    if flip==0:
        return 'player 1'
    else:
        return 'player 2'

def space_check(board,position):
   return board[position]==' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def pl_choice(board):
    position=0
    while position not in range(1,10) and not space_check(board,position):
        position=int(input('Choose a Position (1-9): '))
    return position

def replay():
    choice=input('Play again? Enter yes or no: ').lower()
    return choice=='y'

print('Welcome to the Tic Tac Toe.')
while True:
    tb=[' ']*10
    player1_mrk,player2_mrk=pl_ip()
    turn=choosefirst()
    print(turn+' will go first')
    play_game=input(' ready to play?y or n: ')
    if play_game=='y':
        game_on= True
    else:
        game_on=False

    while game_on:
        if turn=='player 1':
            disboard(tb)
            position=pl_choice(tb)
            place_mrk(tb,player1_mrk,position)
            if win_check(tb,player1_mrk):
                disboard(tb)
                print('player 1 has won!!')
                game_on=False
            else:
                if full_board_check(tb):
                    disboard(tb)
                    print('tie game')
                    game_on=False
                else:
                    turn='player 2'
        else:
            disboard(tb)
            position = pl_choice(tb)
            place_mrk(tb, player2_mrk, position)
            if win_check(tb, player2_mrk):
                disboard(tb)
                print('player 2 has won!!')
                game_on = False
            else:
                if full_board_check(tb):
                    disboard(tb)
                    print('tie game')
                    game_on = False
                else:
                    turn = 'player 1'
    if not replay():
        break