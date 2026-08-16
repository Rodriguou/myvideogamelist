# Project Conventions: MyVideoGameList

This file contains the rules and conventions that AI agents must follow when working on this project.

## 1. Language Convention
- **Strictly English:** All source code, variable names, function names, class names, docstrings, inline comments, and database schemas (tables, columns) MUST be written entirely in English.
- *Note:* Communication with the user (chat, explanations) should remain in the user's preferred language (Portuguese), but the codebase itself is 100% English.

## 2. Architecture & Design Pattern
- **MVC (Model-View-Controller):** The project must strictly adhere to the MVC pattern.
  - `models/`: Exclusively for SQLite database connections and CRUD operations. No UI code here.
  - `views/`: Exclusively for CustomTkinter UI rendering. No direct database queries here.
  - `controllers/`: The glue that handles events from the view and calls the models.

## 3. UI / Aesthetics
- **Library:** `CustomTkinter`.
- **Theme:** Dark Mode.
- **Palette:** Deep Purple / Indigo (`#6200EE`, `#3700B3` for buttons and highlights) over dark gray backgrounds (`#121212`, `#1E1E1E`).

## 4. Git & Commits
- **Semantic Commits:** All commit messages MUST follow the semantic convention (e.g., `feat:`, `chore:`, `fix:`, `refactor:`, `docs:`).
- **Commit Language:** Commit messages MUST be written in **English** (e.g., `feat: add search functionality to main view`).
- **Workflow:** Always work on feature branches (e.g., `feature/nome-da-feature`) and avoid committing directly to the `main` branch.
