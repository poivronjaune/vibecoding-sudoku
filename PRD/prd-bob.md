# Product Requirements Document (PRD)

**Project Name:** Sudoku Trainer  
**Version:** 0.3  
**Author:** Robert Boivin (Owner)  
**Date:** 2025-08-29  

---

## 1. Objective
The goal is to create a minimalist, interactive Sudoku game designed to help players practice and improve their Sudoku-solving techniques and eventually become masters at thegame.  
The game will generate a valid and solvable puzzle of user specified difficulty level and prefered techniques to practice.  

The main screen will offer a difficulty selector, a techniques selector, a reset button, an undo button, a pause button, a timer, a number panel that reflects remaining digits, a toggle button to add notes in cells, .

### Goals  

- 
- To provide users with a functional and intuitive interface for solving Sudoku puzzles.
- To generate a continuous supply of uniquely solvable puzzles across various difficulty levels clearly labeled easy, medium, or hard.
- To create a focused, distraction-free, clean Sudoku experience that reinforces solving discipline and time-on-task.
- To establish a core modular product that can be expanded upon with more advanced training features in future versions.


## 2. Target Audience

* Sudoku enthusiasts seeking structured practice.
* New players learning solving techniques.
* Users wanting to time their solving sessions for performance improvement.



---
## 99. Technical details

#### SOLVING TECHNIQUES

#### THE GRID
The grid will be a clean 9×9 grid, seperated in three horizontal blocks and 3 vertical blocs. These blocks are 3x3 in size with internal lines of 2 px and outer lines of 4 px. The outermost 9x9 grid border must be 6 px thick.

![Grid example](.\GrilleSudokuMinimaliste.png "Example sudoku grid")  

