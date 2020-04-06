#tic tac toe implementation in python feel free to use 
# wherever

board = [ 0 , 0 , 0, 0 , 0 , 0, 0 , 0 , 0]


#def AI(board):
        #take the board state, and calculate the
        #best probable move

        


def is_Draw(board):
    found  = None
    for index in range(0, 8):
        if board[index] == 0:
            found  = True
    if found == True:
        return False
    else:
        return True    

def is_Win(board):
    win_c1 = 'XXX'
    win_c2 = 'KKK'
    won = False
    res  = str(board[0]) + str(board[1]) + str(board[2])
    res_1  = str(board[3]) + str(board[4]) + str(board[5])
    res_2  = str(board[6]) + str(board[7]) + str(board[8])

    ver = str(board[0]) + str(board[3]) + str(board[6])
    ver_1 = str(board[1]) + str(board[4]) + str(board[7])
    ver_2 = str(board[2]) + str(board[5]) + str(board[8])
               
    edge = str(board[0]) + str(board[5]) + str(board[8])
    edge2 = str(board[2]) + str(board[5]) + str(board[6])
    
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
            P = int(input("Enter your move : "))
            if P > 9:
                print("Out of Bounds")
            else:
               

                if(board[P] == 0):
                    board[P] = 'X'
                elif(board[P] == 'K'):
                    print("Your opponent has put a move there")
        
                else:
                    print( "You have already put a value for this square")

                if(is_Draw(board) == True):
                       print("Game Over It's a draw")
                       break 
                    
                print_board(board)
                if(is_Win(board) == True):
                      print("X has won")
                      break
                    
            
            P = int(input("Enter your move : "))
            if P > 9:
                print("Out of Bounds")
            else:           
                if(board[P] == 0):
                    board[P] = 'K'
                elif(board[P] == 'X'):
                    print("Your opponent has put a move there")
                else:
                    print( " You have already put a value for this square")


                if(is_Draw(board) == True):
                    print("Game Over It's a Draw")
                    break
                    
                    
                print_board(board)
                if(is_Win(board) == True):
                    print("O has won")
                    break



def print_board(board):
    print ( "| " + str(board [0 ]) + "|" +  str(board[1]) + "|" + str(board[2])+"\n"
            "| " + str(board [3 ]) + "|" +  str(board[4]) + "|" + str(board[5])+"\n"
             "| " + str(board [6]) + "|" +  str(board[7]) + "|" + str(board[8]))

    
play()

