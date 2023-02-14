package com.example.tictactoe.model;

import com.example.tictactoe.service.GameService;
import org.springframework.stereotype.Component;

import javax.persistence.Entity;

@Entity
@Component("MinMax")
public class MinMaxPlayer extends Player {

    private class Node {
        public int value;
        public int choice;

        public Node(int v, int c) {
            value = v;
            choice = c;
        }
    }
    private int eval(Board board, boolean mover, int lastMove) {
        GameState st = GameService.stateAfter(board, mover, lastMove);
        switch (st) {

            case XWIN -> {
                return this.turn ? -3 : 4;
            }
            case OWIN -> {

                return this.turn ? 4 : -3;
            }
            case DRAW -> {
                return -1;
            }
            default -> { return 0; }
        }

    }

    private Node minimax(Board board, boolean maximizingPlayer, int depth, int lastMove) {
        Node my = new Node(0, lastMove);
        Node child;
        Board childBoard = new Board();
        childBoard.setBoard(board.getBoard());
        if (lastMove != -1) {
            my.value = this.eval(board, maximizingPlayer != this.turn, lastMove);
            if (depth == 0 || my.value != 0) {
                return my;
            }
        }
            if (maximizingPlayer) {
                my.value = -3;
                for (Integer square : board.getEmptySquares()) {
                    childBoard.setBoard(board.getBoard());
                    childBoard.setSquare(square, Board.getSymbols()[turn ? 1 : 0]);
                    child = minimax(childBoard, false, depth - 1, square);
                    if (my.value < child.value) {
                        my.value = child.value;
                        my.choice = square;
                    }
                    if (my.value == 4)
                        return my;
                }
                return my;
            }
            else {
                my.value = +3;
                for (Integer square : board.getEmptySquares()) {
                    childBoard.setBoard(board.getBoard());
                    childBoard.setSquare(square, Board.getSymbols()[turn ? 0 : 1]);
                    child = minimax(childBoard, true, depth - 1, square);

                    if (my.value > child.value) {
                        my.value = child.value;
                        my.choice = square;
                    }
                    if (my.value == -3)
                        return my;
                }
                return my;
            }
    }
    @Override
    public int move(Board board) {
        Node n = minimax(board, true, 9, -1);
        return n.choice;
    }
}
