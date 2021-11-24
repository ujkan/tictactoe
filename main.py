from ttt import players
from ttt import game

def main():
    N = 1
    ran = range(1, 7)
    wins = []
    losses = []
    for d in ran:
        # p1 = players.RandomPlayer('random')
        p1 = players.MinimaxPlayer('minimax1', d, 'X')
        p2 = players.MinimaxPlayer('minimax2', d, 'O')
        p1_wins = 0
        p1_losses = 0
        for i in range(N):
            gamex = game.Game(p1, p2)
            gamex.play()
            if (gamex.state == game.GameState.XWIN):
                p1_wins += 1
            elif (gamex.state == game.GameState.OWIN):
                p1_losses += 1
        wins.append(p1_wins/N)
        losses.append(p1_losses)
    # if minimax is to play correctly, it should never lose
    print("Wins: ", wins)
    print("Number of losses: ", sum(losses))
   

if __name__ == "__main__":
    main()