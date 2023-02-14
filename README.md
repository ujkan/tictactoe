# Tic-Tac-Toe
This project consists of a React web app with a Java backend communicating with each other over a REST API.

Users can play Tic-Tac-Toe (as player 'X') against the game AI, which is based on the Minimax algorithm.

## Background
The genesis of the project was a desire to implement Minimax. This was initially done in Python, but all those commits have been deleted. Upon getting familiar with REST, I wanted to get my hands dirty and develop something myself. Instead of following a tutorial and simply copying instructions one after the other, I decided to do something from scratch (well, almost).

Since my Tic-Tac-Toe implementation needed an interface anyway, I thought I'd just write one in the form of a web app and make use of my already written Python code. With Spring Boot looking far more attractive than the frameworks available for Python, I decided to convert my Python code to Java, making quite a few changes along the way.

The decision to do this was perhaps ill-suited, as there are many features of a REST API that are totally unnecessary for Tic-Tac-Toe, but it was a start nonetheless.

## Current state
The app isn't complete. For one, I still need to have a "Game Over" notification. Secondly, the project stucture is a mess and I've yet to develop a neat way to build and run both the frontend and backend.

## How to run
To run the backend, simply open the `java` folder in a Java environment and run. Alternatively, run
```
mvn spring-boot:run
```
in the command line.

To run the frontend, run `npm start` in the [resources](java/src/main/resources) folder.
