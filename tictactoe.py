
import tkinter as tk

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tic Tac Toe")
        self.geometry("250x300")

        # Create buttons for the game board
        self.buttons = []
        for i in range(9):
            button = tk.Button(self, width=5, height=2, command=lambda i=i: self.play(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)

        # Create a label to display the status
        self.status = tk.StringVar()
        self.status_label = tk.Label(self, textvariable=self.status)
        self.status_label.pack()
        self.status.set("X's turn")

        self.player = "X"
        self.game_over = False

    def play(self, index):
        if self.game_over:
            return
        if self.buttons[index]["text"] != "":
            return
        self.buttons[index].config(text=self.player)
        if self.check_win(self.player):
            self.status.set(f"{self.player} wins!")
            self.game_over = True
        elif self.check_draw():
            self.status.set("It's a draw!")
            self.game_over = True
        else:
            self.player = "O" if self.player == "X" else "X"
            self.status.set(f"{self.player}'s turn")

    def check_win(self, player):
        # Check rows
        for i in range(3):
            if self.buttons[i*3]["text"] == player and self.buttons[i*3+1]["text"] == player and self.buttons[i*3+2]["text"] == player:
                return True
        # Check columns
        for i in range(3):
            if self.buttons[i]["text"] == player and self.buttons[i+3]["text"] == player and self.buttons[i+6]["text"] == player:
                return True
        # Check diagonals
        if self.buttons[0]["text"] == player and self.buttons[4]["text"] == player and self.buttons[8]["text"] == player:
            return True
        if self.buttons[2]["text"] == player and self.buttons[4]["text"] == player and self.buttons[6]["text"] == player:
            return True
        return False

    def check_draw(self):
        for button in self.buttons:
            if button["text"] == "":
                return False
        return True

if __name__ == "__main__":
    game = TicTacToe()
    game.mainloop()
