def display_board(board):
    
    print('   |   |') # 3 space + 3
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------') #11
    print('   |   |')##عشان بنجمع نصوص لازم الليست نصوص
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

#display_board(["x","o","x","o","x","o","x","o","x","o"])
def select_marker_input():
    marker=" "
    while not(marker=='X'or marker=='O'):#if the user enters a value other than x or o
        print("Choose only  X or O")
        marker=input("player1: Do you want X or O? ").upper()
    if marker=='X':
        return('X','O')#save values player1-->X , player2-->o
    elif marker =='O':
        return('O','X')
#random integer ==>0,,,player2 starts ...random==>1...player 1 starts 
import random 
def choose_first():
    if random.randint(0,1)==0:
        return 'player2'
    else:
        return'player1'
##put values in a list
def place_marker(board,marker,position):#لنعطي قيم لليست
    board[position]=marker
#board=['X','O','']
#place_marker(board, 'X',2)
#print(board)
def space_check(board,position):
    return board[position] == ' '
#board=['X','o',' ']
#space_check(board, 2)

#def space_check(board,position):
    #return board[position] == ' '
def full_board_check(board):
    for i in range (1,10):
        if space_check(board,i):##عشان اذا فاضي أي بوزيشن حيطبع فولس حأساس انه في شي بدو لسه تعبئة 
            return False
        
    return True##    الشكل لازم هيك
    
#board=['X','O','O','X',"X",'O','X','O','X']     
#full_board_check(board) 

#def space_check(board,position):
 #   return board[position] == ' '
def player_choice(board):
    position=0#for usxe in while loop
    #position not from 1_9 ,or positio used
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("choose your next position: "))
        if position not in [1,2,3,4,5,6,7,8,9]:
           position=int(input("choose your next position: "))
        if not space_check(board,position):
            print("this position is not availabe, choose another position")            
    
    return position
#board=['X','O',' ','X',"X",'O','X','O','X']  
#player_choice(board)       

def win_check(board, mark):
    return ((board[7]==mark and board[8]==mark and board[9]==mark) or
    (board[4]==mark and board[5]==mark and board[6]==mark) or 
    (board[1]==mark and board[2]==mark and board[3]==mark)or
    (board[7]==mark and board[4]==mark and board[1]==mark) or 
    (board[8]==mark and board[5]==mark and board[2]==mark) or
    (board[9]==mark and board[6]==mark and board[3]==mark) or  
    (board[7]==mark and board[5]==mark and board[3]==mark) or  
    (board[9]==mark and board[5]==mark and board[1]==mark) )##في حال أي حالة موجودة رح يرجع تروو

def replay():
    return input("Do you want to play again? ").lower().startswith('y')   

while True:
    theBoard=[' ']*10 ##the element is repeated 10 times
    player1,player2=select_marker_input()#choose xor o,,the function is with two answers for return
    turn=choose_first()
    print(turn+ " will be the first")
    game=input('Are you ready to play: ')
    if game.lower().startswith('y'):
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn =="player1":
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard, player1, position)#list, marker,position
            if win_check(theBoard,player1):#id player1 win
                display_board(theBoard)
                print("Well done player1")
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("No one win")
                    break
                else:
           
                    turn="player2"
        else:
            display_board(theBoard)
            position=player_choice(theBoard)
            place_marker(theBoard, player2, position)#list, marker,position
            if win_check(theBoard,player2):#id player1 win
                display_board(theBoard)
                print("Well done player2")
                game_on=False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("No one win")
                    break
                else:
                    turn="player1"
    if  not replay():
        break
       
                    
                
    
    