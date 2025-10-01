(37 loc) · 1.87 KB
minesweeper

Minesweeper Mini (or MiniSweeper)
(Group 9 project - Phase 3 of SDF-FT14 - Python CLI)
Setup.
To play the game, run the main.py file in the root folder:

In the terminal:
- $ git clone git@github.com:Joseph-Hansel/python-minesweeper.git
- $ cd python-minesweeper
- $ source .venv/bin/activate     (If virtual environment not activated.)
- $ python3 main.py
Overview; About the Project.
MiniSweeper is a simplified version of the classic Minesweeper game. The goal is to create a functional and engaging game that can be played from the command line.

MVP Features:
Game Board: A grid-based game board with randomly placed mines.
Gameplay: Players can select cells to reveal their contents. If a cell contains a mine, the game is over.
Win Condition: The game is won when all non-mine cells are revealed.
User Interface
The interface used is the command line interface.
The game board will be displayed as a grid of cells.
Empty cells will be white and undug cells are brown
Technical Requirements
The game was developed using the Python Language, with application of ORM to integrate a database.
Packages installed include:
psycopg
sqlalchemy
alembic
python-dotenv
Future Development
Add additional features, such as:
Different difficulty levels (e.g., easy, medium, hard).
Customizable game board size.
Revealing the number of adjacent mines if a dug cell is empty.
Group members
Vanessa Tchappi - Scrum Master - Game logic
Joseph Hansel - Data Storage
Michael Kyalo - User interaction with CLI
Lyon Nganga - Game board generation