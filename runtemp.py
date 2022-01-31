class Error(Exception):
    """Base class for other exceptions"""
    pass


class ColumnFullError(Error):
    """Raised when the column is full"""
    pass


class Board():
    """
    build the board the game is played on
    """
    def __init__(self,):
        self.board = self.build()
        self.number_turns = 2

    def build(self):
        board_width = 7
        board_height = 6
        self.board = []
        for i in range(board_width - 1):
            self.board.append([])

        for i in range(board_height):  # fill board variable
            for j in range(board_width):
                self.board[i].insert(j, "_")
        return self.board

    def draw_board(self):
        print("")
        print("    0 1 2 3 4 5 6 ")
        print("__________________")
        for i in range(6):
                print(i, "~", end="|")
                for j in range(7):
                        print(self.board[i][j], end="|")
                print("")

    def whose_turn(self):
        if self.number_turns % 2 == 0:
            player_piece = "x"
            player = "Player 1 "
            self.number_turns += 1
        else:
            player = "Player 2"
            player_piece = "0"
            self.number_turns += 1
        return player, player_piece

    def take_move(self, player, player_piece):
        col = 11
        while(col < 0) or(col > 6):
            try:
                col = int(input(f"{player} pick a column to drop an {player_piece}: "))
                                
                if col < 0 or col > 6:
                    raise IndexError("between 1 and 6")
                if self.board[0][col] != "_":
                    col = 11
                    raise ColumnFullError

            except ValueError:
                    print("Enter a NUMBER in range 0-6")
            except ColumnFullError:
                    print("column full")
            except IndexError:
                    print("Enter a NUMBER in range 0-6")
        return col, player_piece

    def insert_piece(self, choice):
        for row in range(5, -1, -1):
            if self.board[row][choice[0]] == "_":
                self.board[row][choice[0]] = choice[1]
                
                break
        return

    def check_draw(self, board):
        strboard = str(board)
        temp = strboard.count("_")
        print(temp)
        if temp > 0:
            return False
        else:
            print("DRAW")
            return True


def play_game():
    game = Board()
    game_over = False

    while not game_over:
        player, player_piece = game.whose_turn()
        choice = game.take_move(player, player_piece)
        game.insert_piece(choice)
        game.draw_board()
        game_over = game.check_draw(game.board)

if __name__ == '__main__':
    play_game()
