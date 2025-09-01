🗺️ Treasure Hunt Game

A simple and fun graphical Treasure Hunt game built with Python and Tkinter.
The player has limited attempts to find the hidden treasure on a grid, with hints provided after each guess.

🎮 Features

Interactive 6×6 grid of clickable cells.

Limited turns (default: 8 attempts) to find the treasure.

Directional hints after each wrong guess (NORTH, SOUTH, EAST, WEST).

Clear win/lose messages with treasure reveal.

Restart option to play again instantly.

🛠️ Requirements

Python 3.7+

Tkinter (comes pre-installed with most Python distributions)

🚀 How to Run

Clone this repository:

git clone https://github.com/your-username/treasure-hunt.git
cd treasure-hunt


Run the game:

python treasure_hunt.py

🎯 How to Play

Start the game — a treasure is hidden in one random cell.

Click a cell to guess where the treasure is.

If wrong, you’ll get a hint about the treasure’s direction.

You win if you find the treasure before running out of attempts.

You lose if you run out of attempts — the treasure location is then revealed.

⚙️ Configuration

You can tweak game settings by editing these variables in treasure_hunt.py:

GRID_SIZE = 6      # Grid dimension (e.g., 6 = 6×6 grid)
MAX_TURNS = 8      # Number of allowed wrong guesses
BUTTON_SIZE = 6    # Button size (UI display)

📂 Project Structure
treasure-hunt/
│── treasure_hunt.py   # Main game file
│── README.md          # Project documentation

🏆 Future Improvements

Add difficulty modes (Easy/Medium/Hard).

Timer-based challenges.

Sound effects and animations.

High-score tracking system.

📜 License

This project is licensed under the MIT License — feel free to modify and share.



