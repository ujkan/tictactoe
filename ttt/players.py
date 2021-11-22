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
        winner = self.board.state()
        if (winner != 3 or depth == 0):
            #print("depth: ", depth, " ;; ", "winner: ", winner)
            #self.board.print_board()
            #print("#########")
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
        self.choice = empty_squares[0]
        if (self.rootType == NodeType.MAXNODE):
            self.eval = -999
            childType = NodeType.MINNODE
            symbol = game.Square.X
            flag = True
            for i in range(len(empty_squares)): 
                emptysq = empty_squares[i]
                child_board = game.Board()
                child_board.set_board(deepcopy(self.board.get_board()))
                child_board.set_square(emptysq[0], emptysq[1], symbol)
                # child_board.print_board()
                child_tree = GameTree(childType, child_board)
                child_tree.crawl(depth-1, self.alpha, self.beta)
                if (self.eval < child_tree.eval):
                    self.eval = child_tree.eval
                    self.choice = emptysq
                if (self.eval >= self.beta):
                    break
                
                self.alpha = max(self.alpha, self.eval)
        if (self.rootType == NodeType.MINNODE):
            self.eval = 999
            childType = NodeType.MAXNODE
            symbol = game.Square.O
            flag = False
            for i in range(len(empty_squares)): 
                emptysq = empty_squares[i]
                child_board = game.Board()
                child_board.set_board(deepcopy(self.board.get_board()))
                child_board.set_square(emptysq[0], emptysq[1], symbol)
                # child_board.print_board()
                child_tree = GameTree(childType, child_board)
                child_tree.crawl(depth-1, self.alpha, self.beta)
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
        tree.crawl(self.depth,-9999999,999999999)
        sq = tree.choice
        return sq[0], sq[1]
        