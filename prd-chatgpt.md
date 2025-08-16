# Product Requirements Document (PRD)

**Project Name:** Sudoku Trainer  
**Version:** 0.1  
**Author:** Robert Boivin (Owner)  
**Date:** 2025-08-15  

---

## 1. Objective

The goal is to create a minimalist, interactive Sudoku game designed to help players practice and improve their Sudoku-solving techniques. The game will generate valid puzzles of varying difficulty levels and provide an intuitive interface for number placement, tracking progress, and preventing cheating during pauses.

---

## 2. Target Audience

* Sudoku enthusiasts seeking structured practice.
* New players learning solving techniques.
* Users wanting to time their solving sessions for performance improvement.

---

## 3. Core Features

### 3.1 Sudoku Grid

* **Description:** A 9×9 Sudoku grid divided into nine 3×3 subgrids.
* **Functionality:**

  * Displays initial numbers from the generated puzzle.
  * Allows placing numbers by selecting an empty cell and clicking/tapping a number from the panel.
  * Highlights selected cell and optionally related row, column, and subgrid (optional future enhancement).

---

### 3.2 Number Panel

* **Description:** A panel showing numbers **1 to 9** available for placement.
* **Functionality:**

  * Clicking/tapping a number in the panel will prepare it for placement in the selected grid cell.
  * Numbers become **grayed out** when all nine of that number have been placed on the board.
  * Should visually indicate selected number for quick repeated placement.

---

### 3.3 Sudoku Puzzle Generator

* **Description:** Internal puzzle generator that creates valid Sudoku puzzles.
* **Functionality:**

  * Must ensure all generated puzzles have **one unique solution**.
  * Classifies puzzles into **Easy**, **Medium**, and **Hard** difficulty.
  * Algorithm for classification: based on number of givens and logical complexity required to solve.
  * Provides puzzles to the game grid in real time.

---

### 3.4 Timer

* **Description:** Real-time clock showing elapsed game time.
* **Functionality:**

  * Starts when puzzle is loaded.
  * Stops when puzzle is completed or game is paused.
  * Displays in `MM:SS` format (HH\:MM\:SS for long games).

---

### 3.5 Pause Button & Cheat Prevention

* **Description:** Pauses the game while preventing the player from studying the puzzle.
* **Functionality:**

  * Clicking “Pause” stops the timer.
  * An opaque overlay covers the grid, hiding all numbers.
  * Resume button restores grid visibility and continues the timer.

---

### 3.6 Graphics & User Interface

* **Style:** Minimalist, clean, distraction-free.
* **Elements:**

  * White or light background.
  * Thin black grid lines for main structure.
  * Slightly thicker lines for 3×3 subgrid boundaries.
  * Simple sans-serif font for numbers.
  * No animations except subtle hover/selection effects.

---

## 4. Technical Requirements

| Area              | Requirement                                                            |
| ----------------- | ---------------------------------------------------------------------- |
| **Platform**      | Initially web-based (desktop & mobile browsers)                        |
| **Language**      | HTML, CSS, JavaScript (core logic); possible WebAssembly for generator |
| **Storage**       | Local storage for saving ongoing game state (future)                   |
| **Performance**   | Instant puzzle load; responsive UI                                     |
| **Compatibility** | Works in major browsers (Chrome, Firefox, Edge, Safari)                |

---

## 5. Non-Functional Requirements

* **Accessibility:** High contrast mode option (future).
* **Responsiveness:** Works on touch devices and desktop screens.
* **Internationalization:** Numbers only (no localization needed for text in v0.1).
* **Expandability:** Modular code to allow future features (e.g., hint system, step-by-step technique training).

---

## 6. Future Expansion Ideas (Not in v0.1)

* Highlight conflicts (optional).
* Undo/redo moves.
* Step-by-step solving trainer mode.
* Leaderboards for timed challenges.
* Daily puzzle challenge.

---

## 7. Milestones & Deliverables

1. **MVP:**

   * Functional grid.
   * Number panel with graying out.
   * Puzzle generator with difficulty classification.
   * Timer and pause overlay.
   * Minimalist UI.

2. **Testing & Feedback:**

   * User tests to confirm ease of use and no major bugs.

3. **v1.0 Release:**

   * Public playable version meeting all above requirements.


