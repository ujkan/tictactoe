from enum import Enum
from random import randint
class Square(Enum):
    X = 0
    O = 1
    EMPTY = 2
    
class GameResult(Enum):
    XWIN = 0
    OWIN = 1
    DRAW = 2
    ONGOING = 3
    
class Board:
    def __init__(self):
        self.board = [[Square.EMPTY for i in range(3)] for j in range(3)]
    
    def set_square(self, posX, posY, symbol):
        self.board[posX][posY] = symbol
    
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

class Player:
    def __init__(self, name):
        self.name = name
        
    def move(self, board):
        empty_squares = board.get_empty_squares()
        r = randint(0, len(empty_squares) - 1)
        return empty_squares[r][0], empty_squares[r][1]
        
        

class Game:   
    def __init__(self, player1, player2):
       self.board = Board()
       self.turn = 0
       self.players = [player1, player2]
       self.result = GameResult.ONGOING
    
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
            player_move = self.players[self.turn].move(self.board)
            self.move(player_move[0], player_move[1])
            self.turn = (self.turn + 1) % 2
            self.board.print_board()
            flag = self.won()
        self.result = GameResult(flag)
        return 0 
    def print_result(self): 
        result_dict = {GameResult.XWIN : 'X won', GameResult.OWIN : 'O won', GameResult.DRAW : 'DRAW', GameResult.ONGOING : 'ONGOING'}
        print (result_dict[self.result])
                    

def main():
    player1 = Player('Ujkan')
    player2 = Player('Magnus') 
    game = Game(player1, player2)
    game.play()
    game.print_result()
   

if __name__ == "__main__":
    main()