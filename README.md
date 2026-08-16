# MyVideoGameList 🎮

A modern, fast, and elegant desktop application to manage your video game library across different platforms (Steam, Epic Games, GOG, etc.). Built with Python and `customtkinter`.

## ✨ Features

- **Dark Mode UI**: A beautiful, modern interface with Deep Purple & Indigo accents.
- **Saga Management**: Group your games by sagas/franchises (e.g., The Witcher, Assassin's Creed).
- **Game Tracking**: Track the status of your games (Not Started, Playing, Finished, Dropped).
- **Smart Filtering**: Instantly search for games by name.
- **Sorting**: Click on column headers to sort by Name or Release Date.
- **Local Storage**: All data is securely saved in a local SQLite database.

## 🏗️ Architecture

This project follows strict professional conventions:
- **Language**: 100% English codebase.
- **Pattern**: Strict MVC (Model-View-Controller) architecture.
- **Layout**: Standard Python `src/` layout for secure packaging.
- **Dependency Management**: Powered by [uv](https://github.com/astral-sh/uv) for lightning-fast environment resolution.

## 🚀 Getting Started

### Prerequisites

You will need to have [Python 3.13+](https://www.python.org/) and `uv` installed.
To install `uv`:
```bash
pip install uv
```

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Rodriguou/myvideogamelist.git
cd myvideogamelist
```

2. Let `uv` handle the virtual environment and dependencies automatically:
```bash
uv sync
```

### Usage

Run the application with a single command from the project root:
```bash
uv run myvideogamelist
```
*Note: The local SQLite database (`myvideogamelist.db`) will be automatically generated upon the first run.*

## 📄 License
This project is open-source and available under the MIT License.
