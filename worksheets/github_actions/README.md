# 🎲 Yatzy Game in Python

This is a Python implementation of the classic **Yatzy** dice game. It includes all the core logic for rolling dice, locking them, and calculating scores based on the official rules of the game.

---

## 📌 Features

- Roll and lock dice (5 total)
- Score categories:
  - Ones to Sixes
  - One Pair, Two Pairs
  - Three of a Kind, Four of a Kind
  - Small Straight, Large Straight
  - Full House
  - Chance
  - Yatzy (five of a kind)
- Fully tested with unit tests

---

## 📂 Project Structure

```
github_actions/
└── Yatzy.py              # Main Yatzy class with game logic
└── test_yatzy.py         # Unit tests covering all methods
.github/
└── workflows/
    └── python-ci.yml     # GitHub Actions for CI

README.md                 # Project description and CI details
```

---

## 🧪 Running the Tests Locally

Make sure you have Python 3.11 or above installed.

```bash
# Navigate to the root of the project
cd portfolio/worksheets/github_actions

# Run all unit tests
python -m unittest discover -s tests -p "test_*.py"
```

---

## ⚙️ GitHub Actions CI

This project uses **GitHub Actions** to automatically test your code on every push or pull request — except when only `README.md` is changed.

### 🔧 What It Does

- Installs Python 3.11
- Installs any dependencies (from `requirements.txt`, if present)
- Runs all unit tests using `unittest`

### 📄 Workflow File Location

```
.github/workflows/yatzy-ci-pipeline.yaml
```

---

## ✅ Requirements

- Python 3.11+
- No third-party libraries required (uses only built-in Python modules)

---

## 📌 Notes

- The game logic is ready for expansion (e.g., multiplayer, UI).
- All scoring functions follow standard Yatzy rules.
- Full unit test coverage ensures everything works correctly.

---
