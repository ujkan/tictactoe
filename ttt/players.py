from enum import Enum
from copy import deepcopy
from random import randint
from abc import ABC, abstractmethod
from game import Board, Square
class Player(ABC):
    def __init__(self, name):
        self.name = name
     
    @abstractmethod 
    def move(self, board):
        pass    
    
class RandomPlayer(Player):
    def move(self, board):
        empty_squares = board.get_empty_squares()
        r = randint(0, len(empty_squares) - 1)
        return empty_squares[r][0], empty_squares[r][1]



class NodeType(Enum):
    MAXNODE = 0
    MINNODE = 1
class GameTree:
    def __init__(self, rootType, board):
        self.board = board
        self.rootType = rootType
        self.eval = 0
        self.choice = 0
        self.alpha = -999
        self.beta = +999
    
    def crawl(self, depth, alpha, beta):
        self.alpha = alpha
        self.beta = beta
        empty_squares = self.board.get_empty_squares()
        if (empty_squares == [] or depth == 0):
            winner = self.board.state() 
            if (winner == 0):
                self.eval = 1
            elif (winner == 1):
                self.eval = -1
            else: 
                # bad eval function
                #    self.eval = 0
                # better eval function
                self.eval = self.board.board_eval()
            return
        for i in range(len(empty_squares)): 
            emptysq = empty_squares[i]
            symbol = Square.EMPTY
            flag = True
            if (self.rootType == NodeType.MAXNODE):
                self.eval = -999
                childType = NodeType.MINNODE
                symbol = Square.X
                flag = True
            else:
                self.eval = +999
                childType = NodeType.MAXNODE
                symbol = Square.O
                flag = False
            child_board = Board()
            child_board.set_board(deepcopy(self.board.get_board()))
            child_board.set_square(emptysq[0], emptysq[1], symbol)
            # child_board.print_board()
            child_tree = GameTree(childType, child_board)
            child_tree.crawl(depth-1, self.alpha, self.beta)
            if (flag):
                if (self.eval < child_tree.eval):
                    self.eval = child_tree.eval
                    self.choice = emptysq
                if (self.eval >= self.beta):
                    break
                self.alpha = max(self.alpha, self.eval)
            else:
                if (self.eval > child_tree.eval):
                    self.eval = child_tree.eval
                    self.choice = emptysq
                
                if (self.eval <= self.alpha):
                    break
                self.beta = min(self.beta, self.eval)
         


class MinimaxPlayer(Player):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth
        
    def move(self, board):
        tree = GameTree(NodeType.MAXNODE, board)
        tree.crawl(self.depth,-99,99)
        sq = tree.choice
        return sq[0], sq[1]
         