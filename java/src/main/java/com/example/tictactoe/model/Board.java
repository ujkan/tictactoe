package com.example.tictactoe.model;


import org.springframework.stereotype.Component;

import javax.persistence.Entity;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

@Entity
public class Board {
    private static final char[] symbols = new char[]{'X', 'O', '_'};
    private char[] board;
    private List<Integer> emptySquares;
    public Board() {
        this.board = new char[]{'_', '_', '_', '_', '_', '_', '_', '_', '_'};
        this.emptySquares = new ArrayList<Integer>();
        emptySquares.addAll(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8));
    }

    public void setBoard(String str) {
        emptySquares.removeIf(x -> true);
        emptySquares.addAll(Arrays.asList(0, 1, 2, 3, 4, 5, 6, 7, 8));
        for (int i = 0; i < board.length; i++) {
            this.setSquare(i, str.charAt(i));
        }
    }

    public String getBoard() {
        return String.valueOf(this.board);
    }

    public void setEmpty(int i) {
        this.board[i] = '_';
    }

    public static char[] getSymbols() {
        return symbols;
    }

    public char getSquare(int i) {
        return this.board[i];
    }

    public void setSquare(int i, char c) {
        this.board[i] = c;
        if (c != '_') {
            this.emptySquares.remove(Integer.valueOf(i));
        }
    }

    public List<Integer> getEmptySquares() {
        return emptySquares;
    }

    public boolean isSquareEmpty(int i) {
        return this.emptySquares.contains(i);
    }

    public void printBoard() {
        String line = "";
        for (int i = 2; i >= 0; i--) {
            line = "";
            for (int j = 0; j < 3; j++) {
                line += this.board[j + 3*i];
            }
            System.out.println(line);
        }
    }
}
