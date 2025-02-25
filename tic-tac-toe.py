import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.move_history = {"X": [], "O": []}  # Track moves separately for each player
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe with AI")
        
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=3, font=("Arial", 20), command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        
    def make_move(self, row, col):
        if self.board[row][col] == "":
            if len(self.move_history[self.current_player]) >= 3:
                old_row, old_col = self.move_history[self.current_player].pop(0)
                self.board[old_row][old_col] = ""
                self.buttons[old_row][old_col].config(text="", state=tk.NORMAL)
            
            self.board[row][col] = self.current_player
            self.move_history[self.current_player].append((row, col))
            self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED)
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.window.quit()
            elif self.is_board_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                if self.current_player == "O":
                    self.ai_move()
    
    def ai_move(self):
        best_score = float('-inf')
        best_move = None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = "O"
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        
        if best_move:
            self.make_move(best_move[0], best_move[1])
    
    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("O"):
            return 10 - depth
        if self.check_winner("X"):
            return depth - 10
        if self.is_board_full():
            return 0
        
        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "O"
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ""
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = "X"
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ""
                        best_score = min(score, best_score)
            return best_score
    
    def check_winner(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False
    
    def is_board_full(self):
        return all(cell != "" for row in self.board for cell in row)
    
    def run(self):
        self.window.mainloop()

game = TicTacToe()
game.run()