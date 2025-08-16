# Sudoku Practice Game PRD – Updated

## Version  
Version: v2.0

## Overview

A minimalist Sudoku game designed to help players practice and master solving techniques. The MVP delivers a **clean 9×9 grid with thick 3×3 block borders, a 5-pixel margin around the grid, a number panel reflecting remaining digits, a solvable puzzle generator with difficulty classification, a timer, and a pause mode that hides the board**. Future iterations will add technique-driven training, guided hints, and analytics.

---

## Goals and Non-Goals

* **Primary goal:** Provide a fast, clean Sudoku experience reinforcing solving discipline and time-on-task.
* **Secondary goal:** Ensure every generated puzzle is uniquely solvable and correctly labeled easy, medium, or hard.
* **Non-goals (MVP):** Social features, daily leaderboards, accounts, cloud save, advanced theme customization, adaptive tutoring, and non-9×9 variants.

---

## User Stories and Success Metrics

### User Stories

* **US1 – Start:** As a player, I want to start a new puzzle with a chosen difficulty so I can practice at my level.
* **US2 – Place numbers:** As a player, I want to place numbers on a grid and see conflicts so I can correct mistakes early.
* **US3 – Remaining digits:** As a player, I want a number panel that grays out digits once all nine are placed so I can pace my choices.
* **US4 – Timer:** As a player, I want a timer that tracks my session so I can measure improvement.
* **US5 – Pause:** As a player, I want to pause the game and hide the board so I can take a break without temptation.
* **US6 – Difficulty clarity:** As a player, I want puzzles that truly match easy/medium/hard so I can train effectively.
* **US7 – Reliability:** As a player, I want puzzles to be solvable with a unique solution so I don’t waste time on broken boards.

### Success Metrics

* Completion rate ≥ 80% of puzzles played for ≥3 minutes.
* Difficulty accuracy ≥ 90% agreement with labeled difficulty.
* Initial load under 2 seconds; interactions under 16 ms frame budget.
* 0 known cases of non-unique or unsolvable boards.

---

## Functional Requirements

### Core Gameplay

* **FR1 – Grid:**

  * 9×9 grid with thick 3×3 subgrid boundaries and a **5-pixel margin around the grid**.
  * Acceptance: Clues are non-editable; user inputs editable; row/column/subgrid boundaries visually distinct; no lines overshooting outside the 9×9 area.

* **FR2 – Number Placement:**

  * Tap/click a cell, then tap a digit 1–9 to place; second tap removes it.
  * Acceptance: Placement blocked for clue cells; optional conflict highlighting indicates violations.

* **FR3 – Number Panel with Depletion:**

  * Panel shows digits 1–9 with remaining count (9 minus placements and clues).
  * When remaining count reaches 0, digit becomes disabled and grayed out.
  * Acceptance: Counts update in real time for placements/removals; no placement allowed for disabled digits; panel aligned below grid respecting margin.

* **FR4 – Puzzle Generator:**

  * Generates valid 9×9 puzzles with a unique solution.
  * Acceptance: Every puzzle passes a solver uniqueness check.

* **FR5 – Difficulty Classification:**

  * Labels puzzles as easy, medium, or hard based on solving path.
  * Acceptance: Label computed from minimal solving path using defined techniques per tier.

* **FR6 – Timer:**

  * Stopwatch visible at top; starts on first interaction; pauses/resumes with game state.
  * Acceptance: Time persists on accidental reload; displayed as mm\:ss (or hh\:mm\:ss for >1h).

* **FR7 – Pause Mode:**

  * Full-board overlay; timer stops; interactions disabled.
  * Acceptance: Board content hidden; resume restores identical state; timer does not tick while paused.

* **FR8 – Minimalist Graphics:**

  * Clean, high-contrast theme; limited palette; no long animations.
  * Acceptance: Meets WCAG AA contrast; supports system light/dark preference; grid lines do not overshoot the display area.

### Supporting Features (Nice-to-Have in MVP)

* Undo/redo, pencil marks, error toggles, new game confirmation.

---

## UX and Interaction Design

### Layout

* **Top Bar:** Left: difficulty label; Center: timer; Right: pause button.
* **Main Area:** 9×9 grid centered with **thick 3×3 block borders**, 5px margin around the grid.
* **Bottom Panel:** Digits 1–9 with remaining counts; disabled state when count hits zero; panel aligned with grid edges.

### Interactions

* Single active cell highlight; optional row/column/box shading.
* Mouse/touch: tap cell → tap digit; keyboard: arrow keys to move, numbers to place, 0/Backspace to clear, P to pause.
* Feedback: subtle flash ≤150 ms on placement; red outline on conflicts if enabled.

---

## System Behavior and Logic

* **Game States:** Idle → Playing → Paused → Completed.
* **Generator & Validator:** Generates full valid grid, removes numbers while maintaining uniqueness.
* **Difficulty Classification:** Easy → singles only; Medium → intermediate eliminations; Hard → advanced techniques (no guessing).
* **Number Panel Depletion:** Remaining = 9 − (clues + current placements); disables digit when zero.
* **Completion Detection:** Checks all constraints and grid full; optional final solver validation.

---

## Non-Functional Requirements

* Load ≤ 2 s; frame update ≤ 16 ms; generator under 800 ms for Hard.
* Autosave state every 2 seconds; determinism with seed for QA.
* No PII; local-only storage; pause disables all hints and interactions.
* Target: responsive web, semantic HTML/CSS, minimal JS overhead.

---

## Deliverables, Acceptance Criteria, and Roadmap

* **MVP:** Start puzzle, display immutable clues, place/clear numbers, number panel updates, generator produces unique puzzles, difficulty classification correct, timer and pause functional, UI accessible.
* **Future Roadmap:** Technique training mode, hints, analytics, additional themes, puzzle import/export.

---

✅ **Visual Improvements Integrated**

* Thick 3×3 block lines.
* 5px margin around grid.
* Grid lines contained within 9×9 area (no overshoot).
* Number panel aligned with grid edges.



