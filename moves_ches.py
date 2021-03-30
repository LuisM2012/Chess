import pygame


class Movement:
    def __init__(self, board):
        self._board = board
    
    def update_board(self, board):
        self._board = board

    def moves(self, piece, pos, player):
        info = piece.name.split("_")
        color = info[0][0]
        x, y = pos
        if color == player and player == "b":            
            moves = piece.get_moves((7-x, 7-y), self.invert_board(self._board))
            move_list = self.invert_moves(moves)
        elif color == player:
            move_list = piece.get_moves(pos, self._board)
        else:
            return []

        return self.validate(piece, move_list, player)

    def invert_board(self,board):
        _board = board.copy()
        inverted = []
        for i in reversed(_board):
            a=[]
            for j in reversed(i):
                a.append(j)
            inverted.append(a)

        return inverted

    def invert_moves(self, moves):
        r_move = []
        for item in moves:
            r_move.append((7-item[0], 7-item[1]))

        return r_move
    
    def validate(self, piece, moves, color):
        valid = []

        for move in moves:
            x,y = move
            if self._board[y][x] != 0:
                if self._board[y][x].name[0] != color:
                    valid.append(move)
            else:
                valid.append(move)

        return valid

    def checkmate(self, player):##UNFInished
        moves = []
        pos = ()
        king = []
        for row in self._board:
            for col in row:
                if row[col] != 0:
                    if row[col].name[0] == "b":
                        moves =+ row[col].get_moves((col, row), self.invert_board(self._board))
                    else:
                        moves =+ self._board[row][col].get_moves((col, row), self._board)
                    
                    if self._board[row][col].name == player+"_king":
                        pos = (col, row)

        for move in moves:
            if move == pos and king == []:
                return True, "WINNER"
            elif move == pos:
                return True, "MATE"
        return False, "NO MATE"


class Piece():
    def __init__(self, window, image, position, **kwargs) -> None:
        self._window = window
        self.moves_made = 0
        self.set_image(image)
        self.set_position(position, False)
        self.set_name(kwargs)

    def set_position(self, position, moved):#moved:T/F
        self._position = position
        self._window.blit(self._image, position)
        pygame.display.update()
        if moved:
            self.moved()

    def get_position(self):
        return self._position
    
    def set_image(self, piece):
        self._image = piece

    def set_name(self, moves):
        self.name = moves["name"]
    
    def moved(self):
        self.moves_made +=1

    ##Extras
    def get_straight(self, position, board):
        moves = []
        u = True
        d = True
        l = True
        r = True
        for i in range(1,8):
            if u and (0<=position[1]+i<=7) and (0<=position[0]<=7):#up
                if board[position[1]+i][position[0]] != 0:
                    u = False
                moves.append((position[0], position[1]+i))
            if d and (0<=position[1]-i<=7) and (0<=position[0]<=7):
                if board[position[1]-i][position[0]] != 0:
                    d = False
                moves.append((position[0], position[1]-i)) #down 
            if l and (0<=position[1]<=7) and (0<=position[0]-i<=7):
                if board[position[1]][position[0]-i] != 0:
                    l = False
                moves.append((position[0]-i, position[1])) #left
            if r and (0<=position[1]<=7) and (0<=position[0]+i<=7):
                if board[position[1]][position[0]+i] != 0:
                    r = False
                moves.append((position[0]+i, position[1])) #right

        return moves

    def get_diagnol(self, position, board):
        moves = []
        u = True
        d = True
        l = True
        r = True
        for i in range(1,8):
            if u and (0<=position[1]+i<=7) and (0<=position[0]+i<=7):
                if board[position[1]+i][position[0]+i] != 0:
                    u = False
                moves.append((position[0]+i, position[1]+i))
            if d and (0<=position[1]-i<=7) and (0<=position[0]-i<=7):
                if board[position[1]-i][position[0]-i] != 0:
                    d = False
                moves.append((position[0]-i, position[1]-i)) #down 
            if l and (0<=position[1]+i<=7) and (0<=position[0]-i<=7):
                if board[position[1]+i][position[0]-i] != 0:
                    l = False
                moves.append((position[0]-i, position[1]+i)) #left
            if r and (0<=position[1]-i<=7) and (0<=position[0]+i<=7):
                if board[position[1]-i][position[0]+i] != 0:
                    r = False
                moves.append((position[0]+i, position[1]-i)) #right

        return moves


class Rook(Piece):#Still needs debug
    def __init__(self, window, image, position, **kwargs) -> None:
        super().__init__(window, image, position, **kwargs)

    def get_moves(self, position, board):
        return super().get_straight(position, board)
 
class Queen(Piece):#Still needs debug
    def __init__(self, window, image, position, **kwargs) -> None:
        super().__init__(window, image, position, **kwargs)

    def get_moves(self, position, board):
        move_d = super().get_diagnol(position, board)
        move_s = super().get_straight(position, board)

        moves = move_d+move_s
        return moves


class King(Piece):#Still needs valid
    def __init__(self, window, image, position, **kwargs) -> None:
        super().__init__(window, image, position, **kwargs)

    def get_moves(self, position, board):
        moves = []
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if 0<=position[0]+i<=7 and 0<=position[1]+j<=7:
                    moves.append((position[0]+i, position[1]+j))

        return moves

 
class Bishop(Piece): #Still need debug
    def __init__(self, window, image, position, **kwargs) -> None:
        super().__init__(window, image, position, **kwargs)

    def get_moves(self, position, board):
        return super().get_diagnol(position, board)

class Pawn(Piece):#Stil needs work
    def __init__(self, window, image, position, **kwargs) -> None:
        super().__init__(window, image, position, **kwargs)

    def get_moves(self, position, board):
        if self.moves_made == 0:
            moves = [(position[0],position[1]+1),(position[0],position[1]+2)]
        else:
            moves = [(position[0],position[1]+1)]
        move = []
        for item in moves:##Side takes
            for i in [-1,1]:
                if (0<=item[0]+i<=7 and 0<=item[1]<=7) and (board[item[1]][item[0]+i] != 0):
                    if board[item[1]][item[0]+i].name[0] != self.name[0]:
                        move.append((item[0]+i, item[1]))

        for item in moves:
            if 0<=item[0]<=7 and 0<=item[1]<=7:
                if (item[1] == 3) and (board[3][item[0]] == 0) and (board[2][item[0]] != 0) and (self.moves_made == 0):##Initial jump
                    if board[2][item[0]].name[0] != board[position[1]][position[0]].name[0]:
                        move.append(item)
                elif (item[1] == position[1]+1):
                    if board[item[1]][item[0]] == 0:
                        move.append(item)
                else:
                    move.append(item)
        return move


class Knight(Piece):#Finished
    def __init__(self, window, image, position, **kwargs) -> None:
        super().__init__(window, image, position, **kwargs)

    def get_moves(self, position, board):
        moves = []
        moves.append((position[0]+1, position[1]+2))
        moves.append((position[0]-1, position[1]+2))
        moves.append((position[0]+2, position[1]+1))
        moves.append((position[0]-2, position[1]+1))
        moves.append((position[0]-2, position[1]-1))
        moves.append((position[0]+2, position[1]-1))
        moves.append((position[0]+1, position[1]-2))
        moves.append((position[0]-1, position[1]-2))

        move = []
        for item in moves:
            if 0<=item[0]<=7 and 0<=item[1]<=7:
                move.append(item)

        return move
