package com.example.tictactoe.model;

import org.springframework.stereotype.Component;

import javax.persistence.Entity;
import java.util.Random;
@Entity
@Component("Random")
public class RandomPlayer extends Player {
    @Override
    public int move(Board board) {
        Random r = new Random();
        int s = board.getEmptySquares().size();
        return board.getEmptySquares().get(r.nextInt(s));
    }
}
