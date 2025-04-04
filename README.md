# Open Source Development Portfolio

This repository contains my submission for the **Open Source Development** module coursework at Coventry University. The project demonstrates proficiency in version control (Git/GitHub), automated testing (GitHub Actions), and collaboration using GitHub Issues. It also includes an essay on open-source development.

## Project Overview

### 1. Yatzy Game Class (Python)
A simplified implementation of the Yatzy dice game, featuring:
- A `Yatzy` class with 5 lockable dice.
- Methods for scoring combinations (e.g., `Ones()`, `FullHouse()`).
- Unit tests and a mock game demonstration.
- Automated testing via GitHub Actions.

### 2. Version Control & Collaboration
- Git workflows (`branch`, `commit`, `pull`, etc.).
- Issue tracking and fixes with a peer reviewer.

### 3. Open Source Essay
A 1500-word reflection on open-source development's relevance to my academic/career goals.

---

## Folder Structure
```
portfolio/
├── .github/workflows
│   └── yatzy-ci-pipeline.yml # GitHub Actions workflow for testing/docs
├── worksheets/
│   ├── version_control/
│   │   ├── README.md                 # Demonstration of Git commands used
│   │   ├── git_commands.md           # Logs of Git commands
│   │   └── screenshots/              # Images showing Git actions (e.g., commits, branches)
│   ├── project/
│   │   ├── Yatzy.py                  # Python class `Yatzy` with all required methods
│   │   ├── test_yatzy.py             # Unit tests for all methods
│   │   ├── game_mockup.py            # Mock Yatzy game demonstration
│   │   └── README.md                 # Explanation of the implementation
│   └── github_issues/
│       ├── issue_report.md           # Documentation of issues raised and fixed
│       ├── screenshots/              # Images of GitHub Issues and PRs
│       └── README.md                 # Summary of collaboration process
└── essay/
    ├── KOL389COM-OSD-ESSAY.docx       # Essay in Word format
    └── KOL389COM-OSD-ESSAY.pdf        # Essay in PDF format
```


---

## How to Use

### Yatzy Class
1. Navigate to `worksheets/project/`.
2. Run `python game_mockup.py` to see a demo.
3. Tests can be executed via `python test_yatzy.py` or GitHub Actions.

### Git Examples
- See `version_control/git_commands.md` for documented Git workflows.

### Issues & Fixes
- Review `github_issues/issues_report.md` for collaboration details.

---

## Dependencies
- Python 3.x
- `pytest` (for running tests locally)