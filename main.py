from ttt import players
from ttt import game

def main():
    player1 = players.MinimaxPlayer('Ujkan', 7)
    player2 = players.RandomPlayer('Magnus') 
    gamex = game.Game(player1, player2)
    gamex.play()
    gamex.print_state()
   

if __name__ == "__main__":
    main()