# Sudoku practice game PRD

## Overview

A minimalist Sudoku game designed to help players practice and master solving techniques. The MVP delivers a clean grid, a number panel that reflects remaining digits, a solvable puzzle generator with difficulty classification, a timer, and a pause mode that hides the board to discourage peeking. Future iterations will add technique-driven training, guided hints, and analytics.

---

## Goals and non-goals

- **Primary goal:** Provide a fast, clean Sudoku experience that reinforces solving discipline and time-on-task.
- **Secondary goal:** Ensure every generated puzzle is uniquely solvable and correctly labeled easy, medium, or hard.
- **Non-goals (MVP):** Social features, daily leaderboards, accounts, cloud save, advanced theme customization, adaptive tutoring, and non-9×9 variants.

---

## User stories and success metrics

### User stories

- **US1 – Start:** As a player, I want to start a new puzzle with a chosen difficulty so I can practice at my level.
- **US2 – Place numbers:** As a player, I want to place numbers on a grid and see conflicts so I can correct mistakes early.
- **US3 – Remaining digits:** As a player, I want a number panel that grays out digits once all nine are placed so I can pace my choices.
- **US4 – Timer:** As a player, I want a timer that tracks my session so I can measure improvement.
- **US5 – Pause:** As a player, I want to pause the game and hide the board so I can take a break without temptation.
- **US6 – Difficulty clarity:** As a player, I want puzzles that truly match easy/medium/hard so I can train effectively.
- **US7 – Reliability:** As a player, I want puzzles to be solvable with a unique solution so I don’t waste time on broken boards.

### Success metrics

- **Completion rate:** ≥ 80% of started puzzles are completed by players who spend ≥ 3 minutes.
- **Difficulty accuracy:** ≥ 90% player agreement that labeled difficulty matches experience (post-game thumbs up/down).
- **Performance:** Initial load under 2 seconds on midrange mobile; interactions under 16 ms frame budget.
- **Fair play:** 0 known cases of non-unique or unsolvable boards in production telemetry.

---

## Functional requirements

### Core gameplay

- **FR1 – Grid:**
  - A 9×9 grid with 3×3 subgrids, showing given clues and empty cells for inputs.
  - **Acceptance:** Clues are non-editable; user inputs are editable; row/column/subgrid boundaries are visually distinct.

- **FR2 – Number placement:**
  - Tap/click a cell, then tap a digit 1–9 to place; second tap on the same digit removes it.
  - **Acceptance:** Placement blocked for clue cells; optional conflict highlighting (toggleable) indicates row/column/box violations.

- **FR3 – Number panel with depletion:**
  - Panel shows digits 1–9; each displays remaining count (9 minus placements and clues).
  - When remaining count reaches 0, the digit becomes disabled and grayed out.
  - **Acceptance:** Counts update in real time for placements and removals; no placement allowed for disabled digits.

- **FR4 – Puzzle generator:**
  - Generates valid 9×9 puzzles with a unique solution.
  - **Acceptance:** Every generated puzzle passes a solver uniqueness check; no multiple solutions; no contradictions.

- **FR5 – Difficulty classification:**
  - Generator assigns easy, medium, or hard label.
  - **Acceptance:** Label computed from the minimal solving path using defined techniques per tier (below).

- **FR6 – Timer:**
  - Stopwatch visible at the top; starts on first interaction; pauses/resumes with game state; stops on completion.
  - **Acceptance:** Time persists on accidental reload within session storage; displayed as mm:ss (or hh:mm:ss over 1 hour).

- **FR7 – Pause mode with cover:**
  - Pause button halts the timer and overlays a full-board cover; interactions are disabled until resume.
  - **Acceptance:** No board content visible while paused; resume returns to identical state; timer does not tick during pause.

- **FR8 – Minimalist graphics:**
  - Clean, high-contrast theme; limited color palette; no animations longer than 150 ms.
  - **Acceptance:** Meets WCAG AA contrast; supports system light/dark preference.

### Supporting features (nice-to-have in MVP if low effort)

- **FR9 – Undo/redo:**
  - Stepwise undo/redo for placements and removals.
- **FR10 – Pencil marks:**
  - Note mode for candidates; clear candidates on confirmed placement (optional).
- **FR11 – Error toggles:**
  - Toggle to enable/disable immediate conflict highlights.
- **FR12 – New game:**
  - Start new puzzle with chosen difficulty; confirm if current puzzle not completed.

---

## UX and interaction design

### Layout

- **Top bar:** Left: difficulty label; Center: timer; Right: pause button.
- **Main area:** 9×9 grid centered, responsive to viewport; cell size scales with device; thick borders for 3×3 boxes.
- **Bottom/side panel:** Digits 1–9 with remaining counts; disabled state when count hits zero.

### Interactions

- **Selection model:** Single active cell with highlight; row/column/box shading optional; identical-number highlighting optional.
- **Input methods:**
  - **Mouse/touch:** Tap cell → tap digit; long-press digit toggles note mode (if implemented).
  - **Keyboard:** Arrow keys to move; number keys 1–9 to place; 0/Backspace to clear; P to pause; T to toggle note mode.
- **Feedback:**
  - **Placement feedback:** Subtle cell flash (≤150 ms); updated remaining count.
  - **Conflict feedback (if enabled):** Red outline on conflicting cells; non-blocking.

### Accessibility

- **Screen reader labels:** Each cell announces position (e.g., “Row 3, Column 7, value 5, given” or “empty”).
- **Color independence:** Patterns or outlines convey state in addition to color.
- **Keyboard-only play:** Fully operable without a mouse.
- **Touch targets:** Minimum 44×44 px on mobile.

---

## System behavior and logic

### Game states

- **States:** Idle → Playing → Paused → Completed.
- **Transitions:**
  - **Idle → Playing:** First user interaction or explicit “Start.”
  - **Playing → Paused:** Pause button; timer stops; board covered.
  - **Paused → Playing:** Resume; timer restarts.
  - **Playing → Completed:** All cells filled and constraints satisfied (unique solution achieved); timer stops; end-screen shown.

### Generator and validator

- **Uniqueness check:** Backtracking solver with constraint propagation confirms exactly one solution.
- **Generation approach:** Create a full valid grid, then remove clues while preserving uniqueness and target difficulty.
- **Clue count bounds:** Not strictly fixed; governed by difficulty technique set and branching factor rather than a hard minimum.

### Difficulty classification rubric

- **Easy:** Solvable using only singles.
  - Allowed: Naked Singles, Hidden Singles.
- **Medium:** Requires intermediate eliminations.
  - Allowed: All Easy plus Naked Pairs/Triples, Hidden Pairs/Triples, Pointing Pairs/Triples, Box-Line Reduction.
- **Hard:** Requires advanced strategies but avoids guessing.
  - Allowed: All Medium plus X-Wing, Swordfish, Simple Coloring, XY-Wing. (No trial-and-error.)

Classification is based on the highest-level technique required along an optimal solving path. If multiple paths exist, choose the minimal-difficulty path. If any step requires beyond Hard (e.g., guessing), discard or regenerate.

### Timer and pause specifics

- **Start logic:** Timer starts on first placement or explicit “Start.”
- **Persistence:** Time and board state saved to local/session storage every 2 seconds and on significant actions.
- **Anti-cheat pause:** Full opaque overlay; numbers and notes not visible; disable all inputs; no incremental hints available.

### Number panel depletion logic

- **Remaining count:** For each digit d, remaining = 9 − (clues with d + current placements of d).
- **Disable rule:** When remaining == 0, disable and gray out the digit; prevent placement via UI and keyboard.

### Completion detection

- **Validation:** On every placement, check:
  - Row/column/box constraints satisfied.
  - Grid is full.
  - Optional: Final validation by solver for robustness before completion screen.

---

## Non-functional requirements and constraints

### Performance

- **Load time:** ≤ 2 s on 3G-equivalent; JS bundle under 200 KB gzipped for MVP if web-based.
- **Interaction:** ≤ 16 ms per frame updates; generator completes under 300 ms for Easy/Medium and under 800 ms for Hard on midrange devices (or done off-main-thread).

### Reliability

- **State safety:** Autosave prevents loss on reload/crash within the same session.
- **Determinism:** Given a fixed seed, generator returns identical puzzle (for QA reproducibility).

### Security and privacy

- **Data:** No PII collection in MVP; local-only storage for state and settings.
- **Cheating prevention:** No hint leakage during pause; no exposed internal solution in production builds.

### Platforms and tech constraints

- **Target platforms:** Responsive web (mobile and desktop). Native ports considered later.
- **Rendering:** Semantic HTML/CSS with accessible ARIA roles; minimal JS framework overhead.

---

## Deliverables, acceptance criteria, and future roadmap

### MVP acceptance criteria

- **AC1:** Start a new puzzle in Easy/Medium/Hard; show difficulty label.
- **AC2:** Grid displays immutable clues; user can place and clear numbers in empty cells.
- **AC3:** Number panel shows remaining counts; digits gray out and disable at zero remaining.
- **AC4:** Generator produces puzzles with unique solutions; validator confirms uniqueness.
- **AC5:** Difficulty classification aligns with rubric; internal solver log includes the highest technique used.
- **AC6:** Timer starts/stops appropriately; persists through reload within a session; does not tick while paused.
- **AC7:** Pause overlays the grid fully and disables all interactions until resume.
- **AC8:** UI adheres to minimalist, high-contrast design and passes accessibility checks for keyboard navigation and contrast.

### QA test scenarios (sample)

- **Scenario – Depletion:** Fill all nines; panel “9” grays out and is non-interactive.
- **Scenario – Pause integrity:** Place a few numbers, pause, verify no content visible; resume and verify state/time unchanged.
- **Scenario – Uniqueness:** Randomly sample 100 generated puzzles per difficulty; solver confirms exactly one solution.
- **Scenario – Difficulty sanity:** For each difficulty, solver log shows no technique beyond the tier; reject outliers.

### Future roadmap (post-MVP)

- **Technique training mode:** Curated puzzles per technique with guided hints explaining the exact move.
- **Step-by-step hints:** Explain the next logical step and name the technique used.
- **Analytics:** Personal bests per difficulty; streaks; time distributions.
- **Themes:** Additional minimalist themes; colorblind-safe palettes.
- **Exports/imports:** Share/import puzzles via compact codes; seed inputs.

---

## Notes for implementation (LLM-generated code context)

- **Clarity of contracts:** Specify interfaces for Generator, Solver, Classifier, and Store to keep modules decoupled and testable.
- **Seeded randomness:** Expose a seed parameter for reproducibility in QA and user-shared puzzles.
- **Technique-first solver:** Implement a rule-based solver that logs the highest technique used; use that log to classify difficulty.
- **Background work:** Run generation and solving off the main thread (e.g., Web Worker) to keep UI responsive.
- **Telemetry hooks (optional):** Lightweight event hooks for start, pause, resume, complete, and abandon—disabled by default in MVP.