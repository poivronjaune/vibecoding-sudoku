# Installation Instructions for Sudoku Pygame

## Overview
This project is a minimalist Sudoku game built using Pygame. It allows users to practice and improve their Sudoku-solving skills through an interactive interface.

## Prerequisites
- Python 3.10 to less than 3.13
- Poetry (for dependency management)

## Installation Steps

1. **Clone the Repository**
   ```bash
   git clone https://github.com/poivronjaune/vibecoding-sudoku.git
   cd vibecoding-sudoku
   ```
   Make sure your python wheel and distlib are updated  
   ```bash
   py -3.12 -m pip install --upgrade pip setuptools wheel
   py -3.12 -m pip install "virtualenv<20.33,>=20.26.6" --force-reinstall  
   py -3.12 -m pip install --upgrade distlib
   ```

2. **Install Poetry**
   If you haven't installed Poetry yet, you can do so by following the instructions on the [Poetry website](https://python-poetry.org/docs/#installation).

3. **Setup Poetry virtaul env & Install Dependencies**  
   Make sure no residual poetry virtual environment exist
   ```bash   
   poetry env remove python
   ```
   Setup poetry to use the python launcher with the correct python version you want to use  
   ```bash
   poetry env use "$(py -3.12 -c "import sys; print(sys.executable)")"
   ```
   Use Poetry to install the project dependencies:
   ```bash
   poetry install
   ```

4. **Run the Game**
   After installing the dependencies, you can run the game using:
   ```bash
   poetry run python -m sudoku.main
   ```

## Project Structure
- `sudoku/`: Contains the main game logic and assets.
- `tests/`: Contains unit tests for the game components.
- `pyproject.toml`: Configuration file for Poetry, specifying dependencies and project metadata.
- `.gitignore`: Specifies files and directories to be ignored by Git.

## Usage
Once the game is running, you can select numbers from the panel and place them on the Sudoku grid. The game will track your progress and provide a clean interface for solving puzzles.

## Future Enhancements
This project is a work in progress, and future updates may include additional features such as:
- Step-by-step solving hints
- Difficulty levels for puzzles
- Enhanced user interface elements

Feel free to contribute to the project by submitting issues or pull requests!