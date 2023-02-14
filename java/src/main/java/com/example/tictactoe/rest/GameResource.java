package com.example.tictactoe.rest;
import com.example.tictactoe.model.Board;
import com.example.tictactoe.model.GameState;
import com.example.tictactoe.service.GameService;
import org.springframework.web.bind.annotation.*;

import java.util.Map;

@CrossOrigin(origins = "http://localhost:3000")
@RestController
public class GameResource {
    private GameService gameService;

    public GameResource(GameService gameService) {
        this.gameService = gameService;
    }

    @PutMapping("/board")
    public void move(@RequestBody Map<String, Integer> req) {
        this.gameService.move(req.get("pos"));
    }

    @GetMapping("/state")
    public GameState getGameState() { return this.gameService.getState(); }

    @GetMapping("/ai")
    public int getAiMove() { return this.gameService.aiMove(); }
    @GetMapping("/board")
    public Board getBoard() {
        return this.gameService.getBoard();
    }

    @GetMapping("/move")
    public int lastMove() {
        return this.gameService.getLastMove();
    }

}
