package com.example.tictactoe.service;

import com.example.tictactoe.model.Board;
import com.example.tictactoe.model.GameState;
import com.example.tictactoe.model.MinMaxPlayer;
import com.example.tictactoe.model.Player;
import org.springframework.stereotype.Service;

@Service
public class GameService {
    private Board board;
    private boolean turn;
    private MinMaxPlayer ai;
    private GameState state;
    private int lastMove;

    public void setBoard(Board board) {
        this.board = board;
    }

    public GameService() {
        this.board = new Board();
        this.turn = false;
        this.ai = new MinMaxPlayer();
        this.ai.setTurn(true);
        this.state = GameState.ONGOING;
        this.lastMove = -99;
    }

    public void move(int position) {
        if (this.board.getSquare(position) == '_') {
            this.board.setSquare(position, Board.getSymbols()[turn ? 1 : 0]);
            turn = !turn;
        }
        else
            throw new RuntimeException("INVALID MOVE. SQUARE OCCUPIED");
    }


    private static final int[][] next =
            {{1, -1, 3, 4},
                    {2, -1, 4, -1},
                    {0, 4, 5, -1},
                    {4, -1, 6, -1},
                    {5, 6, 7, 8},
                    {3, -1, 8, -1},
                    {7, 2, 0, -1},
                    {8, -1, 1, -1},
                    {6, -1, 2, 0}};



    public Board getBoard() {
        return board;
    }

    public static GameState stateAfter(Board board, boolean turn, int pos) {
        // Player in current turn has played in position i, what's the state?
        // Corner squares are part of 3 lines, center square is part of 4 lines, edge square is part of 2 lines
        int skipOne = 0;
        int skipTwo = 0;
        int actual = pos;
        if (pos % 2 == 1) {
            // Edge piece
            skipOne = 2;
            skipTwo = 4;
        }
        else if (pos != 4) {
            // Corner piece
            skipOne = (pos % 4) + 2;
        }
        int j = 0;
        for (int d = 1; d <= 4; d++) {
            if (d == skipOne || d == skipTwo)
                continue;
            actual = next[pos][d - 1];
            j = 1;
            while (j < 3) {
                // System.out.println("d, actual= " + d + ", " + actual);
                if (board.getSquare(actual) != Board.getSymbols()[turn ? 1 : 0])
                    break;
                actual = next[actual][d - 1];
                j++;
            }
            if (j == 3) {
                // System.out.println("WIN: d, j, Turn: " + d + ", " +j +", " +turn);
                if (!turn)
                    return GameState.XWIN;
                else
                    return GameState.OWIN;
            }

        }
        if (board.getEmptySquares().size() == 0)
            return GameState.DRAW;
        else
            return GameState.ONGOING;
    }

    public int aiMove() {
        int move = ai.move(this.board);
        this.board.setSquare(move, Board.getSymbols()[turn ? 1 : 0]);
        turn = !turn;
        return move;
    }
    public void play() {
        int playerMove;
        while (state == GameState.ONGOING) {
            // this.board.printBoard();
            // System.out.println("######\n");
            if (!turn) {
                playerMove = ai.move(this.board);
                this.move(playerMove);
                this.lastMove = playerMove;
                state = GameService.stateAfter(this.board, this.turn, playerMove);
                turn = !turn;
            }
        }
        // this.board.printBoard();

    }

    public int getLastMove() {
        return lastMove;
    }

    public GameState getState() {
        return state;
    }
}
