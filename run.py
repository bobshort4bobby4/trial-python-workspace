board = [[],[],[],[],[],[],[]]
number_turns = 2
keep_going_eileen = True
col = 10
player_piece = "x"
underl = "_"
choice = []
temp1 =True

class Error(Exception):
    """Base class for other exceptions"""
    pass


class ColumnFullError(Error):
    """Raised when the input value is too small"""
    pass


for i in range(6): # fill board variable
    for j in range(7):
        board[i].insert(j,"_")

print("Player 1 is x, Player 2  is 0")
print(board.count("_"))
def draw_board(board):        
        print("")
        print("    0 1 2 3 4 5 6 ")
        print("__________________")
        for i in range(6):
                print(i, "~", end="|")
                for j in range(7):
                        print(board[i][j], end="|")
                print("")


def check_column_full(col):
    global temp1
    temp1 = True
    temp= board[0][col]
    print(temp)
    
    while board[0][col] != "_":
        temp1 = False
        print("This column is full. Please choose again: ")
           
           
    return col ,temp1
   


def take_input_from_player():
    global number_turns
    global col 
    global player_piece
    global temp1
    
    col = 10
    going = True
    if number_turns % 2 == 0:
        player_piece = "x"
        player = "Player 1 "
    else:
        player = "Player 2"
        player_piece = "0"

    while (col < 0) or (col > 6) :
        try:
            col = int(input(f"{player} pick a column to drop an {player_piece} : "))
            if board[0][col] != "_":
                raise ColumnFullError
        except ValueError:
            print("Enter a NUMBER in range 0-6")
        except ColumnFullError:
            print("column full")
    
    # if board[0][col] != "_":
    #    raise Exception("column full")
        
        
        
    choice = col
            
   
    for row in range(5, -1, -1):
        if board[row][choice] == "_":
                board[row][choice] = player_piece
                number_turns +=1
                break
                
        #else:
        #    print("That column is full, Pick another")
          #  take_input_from_player()
    
def check_for_quit():
    flag = input("enter y to quit").lower()
    if flag == "y":
        keep_going_eileen = False

draw_board(board)

def check_draw(board):
    strboard = str(board)
    temp = strboard.count("_")
    print(temp)
    if temp > 0:
        return
    else:
        declare_draw()

def declare_draw():
    print("Neither of you were good enough to win") 
    exit()


def check_win(piece):
    print("in checkwin  function piece is ", piece)
    # check rows for line of 4
    temp  = 0
    for i in range(6): 
        for j in range(4):
            if board[i][j] == piece and board[i][j+1] == piece and board[i][j+2] == piece and board[i][j+3] == piece:
                print(f"{piece} has won!")
                exit()

    # check column for line of 4

    for i in range(7):
        for j in range(3):
            if board[j][i] == piece and board[j + 1][i] == piece and board[j + 2][i] == piece and board[j + 3][i] == piece:
                print(f"{piece} has won!")
                exit()

    # check forwards  diagonals for line of 4
   
    for i in range(3,6):
        for j in range(0,4):
            if board[i][j] == piece and board[i-1][j+1] == piece and board[i-2][j+2] == piece and board[i-3][j+3] == piece:
                print(f"{piece} has won!")
                exit()


    # check backwards diagonals for line of 4 

    for i in range(3,6):
        for j in range(6,2,-1):
            if board[i][j] == piece and board[i-1][j-1] == piece and board[i-2][j-2] == piece and board[i-3][j-3] == piece:
                print(f"{piece} has won!")
                exit()



while keep_going_eileen:
    take_input_from_player()
    draw_board(board)
    check_draw(board)
    check_win(player_piece)
    # check_for_quit()




