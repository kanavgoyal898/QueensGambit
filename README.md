# QueenGambit Chess Engine

## Overview
QueenGambit is a Python-based chess engine implemented using the `python-chess` library. It allows users to play against it at different difficulty levels or watch it play against itself. Minimax, depth-pruning, and alpha-beta pruning are crucial techniques in computer chess programming, especially given the vast number of possible board positions starting from the beginning of the game.

1. **Minimax Algorithm**: Minimax is fundamental for decision-making in game theory and chess AI. It works by recursively evaluating possible moves to determine the optimal move for the current player assuming the opponent plays optimally. This is essential because without such a method, evaluating all possible moves to the end of the game (especially considering the branching factor of chess) would be computationally infeasible.

2. **Depth-Pruning**: Depth-pruning limits the depth to which the minimax algorithm explores possible moves. This is critical in chess because it helps balance between depth of search (finding better moves) and computational feasibility. Without depth-pruning, the search space would grow exponentially, making it impractical to compute.

3. **Alpha-Beta Pruning**: Alpha-beta pruning further enhances efficiency by pruning branches of the search tree that cannot possibly influence the final decision. It reduces the number of nodes evaluated by the minimax algorithm by taking advantage of bounds (alpha and beta values) to discard irrelevant subtrees. This technique significantly speeds up the search process in chess AI.

Given the vast number of possible chess board positions (estimated around **1e43** to **1e50**), these techniques are indispensable. They allow chess engines to make intelligent decisions within a reasonable time frame by narrowing down the search space and focusing on the most promising moves. Without them, achieving competitive playing strength would be nearly impossible due to the sheer computational complexity involved.


<div style="text-align: center;">
  <img src="./chess.png" alt="Preview" style="width: 64%;">
</div>

## Library Installations
Before using QueenGambit, make sure you have the following libraries installed:
- **python-chess**: Used for chess board representation and move generation.
  ```bash
  pip install python-chess
  ```
- **cprint**: Used for colored console output during gameplay.
  ```bash
  pip install cprint
  ```

## Code Structure
The implementation is structured into several key components:

### `Engine` Class
- **Initialization (`__init__`):**
  - Initializes the chessboard, engine color (maximizing agent), maximum search depth, and other parameters.
  
- **Evaluation Functions:**
  - `checkmate_opportunity()`: Evaluates if the game is in a checkmate position and assigns scores accordingly.
  - `opening_catalyst()`: Provides a bonus for moves made in the opening phase of the game.
  - `evaluation_function()`: Combines the above evaluations to compute a total score for a given board position.
  - `piece_relative_value(position)`: Assigns relative values to each piece type on the board. You can find more information on relative piece value in chess in this [paper: Assessing Game Balance with AlphaZero: Exploring Alternative Rule Sets in Chess](https://arxiv.org/pdf/2009.04374) by Tomašev et al. (DeepMind, 2020).

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
1. Run the script `main.py`.
2. Follow the prompts to choose your color (Black/White) and difficulty level (Easy/Medium/Difficult).
3. Enter moves in algebraic notation when prompted during your turn.
4. The engine will respond with its move, and the game continues until completion.

## Additional Notes
- **Undo Move:** Typing "UNDO" allows the user to undo their last move.
- **End Game:** Typing "END" terminates the game.
- **Outcome:** After the game ends, the result (win/lose/draw) is displayed.