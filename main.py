from ttt import players
from ttt import game

def main():
    p1 = players.MinimaxPlayer('Ujkan', 4)
    p2 = players.RandomPlayer('Magnus') 
    N = 10
    ran = range(3, 7)
    wins = []
    losses = []
    for d in ran:
        p1 = players.MinimaxPlayer('minimax', d)
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
    print(losses)
   

if __name__ == "__main__":
    main()