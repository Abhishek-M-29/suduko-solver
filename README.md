**Sudoku Solver**

This is a Sudoku Solver written in Python with a graphical user interface (GUI) built using Tkinter.

**Installation**
Clone the repository:

    sh
    git clone https://github.com/Abhishek-M-29/suduko-solver.git
    cd suduko-solver

Ensure you have Python installed. You can download it from python.org.

Install Tkinter if it is not already installed:

    sh
    pip install python-tk

**Usage**
Navigate to the project directory:

    sh
    cd suduko-solver


Run the Sudoku Solver:

    sh
    python "Sudoku Solver.py"

    
The GUI will open. You can interact with the buttons to input values and solve the Sudoku puzzle.

**Code Structure**

Sudoku Solver.py: The main script that initializes the GUI and contains the logic for solving Sudoku puzzles.

Main Functions

 ButtonClick(r, c): Handles button clicks in the GUI, updating the Sudoku grid.
 
 main(): Initializes the Sudoku board and contains the logic for solving the puzzle.
 
 findEmpty(): Finds the next empty cell in the Sudoku grid.
 
 valid(num, pos): Checks if a number is valid in a specific position.
 
 solve(): Uses a backtracking algorithm to solve the Sudoku puzzle.
 
 enter(): Updates the GUI with the solved puzzle.
 
**Contributing**

We welcome contributions! Here are some ways you can contribute:

Report bugs or suggest features by opening an issue.
Fork the repository, make changes, and submit a pull request.
