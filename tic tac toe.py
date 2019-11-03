#tic tac toe
# Finish implent Game AI 

board = [ [ 0 , 0 , 0],
            [ 0 , 0 , 0],
            [ 0 , 0 , 0]]

def is_Draw(board):
	found = False

	for index in range(0, 2):
		for index_b in range(0, 2):
			if 0 == board[index][index_b]:
				found = True
	if found == True:
		return False
	else:
		return True

def is_Win(board):
    win_c1 = 'XXX'
    win_c2 = 'KKK'
    won = False
    res  = str(board[0][0]) + str(board[0][1]) + str(board[0][2])
    res_1  = str(board[1][0]) + str(board[1][1]) + str(board[1][2])
    res_2  = str(board[2][0]) + str(board[2][1]) + str(board[2][2])

    ver = str(board[0][0]) + str(board[1][0]) + str(board[2][0])
    ver_1 = str(board[0][1]) + str(board[1][1]) + str(board[2][1])
    ver_2 = str(board[0][2]) + str(board[1][2]) + str(board[2][2])
               
    edge = str(board[0][0]) + str(board[1][1]) + str(board[2][2])
    edge2 = str(board[0][2]) + str(board[1][1]) + str(board[2][0])
    
    if res == win_c1:
        won = True
        
    if res == win_c2:
        won = True

    if res_1 == win_c1:
        won = True
        
    if res_1 == win_c2:
        won = True
        
    if res_2 == win_c1:
        won = True
        
    if res_2 == win_c2:
        won = True
        
    if ver == win_c1:
        won = True
        
    if ver == win_c2:
        won = True
        
    if ver_1 == win_c1:
        won = True
        
    if ver_1 == win_c2:
        won = True
        
    if ver_2 == win_c1:
        won = True
    if ver_2 == win_c2:
        won = True
    if edge == win_c1:
        won = True
    if edge == win_c2:
        won = True
    if edge2 == win_c1:
        won = True
    if edge2 == win_c2:
        won = True
    return won
        
def play():
    X = True
    O  = False
    i = 0
    j = 0
    A = input("X or O :")
    while(True):
        if (A == 'X'):
            P = input("Enter your move : ")
            if int(P) > 9:
                print("Out of Bounds")
            else:
                #n % 3 
                res = int(P) % 3
                if (res == 0) | (int(P) < 4):
                    i = 0
                    j = int(P) - 1
                    if( int(P) == 1):
                        i = 0
                        j = 0
                    if (int(P) == 2):
                        i = 0
                        j = 1
                    if( int(P) == 6):
                        i = 1
                        j = 2
                    if( int(P) == 9):
                        i = 2
                        j = 2
                elif (res == 0) | (int(P) < 7):
                    i = 1
                    j = int(P) - 4
                elif ( res == 0) | (int(P) >= 7) | (int(P) == 9):
                    i = 2
                    j = int(P) - 7

            if(board[i][j] == 0):
                board[i][j] = 'X'
            elif(board[i][j] == 'K'):
                print("Your opponent has put a move there")
        
            else:
                print( "You have already put a value for this square")

            if(is_Draw(board) == True):
                print("Game Over")
                break 
            
            print_board(board)
            if(is_Win(board) == True):
                print("X has won")
                break
            
            
            P = input("Enter your move : ")
            if int(P) > 9:
                print("Out of Bounds")
            else:
                #n % 3 
                res = int(P) % 3
                if (res == 0) | (int(P) < 4):
                    i = 0
                    j = int(P) - 1
                if( int(P) == 6):
                    i = 1
                    j = 2
                if( int(P) == 9):
                    i = 2
                    j = 2
                if(int(P) == 1):
                    i = 0
                    j = 0
                if (int(P) == 2):
                    i = 0
                    j = 1
                elif (res == 0) | (int(P) < 7):
                    i = 1
                    j = int(P) - 4
                elif ( res == 0) | (int(P) >= 7) | (int(P) == 9):
                    i = 2
                    j = int(P) - 7
            
            if(board[i][j] == 0):
                board[i][j] = 'K'
            elif(board[i][j] == 'X'):
                print("Your opponent has put a move there")
            else:
                print( " You have already put a value for this square")


            if(is_Draw(board) == True):
                print("Game Over")
                break
            
            
            print_board(board)
            if(is_Win(board) == True):
                print("O has won")
                break



def print_board(board):
    print ( "| " + str(board [0 ][0]) + "|" +  str(board[0][1]) + "|" + str(board[0][2])+"\n"
            "| " + str(board [1 ][0]) + "|" +  str(board[1][1]) + "|" + str(board[1][2])+"\n"
             "| " + str(board [2 ][0]) + "|" +  str(board[2][1]) + "|" + str(board[2][2]))

    
play()
