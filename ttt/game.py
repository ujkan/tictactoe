from enum import Enum
from random import randint
class Square(Enum):
    X = 0
    O = 1
    EMPTY = 2
    
class GameState(Enum):
    XWIN = 0
    OWIN = 1
    DRAW = 2
    ONGOING = 3
    
class Board:
    def __init__(self):
        self.board = [[Square.EMPTY for i in range(3)] for j in range(3)]
    
    def set_board(self, board):
        self.board = board
    def get_board(self):
        return self.board
    
    def set_square(self, posX, posY, symbol):
        self.board[posX][posY] = symbol
        
    def board_eval(self):
        x2 = 0
        x1 = 0
        o2 = 0
        o1 = 0
        vals = {Square.EMPTY : 0, Square.X : 1, Square.O : -1}
        for row in range(3):
            s = sum(map(lambda sq: vals[sq], self.board[row]))
            if (s == 2):
                x2 +=1
            elif (s == 1):
                x1 += 1
            elif (s == -1):
                o1 += 1
            elif (s == -2):
                o2 += 2
        for col in range(3):
            s = sum(map(lambda sq: vals[sq], [self.board[i][col] for i in range(3)]))
            if (s == 2):
                x2 +=1
            elif (s == 1):
                x1 += 1
            elif (s == -1):
                o1 += 1
            elif (s == -2):
                o2 += 2
                
        s = sum(map(lambda sq: vals[sq], [self.board[i][i] for i in range(3)]))
        if (s == 2):
            x2 +=1
        elif (s == 1):
            x1 += 1
        elif (s == -1):
           o1 += 1
        elif (s == -2):
            o2 += 2
        s = sum(map(lambda sq: vals[sq], [self.board[i][2-i] for i in range(3)]))
        if (s == 2):
            x2 +=1
        elif (s == 1):
            x1 += 1
        elif (s == -1):
           o1 += 1
        elif (s == -2):
            o2 += 2
            
            
        return 3*x2 + x1 - (3*o2 + o1)

 
                 
            
    def state(self):
        for k in range(2):
            for i in range(3):
                if (all(self.board[i][j] == Square(k) for j in range (3)) or all(self.board[j][i] == Square(k) for j in range (3))):
                    return k
            if (all(self.board[i][i] == Square(k) for i in range(3)) or all(self.board[i][2-i] == Square(k) for i in range(3))):
                return k
        if (len(self.get_empty_squares())==0):
            return 2
        return 3

    def get_square(self, posX, posY):
        return self.board[posX][posY] 
    def get_empty_squares(self):
        return list(filter(lambda pos: self.board[pos[0]][pos[1]] == Square.EMPTY, [(i, j) for i in range(3) for j in range(3)]))
    def print_board(self):
        dict_squares = {Square.X : 'X', Square.O : 'O', Square.EMPTY : '_'}
        for row in range(2, -1, -1):
            line = list(map(lambda sq: dict_squares[sq], self.board[row]))
            print(''.join(line))   
        print("")
               
class Game:   
    def __init__(self, player1, player2):
       self.board = Board()
       self.turn = 0
       self.players = [player1, player2]
       self.state = GameState.ONGOING
    
    def won(self):
        player = (self.turn + 1)%2
        for i in range(3):
            if (all(self.board.get_square(i, j) == Square(player) for j in range (3)) or all(self.board.get_square(j, i) == Square(player) for j in range (3))):
                return player
        if (all(self.board.get_square(i, i) == Square(player) for i in range(3)) or all(self.board.get_square(i, 2-i) == Square(player) for i in range(3))):
            return player
        if (self.board.get_empty_squares() == []):
            return 2
        return 3
    
    def move(self, posX, posY):
        assert(self.board.get_square(posX, posY) == Square.EMPTY)
        self.board.set_square(posX, posY, Square(self.turn))
   
    def play(self):
        flag = self.won()
        while (flag == 3):
            #print("*******")
            #self.board.print_board()
            #print("*******")
            player_move = self.players[self.turn].move(self.board)
            self.move(player_move[0], player_move[1])
            self.turn = (self.turn + 1) % 2
            flag = self.won()
        self.state = GameState(flag)
        return 0 
    
    def print_state(self): 
        state_dict = {GameState.XWIN : 'X won', GameState.OWIN : 'O won', GameState.DRAW : 'DRAW', GameState.ONGOING : 'ONGOING'}
        print (state_dict[self.state])
     