from ttt import players

def main():
    player1 = players.MinimaxPlayer('Ujkan', 4)
    player2 = players.RandomPlayer('Magnus') 
    game = players.game.Game(player1, player2)
    game.play()
    game.print_state()
   

if __name__ == "__main__":
    main()