import unittest
import ttt.game as game
import ttt.players as players

class TestMinimax(unittest.TestCase):
    def test_X_vs_random(self):
        N = 100
        ran = range(1, 7)
        for d in ran:
            p1 = players.MinimaxPlayer('minimax', d, 'X')
            p2 = players.RandomPlayer('random')
            p1_losses = 0
            for i in range(N):
                gamex = game.Game(p1, p2)
                gamex.play()
                if (gamex.state == game.GameState.OWIN):
                    # if minimax is to play correctly, it should never lose
                    self.fail('Minimax has lost.')
    
    def test_O_vs_random(self):
        N = 100
        ran = range(4, 7)
        for d in ran:
            p1 = players.RandomPlayer('random')
            p2 = players.MinimaxPlayer('minimax', d, 'O')
            for i in range(N):
                gamex = game.Game(p1, p2)
                gamex.play()
                if (gamex.state == game.GameState.XWIN):
                    # if minimax is to play correctly, it should never lose
                    gamex.board.print_board()
                    self.fail('Minimax has lost.')
                
    def test_vs_minimax(self):
        # because minimax is deterministic, N = 1 suffices
        N = 1
        ran = range(2, 7)
        for d in ran:
            p1 = players.MinimaxPlayer('minimax1', d, 'X')
            p2 = players.MinimaxPlayer('minimax2', d, 'O')
            for i in range(N):
                gamex = game.Game(p1, p2)
                gamex.play()
                if (gamex.state != game.GameState.DRAW):
                    self.fail('Minimax has lost.')
                    
    def test_vs_minimax_depth_1(self):
        p1 = players.MinimaxPlayer('minimax1', 1, 'X')
        p2 = players.MinimaxPlayer('minimax2', 1, 'O')
        gamex = game.Game(p1, p2)
        gamex.play()
        self.assertEquals(gamex.state, game.GameState.DRAW)

    # at depths below than 3, minimax loses as O
    def test_O_vs_random_depth_3(self):
        N = 100
        for i in range(N):
            p1 = players.RandomPlayer('random')
            p2 = players.MinimaxPlayer('minimax2', 3, 'O')
            gamex = game.Game(p1, p2)
            gamex.play()
            self.assertNotEqual(gamex.state, game.GameState.XWIN)

 

if __name__ == '__main__':
    unittest.main()