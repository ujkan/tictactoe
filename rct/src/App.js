import React, { useState, useEffect } from 'react';

const App = () => {
  // State to keep track of the current player (X or O)
  const [currentPlayer, setCurrentPlayer] = useState('X');

  // State to keep track of the cells and their contents
  const [grid, setGrid] = useState([
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
  ]);

  // Fetch the current game state from the API when the component mounts
  useEffect(() => {
    fetch('/api/game')
      .then(response => response.json())
      .then(data => {
        setGrid(data.grid);
        setCurrentPlayer(data.currentPlayer);
      });
  }, []);

  // Function to handle clicks on the grid cells
  const handleCellClick = (row, col) => {
    // Ignore the click if the cell is already filled
    if (grid[row][col] !== '') {
      return;
    }

    // Update the grid with the current player's symbol
    const updatedGrid = [...grid];
    updatedGrid[row][col] = currentPlayer;

    // Check if the game is over
    const gameOver = isGameOver(updatedGrid);

    let nextPlayer;
    if (gameOver) {
      // If the game is over, don't switch to the other player
      nextPlayer = currentPlayer;
    } else {
      // Switch to the other player
      nextPlayer = currentPlayer === 'X' ? 'O' : 'X';

      // If the other player is the AI, make a move on behalf of the AI
      if (nextPlayer === 'O') {
        fetch('/api/game/ai')
          .then(response => response.json())
          .then(aiMove => {
            // Update the grid with the AI's move
            const newGrid = [...updatedGrid];
            newGrid[aiMove.row][aiMove.col] = 'O';

            // Check if the game is over after the AI's move
            const newGameOver = isGameOver(newGrid);

            // Update the state with the new grid and current player
            setGrid(newGrid);
            setCurrentPlayer(newGameOver ? 'O' : 'X');

            // Send the updated game state to the API
            fetch('../../src/api/game', {
              method: 'PUT',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ grid: newGrid, currentPlayer: nextPlayer }),
            });
          });
      }
    }

    // Update the state with the new grid and current player
    setGrid(updatedGrid);
    setCurrentPlayer(nextPlayer);

    // Send the updated game state to the API
    fetch('/api/game', {
      method: 'PUT',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ grid: updatedGrid, currentPlayer

      })
    })
  }}

export default App;

// Log to console
console.log('Hello console')


