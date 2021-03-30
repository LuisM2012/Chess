from moves_ches import Movement, Pawn, Rook, King, Knight, Queen, Bishop
from pygame import image, transform, draw
import pygame, os, math, time


WIDTH = 800
HEIGHT = 700
PIECE_FRAME = (80,80)

game_board = transform.scale(image.load(os.path.join("Chess Pieces", "CHESS_GAMEBOARD.jpg")), (WIDTH-100, HEIGHT))

blue_rook = transform.scale(image.load(os.path.join("Chess Pieces", "ROOK-BLUE.png")), PIECE_FRAME)
red_rook = transform.scale(image.load(os.path.join("Chess Pieces", "ROOK-RED.png")), PIECE_FRAME)
blue_bishop = transform.scale(image.load(os.path.join("Chess Pieces", "BISHOP-BLUE.png")), PIECE_FRAME)
red_bishop = transform.scale(image.load(os.path.join("Chess Pieces", "BISHOP-RED.png")), PIECE_FRAME)
blue_pawn = transform.scale(image.load(os.path.join("Chess Pieces", "PAWN-BLUE.png")), PIECE_FRAME)
red_pawn = transform.scale(image.load(os.path.join("Chess Pieces", "PAWN-RED.png")), PIECE_FRAME)

blue_knight = transform.scale(image.load(os.path.join("Chess Pieces", "KNIGHT-BLUE.png")), PIECE_FRAME)
red_knight = transform.scale(image.load(os.path.join("Chess Pieces", "KNIGHT-RED.png")), PIECE_FRAME)
blue_queen = transform.scale(image.load(os.path.join("Chess Pieces", "QUEEN-BLUE.png")), PIECE_FRAME)
red_queen = transform.scale(image.load(os.path.join("Chess Pieces", "QUEEN-RED.png")), PIECE_FRAME)
blue_king = transform.scale(image.load(os.path.join("Chess Pieces", "KING-BLUE.png")), PIECE_FRAME)
red_king = transform.scale(image.load(os.path.join("Chess Pieces", "KING-RED.png")), PIECE_FRAME)


class Board:

    board = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]
    
    def __init__(self, window):
        self.window = window
        self.window.blit(game_board, (0,0))

        self.board[1][0] = Pawn(window, red_pawn, self.position(0,1), name="r1_pawn")
        self.board[1][1] = Pawn(window, red_pawn, self.position(1,1), name="r2_pawn")
        self.board[1][2] = Pawn(window, red_pawn, self.position(2,1), name= "r3_pawn")
        self.board[1][3] = Pawn(window, red_pawn, self.position(3,1), name="r4_pawn")
        self.board[1][4] = Pawn(window, red_pawn, self.position(4,1), name="r5_pawn")
        self.board[1][5] = Pawn(window, red_pawn, self.position(5,1), name="r6_pawn")
        self.board[1][6] = Pawn(window, red_pawn, self.position(6,1), name="r7_pawn")
        self.board[1][7] = Pawn(window, red_pawn, self.position(7,1), name="r8_pawn")

        self.board[0][4]= King(window,   red_king, self.position(4,0)   , name="r_king")
        self.board[0][3] = Queen(window, red_queen, self.position(3,0) , name="r_queen")
        self.board[0][2] = Bishop(window,red_bishop, self.position(2,0), name="r1_bishop")
        self.board[0][5] = Bishop(window,red_bishop, self.position(5,0), name="r2_bishop")
        self.board[0][1] = Knight(window,red_knight, self.position(1,0), name="r1_knight")
        self.board[0][6] = Knight(window,red_knight, self.position(6,0), name="r2_knight")
        self.board[0][0] = Rook(window,  red_rook, self.position(0,0)  , name="r1_rook")
        self.board[0][7] = Rook(window,  red_rook, self.position(7,0)  , name="r2_rook")

        self.board[6][0] = Pawn(window, blue_pawn, self.position(0,6), name="b1_pawn")
        self.board[6][1] = Pawn(window, blue_pawn, self.position(1,6), name="b2_pawn")
        self.board[6][2] = Pawn(window, blue_pawn, self.position(2,6), name="b3_pawn")
        self.board[6][3] = Pawn(window, blue_pawn, self.position(3,6), name="b4_pawn")
        self.board[6][4] = Pawn(window, blue_pawn, self.position(4,6), name="b5_pawn")
        self.board[6][5] = Pawn(window, blue_pawn, self.position(5,6), name="b6_pawn")
        self.board[6][6] = Pawn(window, blue_pawn, self.position(6,6), name="b7_pawn")
        self.board[6][7] = Pawn(window, blue_pawn, self.position(7,6), name="b8_pawn")

        self.board[7][4]= King(window,   blue_king, self.position(4,7)   , name="b_king")
        self.board[7][3] = Queen(window, blue_queen, self.position(3,7) , name="b_queen")
        self.board[7][2] = Bishop(window,blue_bishop, self.position(2,7), name="b1_bishop")
        self.board[7][5] = Bishop(window,blue_bishop, self.position(5,7), name="b2_bishop")
        self.board[7][1] = Knight(window,blue_knight, self.position(1,7), name="b1_knight1")
        self.board[7][6] = Knight(window,blue_knight, self.position(6,7), name="b2_knight2")
        self.board[7][7] = Rook(window,  blue_rook, self.position(7,7)  , name="b2_rook")
        self.board[7][0] = Rook(window,  blue_rook, self.position(0,7)  , name="b1_rook")

        self.initiate_movement(self.board)

    def position(self, x, y):
        return ((x*80)+30, (y*80)+30)

    def initiate_movement(self, bo):
        self.moves = Movement(bo)
        self._saved_moves = []
        self.selected_piece = 0

    def board_position(self, x, y):
        row = math.floor((y-30)/80)
        col = math.floor((x-30)/80)
        return col, row

    def selected(self, pos, color):
        x, y = pos
        select = self.valid_selection(pos, color)
        if self._saved_moves != [] and select:
            for i in self._saved_moves:
                if i[0] == x and i[1] == y:
                    c,r = self.selected_piece.get_position()
                    piece_pos = self.board_position(c,r)
                    self.move_piece(piece_pos, i, True)
                    self._saved_moves = []
                    self.selected_piece = 0
                    self.moves.update_board(self.board)
                    bol, mess = self.moves.checkmate(color)
                    if bol:
                        print(mess)
                    return True

        elif not select:
            if self.selected_piece != 0:
                self.remove_dots()
            self.selected_piece = self.board[y][x]
            self._saved_moves = self.moves.moves(self.board[y][x], pos, color) #list of moves
            for move in self._saved_moves:
                draw.circle(self.window,"white", self.dot_pos(move), 10)

        return False
    
    def move_piece(self, piece_pos, new_pos, value):#Ignore value: Used for (bool) if move made
        piece = self.board[piece_pos[1]][piece_pos[0]]
        new_pos_piece = self.board[new_pos[1]][new_pos[0]]
        print("TEST",piece, piece_pos)
        self.board[new_pos[1]][new_pos[0]] = piece
        self.board[piece_pos[1]][piece_pos[0]] = 0
        print("TEST",piece)
        piece.set_position(self.position(new_pos[0],new_pos[1]), value)
        # if new_pos_piece != 0:     ##Could be used to intergrate for showing takes
        #     new_pos_piece.set_position((8,8), value)
        self.remove_dots()

    def remove_dots(self):
        self.window.blit(game_board, (0,0))
        list_nest = self.board
        for list in list_nest:
            for item in list:
                if item != 0:
                    pos = item.get_position()
                    item.set_position(pos, False)
        
    def valid_selection(self, pos, player):
        x,y = pos
        if self.board[y][x] == 0:
            print("Valid Place")
            return True
        elif self.board[y][x].name[0] != player:
            print(self.board[y][x].name)
            return True
        return False
            
    def dot_pos(self, pos):
        x,y = pos
        return ((x*80)+70, (y*80)+70)


class Chess:
    def __init__(self, window, font):
        self._window = window
        self.font = font
        self.main()

    def main(self):
        run = True
        clock = pygame.time.Clock()
        self.set_game()
        self.player_turn = "b"
        self.player1 = 15*60
        self.player2 = 15*60
        self.switch = False

        start = time.time()
        while run:
            clock.tick(10)
            
            if self.switch:
                if self.player_turn == "r":
                    self.player1 -= (time.time()- start)
                else:
                    self.player2 -= (time.time()- start)
                start = time.time()


            time_elapsed = (time.time() - start)
            if self.player_turn == "b":
                player1 = self.player1 - time_elapsed
                player2 = self.player2
            else:
                player2 = self.player2 - time_elapsed
                player1 = self.player1

            self.update_game(player1, player2)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEMOTION:
                    pass
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.onClick(pos)


    def update_game(self, play1, play2):
        self.update_timer(play1, play2)
        if self.switch:
            self.switch = False
        pygame.display.update()
    
    def update_timer(self, player1, player2):
        self.timer((705, 600), player1)
        self.timer((705, 30), player2) 

    def timer(self, position, time_rem):
        draw.rect(self._window, "white", (position[0],position[1],90,70), 0, 13)
        timer_text = self.font.render(("Timer:"), True, "black")
        self._window.blit(timer_text, (position[0]+12,position[1]+10))
        player_time = self.time_display(position, time_rem)
        pygame.display.update()
        return player_time
    
    def time_display(self, position, time_left):
        min = str(int(time_left//60))
        sec = str(int(time_left-(float(min)*60)))
        stringe = f"{min:0>2}:{sec:0>2}".format(min, sec)
        time_display = self.font.render((stringe), True, "black")
        self._window.blit(time_display, (position[0]+12,position[1]+40))
    
    def set_game(self):
        self.game = Board(self._window)
        pygame.display.update()

    def onClick(self, pos):
        col = math.floor((pos[0]-30)/80)
        row = math.floor((pos[1]-30)/80)
        print(col, row)
        if col in (0,1,2,3,4,5,6,7) and row in (0,1,2,3,4,5,6,7) :
            self.switch = self.game.selected((col, row), self.player_turn)
        else:
            self.switch = False
            print("out of board")
            print(self.game.board)
        
        if self.switch:
            self.player_turn = "r" if self.player_turn == "b" else "b"


if __name__ == "__main__":

    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("Somic Sans MS", 30)
    pygame.display.set_caption('CHESS PYGAME')

    main_game = Chess(win, font)