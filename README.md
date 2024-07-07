# QueenGambit Chess Engine

## Overview
QueenGambit is a Python-based chess engine implemented using the `python-chess` library. It allows users to play against it at different difficulty levels or watch it play against itself.

## Code Structure
The implementation is structured into several key components:

### `Engine` Class
- **Initialization (`__init__`):**
  - Initializes the chessboard, engine color (maximizing agent), maximum search depth, and other parameters.
  
- **Evaluation Functions:**
  - `checkmate_opportunity()`: Evaluates if the game is in a checkmate position and assigns scores accordingly.
  - `piece_relative_value(position)`: Assigns relative values to each piece type on the board.
  - `opening_catalyst()`: Provides a bonus for moves made in the opening phase of the game.
  - `evaluation_function()`: Combines the above evaluations to compute a total score for a given board position.

- **Minimax Algorithm:**
  - `max_value(depth, alpha, beta)`: Implements the maximizing agent's logic using minimax with alpha-beta pruning.
  - `min_value(depth, alpha, beta)`: Implements the minimizing agent's logic using minimax with alpha-beta pruning.
  - `get_best_move()`: Initiates the search for the best move using the minimax algorithm.

### Gameplay Functions
- **Player vs. Engine:**
  - `play_engine_move(board, color, max_depth)`: Allows the engine to make a move based on its evaluation.
  - `play_human_move(board)`: Accepts moves from the user, validates them, and updates the board accordingly.
  - `start_game(board, color, max_depth)`: Manages the flow of the game between player and engine.

- **User Interaction:**
  - `get_user_input()`: Takes user input for selecting color and difficulty level and starts the game accordingly.

### Main Execution
- **Main Function (`main()`):**
  - Entry point of the program, which initializes the game by calling `get_user_input()`.

## Usage
To play the game:
1. Run the script.
2. Follow the prompts to choose your color (Black/White) and difficulty level (Easy/Medium/Difficult).
3. Enter moves in algebraic notation when prompted during your turn.
4. The engine will respond with its move, and the game continues until completion.

## Additional Notes
- **Undo Move:** Typing "UNDO" allows the user to undo their last move.
- **End Game:** Typing "END" terminates the game.
- **Outcome:** After the game ends, the result (win/lose/draw) is displayed.