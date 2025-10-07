
Minesweeper Mini
(Group 9 project - Phase 2 of SDF-FT14)
Setup.
To view the game, you can either directly visit the live page or execute the following commands.

In the terminal:
$git clone git@github.com:Joseph-Hansel/group-9-minesweeper.git

$cd minesweeper

$npm run install

$npm run dev

Overview; About the Project.
MiniSweeper is a simplified version of the classic Minesweeper game. The goal is to create a functional and engaging game that can be played in a web browser.

MVP Features:
Game Board: A grid-based game board with randomly placed mines.
Gameplay: Players can click on cells to reveal their contents. If a cell contains a mine, the game is over. If a cell is empty, it will reveal the number of adjacent mines.
Win Condition: The game is won when all non-mine cells are revealed.
Reset Button: A button to reset the game and start a new round.
User Interface
The game board will be displayed as a grid of cells.
Each cell will have a distinct visual representation (e.g., empty cells will be blank, mine cells will have a mine icon, and numbered cells will display the number of adjacent mines).
The reset button will be prominently displayed above or below the game board.
Technical Requirements
The game will be built using HTML, CSS, and JavaScript.
The game board will be generated dynamically using JavaScript.
The game will use a simple random number generator to place mines on the board.
Future Development
Add additional features, such as:
Timer and score tracking.
Different difficulty levels (e.g., easy, medium, hard).
Customizable game board size.
Animations and sound effects.
Group members
- Vanessa Tchappi - Scrum Master - State and App management
- Joseph Hansel - Testing, and UX
- Michael Kyalo - Styling and Layout Designing
- Lyon Nganga - Game logic engineer
