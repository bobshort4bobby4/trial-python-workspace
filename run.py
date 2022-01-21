board = [[],[],[],[],[],[],[]]
number_turns = 2
keep_going_eileen = True
col = 10

underl = "_"


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
   
    temp= board[0][col]
    print(temp)
    
    while board[0][col] != "_":
        col = int(input("This column is full. Please choose again: "))

    return col
   


def take_input_from_player():
    global number_turns
    global col 
    col = 10
    going = True
    if number_turns % 2 == 0:
        player_piece = "x"
        player = "Player 1 "
    else:
        player = "Player 2"
        player_piece = "0"

    while (col < 0) or (col > 6):
        try:
            col = int(input(f"{player} pick a column to drop an {player_piece} : "))
        except ValueError:
            print("Enetr a number in range 0-6")




    # while going:
    #     if col in range(0, 7):
    #         print("Valid column thanks very much you're very kind")
    #         going = False
    #     else:
    #         print("NOT IN RANGE")
    #         try:
    #             col = int(input(f"{player} pick a column to drop an {player_piece} :"))
    #         except ValueError:
    #             print("Enetr a NUMBER in range 0-6")
        
            
    choice = check_column_full(col)
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




while keep_going_eileen:
    take_input_from_player()
    draw_board(board)
    check_draw(board)
    # check_for_quit()




