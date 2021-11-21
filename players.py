from enum import Enum
from copy import deepcopy
from random import randint
from abc import ABC, abstractmethod
import game
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
    XNODE = 0
    ONODE = 1
class GameTree:
    def __init__(self, rootType, board):
        self.board = board
        self.rootType = rootType
        self.children = []
        self.eval = 0
        self.choice = 0
    
    def crawl(self, depth):
        empty_squares = self.board.get_empty_squares()
        if (empty_squares == [] or depth == 0):
            winner = self.board.state() 
            if (winner == 0):
                self.eval = 1
            elif (winner == 1):
                self.eval = -1
            else:
                self.eval = 0
            return
        for emptysq in self.board.get_empty_squares():
            symbol = game.Square.EMPTY
            flag = True
            if (self.rootType == NodeType.XNODE):
                childType = NodeType.ONODE
                symbol = game.Square.X
                flag = True
            else:
                childType = NodeType.XNODE
                symbol = game.Square.O
                flag = False
            child_board = game.Board()
            child_board.set_board(deepcopy(self.board.get_board()))
            child_board.set_square(emptysq[0], emptysq[1], symbol)
            # child_board.print_board()
            child_tree = GameTree(childType, child_board)
            self.children.append([child_tree, emptysq])
            child_tree.crawl(depth-1)
        evals = [ch[0].eval for ch in self.children]
        if (flag): 
            index_max = max(range(len(evals)), key=evals.__getitem__)
            self.choice = self.children[index_max][1]
        else:
            index_min = min(range(len(evals)), key=evals.__getitem__)
            self.choice = self.children[index_min][1]

            
         
    

class MinimaxPlayer(Player):
    def __init__(self, name, depth):
        super().__init__(name)
        self.depth = depth
        
    def move(self, board):
        tree = GameTree(NodeType.XNODE, board)
        tree.crawl(self.depth)
        sq = tree.choice
        return sq[0], sq[1]
         