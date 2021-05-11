class Piece():
    def __init__(self, position, player, image=None, **kwargs): #will need to imput name, and player in kwargs
        self.moves_made = 0
        self.set_image(image)
        self.set_position(position, False)
        self.set_info(kwargs)
        self.player = player

    def set_position(self, position: (int, int), moved: bool = True):
        self._position = position
        #Used to keep track of moves made
        if moved: 
            self.moved()

    def get_position(self):
        return self._position
    
    def set_image(self, image):
        self.image = image

    def set_info(self, info):
        if "name" in info:
            self.name = info["name"]
        else:
            self.name = None
    
    def moved(self):
        self.moves_made +=1

    def check_mate(self, board):
        king_moves = []
        players_move =[]
        for j in board:
            for i in j:
                if i!=0 and i.name=="K" and i.player==self.player:
                    king_moves.append(i.get_position())
                    king_moves += i.get_moves(board)
                if i!=0 and i.player !=self.player:
                    players_move += i.get_moves(board)
        print(f"other:{players_move}")
        print(f"king:{king_moves}")
        return

    def invert_moves(self, moves):
        r_move = []
        for item in moves:
            r_move.append((7-item[0], 7-item[1]))

        return r_move

    ##Extras
    def get_straight(self, board):
        position = self._position
        moves = []
        u,d,l,r = (True, True, True, True)

        for i in range(1,8):
            if u and (0<=position[1]+i<=7) and (0<=position[0]<=7):#+row
                if board[position[1]+i][position[0]] != 0:
                    u = False
                moves.append((position[0], position[1]+i)) if board[position[1]+i][position[0]]==0 or board[position[1]+i][position[0]].player!=self.player else None
            if d and (0<=position[1]-i<=7) and (0<=position[0]<=7):#-row
                if board[position[1]-i][position[0]] != 0:
                    d = False
                moves.append((position[0], position[1]-i)) if board[position[1]-i][position[0]]==0 or board[position[1]-i][position[0]].player!=self.player else None
            if l and (0<=position[1]<=7) and (0<=position[0]-i<=7):#-col
                if board[position[1]][position[0]-i] != 0:
                    l = False
                moves.append((position[0]-i, position[1])) if board[position[1]][position[0]-i]==0 or board[position[1]][position[0]-i].player!=self.player else None
            if r and (0<=position[1]<=7) and (0<=position[0]+i<=7):#+col
                if board[position[1]][position[0]+i] != 0:
                    r = False
                moves.append((position[0]+i, position[1])) if board[position[1]][position[0]+i]==0 or board[position[1]][position[0]+i].player!=self.player else None

        return moves

    def get_diagnol(self, board):
        position = self._position
        moves = []
        u,d,l,r = (True, True, True, True)

        for i in range(1,8):
            if u and (0<=position[1]+i<=7) and (0<=position[0]+i<=7):#+row +col
                if board[position[1]+i][position[0]+i] != 0:
                    u = False
                moves.append((position[0]+i, position[1]+i)) if board[position[1]+i][position[0]+i]==0 or board[position[1]+i][position[0]+i].player!=self.player else None
            if d and (0<=position[1]-i<=7) and (0<=position[0]-i<=7):#-row -col
                if board[position[1]-i][position[0]-i] != 0:
                    d = False
                moves.append((position[0]-i, position[1]-i)) if board[position[1]-i][position[0]-i]==0 or board[position[1]-i][position[0]-i].player!=self.player else None
            if l and (0<=position[1]+i<=7) and (0<=position[0]-i<=7):#+row -col
                if board[position[1]+i][position[0]-i] != 0:
                    l = False
                moves.append((position[0]-i, position[1]+i)) if board[position[1]+i][position[0]-i]==0 or board[position[1]+i][position[0]-i].player!=self.player else None
            if r and (0<=position[1]-i<=7) and (0<=position[0]+i<=7):#-row +col
                if board[position[1]-i][position[0]+i] != 0:
                    r = False
                moves.append((position[0]+i, position[1]-i)) if board[position[1]-i][position[0]+i]==0 or board[position[1]-i][position[0]+i].player!=self.player else None

        return moves

    def __str__(self):
        return self.name if self.name != None else self.player

    def __getitem__(self, index): #returns x or y for 0 or 1, respectively
        if type(index) is int and index in [0,1]: return self._position[index]
        else: return None


class Rook(Piece):#Needs Castling

    def get_moves(self, board):
        return self.get_straight(board)
 
class Queen(Piece):#Finished

    def get_moves(self, board):
        move_d = self.get_diagnol(board)
        move_s = self.get_straight(board)

        return move_d+move_s

class King(Piece):#Needs Castling and Check Mating Prevention

    def get_moves(self, board):
        position = self._position
        moves = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0<=position[0]+i<=7 and 0<=position[1]+j<=7:
                    moves.append((position[0]+i, position[1]+j)) if board[position[1]+j][position[0]+i]==0 or board[position[1]+j][position[0]+i].player!=self.player else None

        return moves

 
class Bishop(Piece): #Finished

    def get_moves(self, board):
        return self.get_diagnol(board)

class Pawn(Piece):#Stil needs work + en passant

    def get_moves(self, board):
        position = self._position
        moves = []

        term = -1 if self.player==1 else 1
        moves.append((position[0],position[1]+(term*1))) if 0<=position[1]+(term*1)<=7 and 0<=position[0]<=7 and (board[position[1]+(term*1)][position[0]]==0) else None

        for i in [-1,1]: #takes
            if (0<=position[0]+i<=7 and 0<=position[1]+(term*1)<=7) and (board[position[1]+(term*1)][position[0]+i]!=0 and board[position[1]+(term*1)][position[0]+i].player!=self.player):
                    moves.append((position[0]+i, position[1]+(term*1)))

        if self.moves_made == 0: #leap for first turn
            if 0<=position[0]<=7 and 0<=position[1]+(term*2)<=7 and board[position[1]+(term*1)][position[0]]==0:
                moves.append((position[0],position[1]+(term*2))) if board[position[1]+(term*2)][position[0]]==0 else None

        # self.check_mate(board) causes recurion
        return moves


class Knight(Piece):#Finished

    def get_moves(self, board):
        position = self._position
        moves = []
        moves.append((position[0]+1, position[1]+2)) if 0<=position[0]+1<=7 and 0<=position[1]+2<=7 and (board[position[1]+2][position[0]+1] == 0 or board[position[1]+2][position[0]+1].player != self.player) else None
        moves.append((position[0]-1, position[1]+2)) if 0<=position[0]-1<=7 and 0<=position[1]+2<=7 and (board[position[1]+2][position[0]-1] == 0 or board[position[1]+2][position[0]-1].player != self.player) else None
        moves.append((position[0]+2, position[1]+1)) if 0<=position[0]+2<=7 and 0<=position[1]+1<=7 and (board[position[1]+1][position[0]+2] == 0 or board[position[1]+1][position[0]+2].player != self.player) else None
        moves.append((position[0]-2, position[1]+1)) if 0<=position[0]-2<=7 and 0<=position[1]+1<=7 and (board[position[1]+1][position[0]-2] == 0 or board[position[1]+1][position[0]-2].player != self.player) else None
        moves.append((position[0]-2, position[1]-1)) if 0<=position[0]-2<=7 and 0<=position[1]-1<=7 and (board[position[1]-1][position[0]-2] == 0 or board[position[1]-1][position[0]-2].player != self.player) else None
        moves.append((position[0]+2, position[1]-1)) if 0<=position[0]+2<=7 and 0<=position[1]-1<=7 and (board[position[1]-1][position[0]+2] == 0 or board[position[1]-1][position[0]+2].player != self.player) else None
        moves.append((position[0]+1, position[1]-2)) if 0<=position[0]+1<=7 and 0<=position[1]-2<=7 and (board[position[1]-2][position[0]+1] == 0 or board[position[1]-2][position[0]+1].player != self.player) else None
        moves.append((position[0]-1, position[1]-2)) if 0<=position[0]-1<=7 and 0<=position[1]-2<=7 and (board[position[1]-2][position[0]-1] == 0 or board[position[1]-2][position[0]-1].player != self.player) else None

        return moves
