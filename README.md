# Tic Tac Toe with AI (Tkinter)  

This is an advanced Tic Tac Toe game built using Python's Tkinter library. It features an AI opponent and a unique gameplay rule where only the last three moves of each player remain on the board.  

## Features  
- **AI Opponent**: Uses the Minimax algorithm for optimal gameplay.  
- **Limited Moves Rule**: Each player can only have three moves on the board at any time. When a new move is made, the oldest move disappears.  
- **Graphical Interface**: A user-friendly UI built with Tkinter.  
- **Win Detection**: Checks for a winner or draw condition after every move.  

## How to Run  
1. Clone the repository:  
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project folder:  
   ```bash
   cd tictactoe-tkinter
   ```
3. Install dependencies (if needed):  
   ```bash
   pip install tk
   ```
4. Run the game:  
   ```bash
   python tictactoe.py
   ```

## How to Play  
- Click on an empty cell to place your move (X).  
- The AI (O) will respond with its move.  
- After each player has made three moves, their oldest move disappears when placing a new move.  
- The game continues until a player wins or the board is full.  

## Future Enhancements  
- Add difficulty levels for AI.  
- Implement a multiplayer mode.  
- Improve UI with animations.
- 
