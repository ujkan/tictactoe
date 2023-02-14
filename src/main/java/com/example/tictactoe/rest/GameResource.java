package com.example.tictactoe.rest;
import com.example.tictactoe.model.Board;
import com.example.tictactoe.service.GameService;
import org.springframework.web.bind.annotation.*;

@RestController
public class GameResource {
    private GameService gameService;

    public GameResource(GameService gameService) {
        this.gameService = gameService;
    }

    @PutMapping("/board")
    public int move(@RequestBody int pos) {
        this.gameService.move(pos);
        return pos;
    }

    @GetMapping("/board")
    public Board getBoard() {
        return this.gameService.getBoard();
    }

    @GetMapping("/move")
    public int lastMove() {
        return this.gameService.getLastMove();
    }

}
