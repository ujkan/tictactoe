from enum import Enum
from copy import deepcopy
from random import randint
from abc import ABC, abstractmethod
from . import game

# from game import Board, game.Square
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
        return empty_squares[r]



class NodeType(Enum):
    MAXNODE = 0
    MINNODE = 1
    
class GameTree:
    def __init__(self, rootType, board, alpha, beta):
        self.board = board
        self.rootType = rootType
        self.eval = 0
        self.choice = -1
        self.alpha = alpha
        self.beta = beta
    
    def crawl(self, depth):
        empty_squares = self.board.get_empty_squares()
        winner = self.board.state()
        if (winner != 3 or depth == 0):
            winner = self.board.state() 
            if (winner == 0):
                self.eval = 99
            elif (winner == 1):
                self.eval = -99
            else: 
                # bad eval function
                #    self.eval = 0
                # better eval function
                self.eval = self.board.board_eval()
            return
        self.choice = empty_squares[0]
        if (self.rootType == NodeType.MAXNODE):
            self.eval = -99
            childType = NodeType.MINNODE
            symbol = 'X'
            for i in range(len(empty_squares)): 
                emptysq = empty_squares[i]
                child_board = game.Board()
                child_board.set_board(self.board.get_board())
                child_board.set_square(emptysq, symbol)
                # child_board.print_board()
                child_tree = GameTree(childType, child_board, self.alpha, self.beta)
                child_tree.crawl(depth-1)
                if (self.eval < child_tree.eval):
                    self.eval = child_tree.eval
                    self.choice = emptysq
                if (self.eval >= self.beta):
                    break
                self.alpha = max(self.alpha, self.eval)
        else: #MINNODE 
            self.eval = 99
            childType = NodeType.MAXNODE
            symbol = 'O'
            for i in range(len(empty_squares)): 
                emptysq = empty_squares[i]
                child_board = game.Board()
                child_board.set_board(self.board.get_board())
                child_board.set_square(emptysq, symbol)
                # child_board.print_board()
                child_tree = GameTree(childType, child_board, self.alpha, self.beta)
                child_tree.crawl(depth-1)
                if (self.eval > child_tree.eval):
                    self.eval = child_tree.eval
                    self.choice = emptysq
                if (self.eval <= self.alpha):
                    break
                self.beta = min(self.beta, self.eval)

         


class MinimaxPlayer(Player):
    def __init__(self, name, depth, square):
        super().__init__(name)
        self.depth = depth
        if (square == 'X'):
            self.type = NodeType.MAXNODE
        elif (square == 'O'):
            self.type = NodeType.MINNODE
        
    def move(self, board):
        tree = GameTree(self.type, board, -99, 99)
        tree.crawl(self.depth)
        return tree.choice
        