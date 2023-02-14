package com.example.tictactoe.model;

import org.springframework.stereotype.Component;

import javax.persistence.Entity;

public abstract class Player {
    protected boolean turn;

    public void setTurn(boolean turn) {
        this.turn = turn;
    }

    public abstract int move(Board board);
}
