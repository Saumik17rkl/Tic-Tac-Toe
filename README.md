# Tic Tac Toe with AI (Tkinter)  

This is a Python-based Tic Tac Toe game featuring an AI opponent and a unique gameplay rule where only the last three moves of each player remain on the board.  

## Features  
- **AI Opponent**: Uses the Minimax algorithm for strategic gameplay.  
- **Limited Moves Rule**: Each player can only have three moves on the board at a time. When a new move is made, the oldest move disappears.  
- **Graphical Interface**: Built using Tkinter for an interactive experience.  
- **Win Detection**: Checks for winning conditions after every move.  

## How to Run  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Saumik17rkl/Tic-Tac-Toe.git
   ```
2. Navigate to the project folder:  
   ```bash
   cd Tic-Tac-Toe
   ```
3. Run the game:  
   ```bash
   python tictactoe.py
   ```

## How to Play  
- Click on an empty cell to place your move (X).  
- The AI (O) will respond with its move.  
- Only the last three moves per player remain on the board. When a new move is made, the oldest move disappears.  
- The game continues until a player wins or all possible moves are exhausted.  

## Future Enhancements  
- Adjustable difficulty levels for AI.  
- Multiplayer mode.  
- Improved UI with animations.  
