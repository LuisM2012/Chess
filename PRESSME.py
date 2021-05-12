from pieces import Pawn, Rook, King, Knight, Queen, Bishop
from pygame import image, transform, draw
from chess_client import Connection
import pygame, os, math, time


WIDTH = 800 #window width
HEIGHT = 700 #window height
PIECE_FRAME = (80,80)  #piece width and height

#game board image and pieces images for respective color and type
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

"""
Chess class uses Board class to implement movement
"""
class Chess: #game set-up is here / managers turns, time, and window display
    
    def __init__(self, window, font):
        self._window = window
        self.font = font
        self.player1 = 1
        self.player2 = 2
        self._reset()
        self.main()

    ###Manage initial board variables and pieces.
    def _reset_board(self):
        """Reset the board to 0s and set up new pieces."""
        self.board = [[0 for i in range(8)] for _ in range (8)]

        for i in range(8):
            self.board[1][i] = Pawn((i,1), self.player2, image= red_pawn, name="P")

        self.board[0][4] = King((4,0),     self.player2, image= red_king, name="K")
        self.board[0][3] = Queen((3,0),    self.player2, image= red_queen, name="Q")
        self.board[0][2] = Bishop((2,0),   self.player2, image= red_bishop, name="B")
        self.board[0][5] = Bishop((5,0),   self.player2, image= red_bishop, name="B")
        self.board[0][1] = Knight((1,0),   self.player2, image= red_knight, name="N")
        self.board[0][6] = Knight((6,0),   self.player2, image= red_knight, name="N")
        self.board[0][0] = Rook((0,0),     self.player2, image= red_rook, name="R")
        self.board[0][7] = Rook((7,0),     self.player2, image= red_rook, name="R")

        for i in range(8):
            self.board[6][i] = Pawn((i,6), self.player1, image= blue_pawn, name="P")

        self.board[7][4] = King((4,7),   self.player1, image=blue_king, name="K")
        self.board[7][3] = Queen((3,7),  self.player1, image=blue_queen, name="Q")
        self.board[7][2] = Bishop((2,7), self.player1, image=blue_bishop, name="B")
        self.board[7][5] = Bishop((5,7), self.player1, image=blue_bishop, name="B")
        self.board[7][1] = Knight((1,7), self.player1, image=blue_knight, name="N")
        self.board[7][6] = Knight((6,7), self.player1, image=blue_knight, name="N")
        self.board[7][7] = Rook((7,7),   self.player1, image=blue_rook, name="R")
        self.board[7][0] = Rook((0,7),   self.player1, image=blue_rook, name="R")

    def _reset(self):
        """Reset entire board"""
        self._reset_board()             #reset board
        self.time2 = 40                #player 2 time
        self.time1 = 41                #player 1 time
        self.timer = 0                  #for tracking time passed for each player
        self.clicked = None             #for tracking clicks
        self.current = 1             #to track current player     
        self.switch = False             #track if players switched
        self.in_menu = True             #to track screen to show
        self.online = False             #online or offline
        self.end = False
        self.moves = []                 


    def online_base(self):  #uncomment below to play online
        """Connect to server and reset players and screen for online match."""
        # self.connection = Connection()            
        self.screen = 1#self.connection.listen()
        self.online = True

    def manage_screens(self):
        """Invert board if screen is reversed"""                     
        self.t_pos = (30, 600)          #for setting position of time
        if self.screen == 2:            #to switch view
            self.invert_e()  
            self.t_pos = (600, 30)                  

    #manage game
    def manage_win(self, time):
        """Report win and loss from out of time or checkmate."""
        if time <= 0: #out of time
            self.end = 1 if self.current==2 else 2    
            if self.online: self.connection.send('QUIT')     

    def listen_for(self): #uncomment below to play online
        # move = self.connection.listen() #WILL return QUIT or ((2,2),(1,1))
        # if move != 'QUIT':
        #     old = (7-move[0][0], 7-move[0][1])  #piece position
        #     new = (7-move[1][0], 7-move[1][1])  #new position
        #     self.board[new[1]][new[0]] = self.board[old[1]][old[0]]
        #     self.board[old[1]][old[0]] = 0
        # else:
        #     self.end = 2 if self.screen==2 else 1
        pass

    def send_to(self, piece: (int,int), new: (int,int) ): #uncomment below to play online
        # self.connection.send(str((piece, new)))
        pass

    def check_mate(self, board): #still in production
        """Check if current player is checkmated."""
        king_moves = []
        players_move =[]
        for j in board:
            for i in j:
                if i!=0 and i.name=="K" and i.player==self.current:
                    king_moves += i.get_moves(board, True if ) + i._position
                if i!=0 and i.player!=self.current:
                    players_move += i.get_moves(board, True)
        print(f"other:{players_move}")
        print(f"king:{king_moves}")
        # return

    ### Change board
    def invert_e(self):
        """Invert both the board and the position of pieces. Works only with unison of pieces module."""
        self.board = [row[::-1] for row in self.board[::-1]]
        for row in self.board:
            y = self.board.index(row)
            for piece in row:
                x = row.index(piece)
                piece.set_position((x, y), False) if piece!=0 else None

    ### Display in Screen
    def _draw(self):
        """Draw out the window with the game board, pieces, and time."""
        if self.end:
            self.end_screen(self.end)
        elif not self.in_menu:
            self._window.fill("black")
            self._window.blit(game_board, (0,0))

            for i in self.board:
                for p in i:
                        self._window.blit(p.image, self.position(p[0], p[1])) if p!=0 and p.image is not None else None

            for b in self.moves: ##draw possible moves
                draw.circle(self._window, "white", self.position(b[0], b[1], 40), 8) 

            pygame.draw.rect(self._window, "white", (705, 30,90,70), 0, 13)
            pygame.draw.rect(self._window, "white", (705, 600,90,70), 0, 13)

            time1 = (self.time1-self.timer) if self.current==1 else self.time1
            time2 = (self.time2-self.timer) if self.current==2 else self.time2
            if not self.online: self.manage_win(time2)
            self.manage_win(time1) if self.screen==1 else self.manage_win(time2)

            mins = str(int(time2//60))
            secs = str(int(time2-(float(mins)*60)))
            stringe = f"   {mins}:{secs:0>2}" if time2>0 else "TIME UP"
            color1 = "black" if time2>30 else "red"
            time_display = self.font.render((stringe), True, color1)
            self._window.blit(time_display, (710,self.t_pos[0]+25))
            p2 = self.font.render(("PLAYER 2"), True, "white")
            self._window.blit(p2, (702,self.t_pos[0]-20))
            
            mins = str(int(time1//60))
            secs = str(int(time1-(float(mins)*60)))
            stringe = f"   {mins}:{secs:0>2}" if time1>0 else "TIME UP"
            color2 = "black" if time1>30 else "red"
            time_display = self.font.render((stringe), True, color2)
            self._window.blit(time_display, (710,self.t_pos[1]+25))
            p1 = self.font.render(("PLAYER 1"), True, "white")
            self._window.blit(p1, (702,self.t_pos[1]-20))
        else:
            self.menu_screen()
        
        pygame.display.update()

    def menu_screen(self):
        """Display menu screen."""
        self._window.fill("gray")
        draw.rect(self._window, "blue", (305, 300,80,40), 0, 13)
        draw.rect(self._window, "green", (305, 375,80,40), 0, 13)
        multi = self.font.render(("Online"), True, "white")
        off = self.font.render(("Offline"), True, "white")
        self._window.blit(multi, (310, 310))
        self._window.blit(off, (310, 390))
    
    def end_screen(self, results): #tip: for rect pygame uses (x1,y1,x2,y2) such as (0,0,width, height)
        """Display end screen."""
        self._window.fill("red")
        self._window.fill("green", (0,0,WIDTH, HEIGHT//2) if results!=self.screen else (0,HEIGHT//2, WIDTH, HEIGHT))
        draw.rect(self._window, "blue", (320,320, 160,60), 0, 13)
        self.font = pygame.font.SysFont("Comic Sans", 60)
        multi = self.font.render(("Next"), True, "white")
        self._window.blit(multi, (355, 330))

        side = (200, 500) if results!=self.screen else (500,200)
        multi = self.font.render(("Winner"), True, "white")
        self._window.blit(multi, (340, side[0]))
        multi = self.font.render(("Loser"), True, "white")
        self._window.blit(multi, (350, side[1]))

        self.font = pygame.font.SysFont("Somic Sans MS", 30)

    ### Manage movement, clicks, pieces
    def position(self, x, y, plus=0): #conversion function board position to window position
        """Return board position to window position."""
        return ((x*80)+30+plus, (y*80)+30+plus)

    def onClick(self, pos): #monitors players moves
        """Manage click on board (assuming there's no buttons and only the board)."""
        # if self.online:                               #uncomment for online
        #     if self.current != self.screen: return    #uncomment for online
        col = ((pos[0]-30)//80)         #for easiness with x value
        row = ((pos[1]-30)//80)         #for easiness with y value
        
        if col in (0,1,2,3,4,5,6,7) and row in (0,1,2,3,4,5,6,7): #check if its in board | select movement if True
            self.movement((col, row))

    def movement(self, pos):
        """Manage click on board spots."""
        if self.moves!=[] and pos in self.moves:    #check if piece should be moved | if True move piece with self.move
            self.move(pos)
        else:                   #else get board spot clicked and get moves if not 0 and piece is current player's piece
            self.clicked = pos  #get board spot clicked
            print(self.board[pos[1]][pos[0]])
            if self.current != self.screen:         #if different screen from current, must get moves from reciprocated board
                self.moves = self.board[pos[1]][pos[0]].get_moves(self.board, True) if self.board[pos[1]][pos[0]]!=0 and self.board[pos[1]][pos[0]].player==self.current else []
            else:                                   #else get from normal board
                self.moves = self.board[pos[1]][pos[0]].get_moves(self.board) if self.board[pos[1]][pos[0]]!=0 and self.board[pos[1]][pos[0]].player==self.current else []
        print(self.moves)
        
    def move(self, new_pos):
        """Move piece to new position and set old position as 0."""
        pos = self.clicked          #use for easiness when setting positions
        self.board[pos[1]][pos[0]].set_position(new_pos)                    #set position to new position (for drawing)
        self.board[new_pos[1]][new_pos[0]] = self.board[pos[1]][pos[0]]     #set piece to new board position (for self.board)
        self.board[pos[1]][pos[0]] = 0                                      #set old position as 0
        self.switch = True          #switch players
        self.moves = []             #reset moves for next player
        if self.online: self.send_to(pos, new_pos)          #used for online

    ### Main set-up / time and player monitor
    def main(self): 
        run = True
        clock = pygame.time.Clock()

        start = 0
        while run:
            clock.tick(10)

            if self.switch:
                self.time1 = self.time1-self.timer if self.current==1 else self.time1 
                self.time2 = self.time2-self.timer if self.current==2 else self.time2 
                self.current = 1 if self.current == 2 else 2

                start = time.time()
                self.switch = False

            self.timer = (time.time() - start) if start != 0 else 0
            self._draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if self.in_menu: 
                        if 305<=pos[0]<=385 and 300<=pos[1]<=340: #ONLINE button pressed
                            self.online_base()
                            self.in_menu = False
                            start = time.time()
                            self.manage_screens()
                        if 305<=pos[0]<=385 and 375<=pos[1]<=415: #OFFLINE button pressed
                            self.in_menu = False
                            self.screen = 1                 #to set up view
                            start = time.time()
                            self.manage_screens()
                    elif self.end:
                        if 320<=pos[0]<=480 and 320<=pos[1]<=380: #NEXT button is pressed
                            self.end = False
                            self._reset()
                    else:
                        self.onClick(pos)


if __name__ == "__main__":
    ###initializes pygame window with Title, Font, and Display Size
    pygame.init()
    win = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.SysFont("Somic Sans MS", 30)
    pygame.display.set_caption('CHESS PYGAME')
    ###initializes game
    main_game = Chess(win, font)
