import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        self.buttons = [[tk.Button(master, text='', font=('Helvetica', 24), width=5, height=2, command=lambda i=i, j=j: self.click(i, j)) for j in range(3)] for i in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].grid(row=i, column=j)

    def click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player
            self.buttons[i][j].config(text=self.current_player)
            if self.check_winner(i, j):
                messagebox.showinfo("Victoire", f"Le joueur {self.current_player} a gagné !")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Match nul", "Le jeu est un match nul !")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        # Vérifier la ligne
        if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
            return True
        # Vérifier la colonne
        if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
            return True
        # Vérifier les diagonales
        if row == col and self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if row + col == 2 and self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def check_draw(self):
        return all(self.board[i][j] != ' ' for i in range(3) for j in range(3))

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ' '
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
