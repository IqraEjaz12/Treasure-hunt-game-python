"""
treasure_hunt.py
A simple graphical Treasure Hunt game using tkinter.

How to run:
    python treasure_hunt.py
"""

import tkinter as tk
from tkinter import messagebox
import random

# ----- Game settings -----
GRID_SIZE = 6        # grid will be GRID_SIZE x GRID_SIZE
MAX_TURNS = 8        # allowed incorrect guesses
BUTTON_SIZE = 6      # visual button size

# ----- Game logic / state -----
class TreasureHuntGame:
    def __init__(self, master):
        self.master = master
        master.title("Treasure Hunt 🗺️")
        self.frame = tk.Frame(master, padx=10, pady=10)
        self.frame.pack()

        # top controls
        ctrl_frame = tk.Frame(self.frame)
        ctrl_frame.grid(row=0, column=0, columnspan=GRID_SIZE, sticky="we", pady=(0,8))
        self.info_label = tk.Label(ctrl_frame, text="", font=("Helvetica", 12))
        self.info_label.pack(side="left")
        restart_btn = tk.Button(ctrl_frame, text="Restart", command=self.reset_game)
        restart_btn.pack(side="right")

        # hint area
        self.hint_label = tk.Label(self.frame, text="Click a cell to search for the treasure!", anchor="w")
        self.hint_label.grid(row=1, column=0, columnspan=GRID_SIZE, sticky="we", pady=(0,8))

        # grid of buttons
        self.buttons = {}
        grid_frame = tk.Frame(self.frame)
        grid_frame.grid(row=2, column=0, columnspan=GRID_SIZE)
        for r in range(GRID_SIZE):
            for c in range(GRID_SIZE):
                btn = tk.Button(grid_frame,
                                text="?",
                                width=BUTTON_SIZE,
                                height=2,
                                command=lambda rr=r, cc=c: self.on_click(rr, cc))
                btn.grid(row=r, column=c, padx=3, pady=3)
                self.buttons[(r, c)] = btn

        # status footer
        self.status_label = tk.Label(self.frame, text="", font=("Helvetica", 10, "italic"))
        self.status_label.grid(row=3, column=0, columnspan=GRID_SIZE, pady=(8,0))

        # start the first game
        self.reset_game()

    def reset_game(self):
        # place treasure at random row, col
        self.treasure_r = random.randint(0, GRID_SIZE - 1)
        self.treasure_c = random.randint(0, GRID_SIZE - 1)
        self.turns_left = MAX_TURNS
        self.game_over = False

        # reset UI buttons
        for (r, c), btn in self.buttons.items():
            btn.config(text="?", state="normal", relief="raised", bg=None)

        self.update_labels("New game started! Find the treasure.")
        self.hint_label.config(text=f"You have {self.turns_left} attempts. Good luck!")

    def update_labels(self, status_text):
        self.status_label.config(text=status_text)
        self.info_label.config(text=f"Grid: {GRID_SIZE}×{GRID_SIZE}    Attempts left: {self.turns_left}")

    def on_click(self, r, c):
        if self.game_over:
            return

        btn = self.buttons[(r, c)]
        # disable clicked button
        btn.config(state="disabled", relief="sunken")

        # correct guess
        if (r, c) == (self.treasure_r, self.treasure_c):
            btn.config(text="🏆", bg="#ffd700")
            self.reveal_treasure(win=True)
            return

        # wrong guess
        btn.config(text="X")
        self.turns_left -= 1

        # give directional hint (rows: 0 top -> down = south)
        vertical = ""
        horizontal = ""
        if r < self.treasure_r:
            vertical = "SOUTH"
        elif r > self.treasure_r:
            vertical = "NORTH"

        if c < self.treasure_c:
            horizontal = "EAST"
        elif c > self.treasure_c:
            horizontal = "WEST"

        # combine hints elegantly
        if vertical and horizontal:
            hint = f"The treasure is to the {vertical}-{horizontal} from here."
        elif vertical:
            hint = f"The treasure is to the {vertical} from here."
        elif horizontal:
            hint = f"The treasure is to the {horizontal} from here."
        else:
            hint = "You're very close!"

        self.hint_label.config(text=hint)
        self.update_labels("Keep searching...")

        # check lose condition
        if self.turns_left <= 0:
            self.reveal_treasure(win=False)

    def reveal_treasure(self, win: bool):
        # reveal treasure cell visually
        for (r, c), btn in self.buttons.items():
            if (r, c) == (self.treasure_r, self.treasure_c):
                btn.config(text="💎", bg="#7CFC00", state="disabled", relief="sunken")
            else:
                # optionally disable all remaining buttons so game ends cleanly
                btn.config(state="disabled")

        self.game_over = True
        if win:
            self.hint_label.config(text=f"🎉 You found the treasure! ({self.treasure_r+1}, {self.treasure_c+1})")
            messagebox.showinfo("You win!", "Congratulations — you found the treasure!")
        else:
            self.hint_label.config(text=f"💔 Out of attempts. Treasure was at row {self.treasure_r+1}, col {self.treasure_c+1}.")
            messagebox.showinfo("Game over", f"Out of attempts!\nTreasure was at row {self.treasure_r+1}, col {self.treasure_c+1}.")

        self.update_labels("Game over. Press Restart to play again.")

# ----- Run the app -----
if __name__ == "__main__":
    root = tk.Tk()
    # make window not huge on small screens
    root.resizable(False, False)
    app = TreasureHuntGame(root)
    root.mainloop()
