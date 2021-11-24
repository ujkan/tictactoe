from enum import Enum
from random import randint

    
class GameState(Enum):
    XWIN = 0
    OWIN = 1
    DRAW = 2
    ONGOING = 3
    
class Board:
    squares = ['X', 'O', '_']
    def __init__(self):
        self.board = '_________'
    
    def set_board(self, board):
        self.board = board
    def get_board(self):
        return self.board 
    def set_square(self, pos, symbol):
        self.board = self.board[:pos] + symbol + self.board[pos + 1:]
       
    @staticmethod 
    def update_eval(s, x1, x2, o1, o2): 
        if (s == 2):
            x2 +=1
        elif (s == 1):
            x1 += 1
        elif (s == -1):
            o1 += 1
        elif (s == -2):
            o2 += 2
        return x1, x2, o1, o2

    def board_eval(self):
        """Heuristic to evaluate a particular position from the perspective of X."""
        x2 = 0
        x1 = 0
        o2 = 0
        o1 = 0
        vals = {'_': 0, 'X' : 1, 'O' : -1}
        for row in range(3):
            s = sum(map(lambda sq: vals[sq], self.board[(0 + 3 * row) : (3 + 3 * row)]))
            x1, x2, o1, o2 = Board.update_eval(s, x1, x2, o1, o2)
        for col in range(3):
            s = sum(map(lambda sq: vals[sq], [self.board[0 * col + 3 * i] for i in range(3)]))
            x1, x2, o1, o2 = Board.update_eval(s, x1, x2, o1, o2)
        
        # first diagonal         
        s = sum(map(lambda sq: vals[sq], [self.board[i * 4] for i in range(3)]))
        x1, x2, o1, o2 = Board.update_eval(s, x1, x2, o1, o2)
        # second diagonal 
        s = sum(map(lambda sq: vals[sq], [self.board[2*i + 2] for i in range(3)]))
        x1, x2, o1, o2 = Board.update_eval(s, x1, x2, o1, o2)
        
        return 3*x2 + x1 - (3*o2 + o1)

    def state(self):
        """ returns 0 if X has won, 1 if Y has won, 2 if a draw has occurred, and 3 if the game is ongoing"""
        for k in range(2):
            for i in range(3):
                if (all(self.board[j + 3 * i] == self.squares[k] for j in range (3)) or all(self.board[0 * i + 3 * j] == self.squares[k] for j in range (3))):
                    return k
            if (all(self.board[i * 4] == self.squares[k] for i in range(3)) or all(self.board[2 * i + 2] == self.squares[k] for i in range(3))):
                return k
        if (len(self.get_empty_squares())==0):
            return 2
        return 3

    def get_square(self, pos):
        return self.board[pos]
    def get_empty_squares(self):
        return list(filter(lambda pos: self.board[pos] == '_', [i for i in range(9)]))
    def print_board(self):
        for i in range(3):
            print(self.board[(0 + 3 * i) : (3 + 3 * i)])
        print()
               
class Game:   
    def __init__(self, player1, player2):
       self.board = Board()
       self.turn = 0
       self.players = [player1, player2]
       self.state = GameState.ONGOING
    
    def won(self):
        k = (self.turn + 1)%2
        for i in range(3):
            if (all(self.board.get_square(j + 3 * i) == self.board.squares[k] for j in range (3)) or all(self.board.get_square(0 * i + 3 * j) == self.board.squares[k] for j in range (3))):
                    return k
        if (all(self.board.get_square(i * 4) == self.board.squares[k] for i in range(3)) or all(self.board.get_square(2 * i + 2) == self.board.squares[k] for i in range(3))):
            return k
        if (len(self.board.get_empty_squares())==0):
            return 2
        return 3
    
    def move(self, pos):
        assert(self.board.get_square(pos) == '_')
        self.board.set_square(pos, self.board.squares[self.turn])
   
    def play(self):
        flag = self.won()
        while (flag == 3):
            player_move = self.players[self.turn].move(self.board)
            self.move(player_move)
            self.turn = (self.turn + 1) % 2
            flag = self.won()
        self.state = GameState(flag)
        # self.board.print_board()
        # self.print_state()
        return 0 
    
    def print_state(self): 
        state_dict = {GameState.XWIN : 'X won', GameState.OWIN : 'O won', GameState.DRAW : 'DRAW', GameState.ONGOING : 'ONGOING'}
        print (state_dict[self.state])
     