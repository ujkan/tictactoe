package com.example.tictactoe.model;

import org.springframework.stereotype.Component;
import org.springframework.stereotype.Repository;

import javax.persistence.Entity;

@Entity
public enum GameState {
    XWIN, OWIN, DRAW, ONGOING;
}
