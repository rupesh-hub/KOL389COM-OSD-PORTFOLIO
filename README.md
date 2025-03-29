# README.md

## Portfolio Overview
This portfolio contains all required materials for the coursework, organized into three main categories:
1. **Version Control** – Demonstrates proper use of Git and GitHub.
2. **GitHub Actions** – Implements automation for testing and documentation.
3. **GitHub Issues** – Documents issue tracking and resolution through collaboration.

## Folder Structure
```
portfolio/  
│── worksheets/  
│   ├── version_control/  
│   │   ├── version_control_notes.pdf  # Explanation of Git workflow  
│   │   ├── git_commands_examples.png  # Screenshot of Git commands in use  
│   │   ├── git_workflow_steps.txt  # Step-by-step Git process  
│   │   ├── git_branching_example.png  # Diagram of branching strategy  
│   ├── github_actions/  
│   │   ├── yatzy.py  # The main Yatzy class  
│   │   ├── test_yatzy.py  # Unit tests for the Yatzy class  
│   │   ├── game_mockup.py  # A simple script to simulate a game  
│   │   ├── .github/  
│   │   │   ├── workflows/  
│   │   │   │   ├── test.yml  # GitHub Actions for running tests  
│   │   │   │   ├── documentation.yml  # GitHub Actions for generating docs  
│   │   ├── github_actions_notes.pdf  # Explanation of automation setup  
│   │   ├── yatzy_class_diagram.png  # UML diagram of the class structure  
│   │   ├── test_results_screenshot.png  # Screenshot of test results  
│   ├── github_issues/  
│   │   ├── issues_report.pdf  # Report of issues found and fixed  
│   │   ├── fixed_issue_screenshot.png  # Screenshot of a resolved issue  
│   │   ├── git_merge_process.txt  # Steps on merging the fixed code  
│   │   ├── collaboration_notes.pdf  # Notes on working with a peer  
│  
│── README.md  # Overview of the portfolio and how to navigate  
│── submission_notes.txt  # Any additional notes for the instructor  
```

Each section contains notes, screenshots, and supporting documents.

---

# submission_notes.txt

## Submission Notes
- Ensure that all files are well-organized within the `portfolio` directory.
- The `version_control` section provides evidence of correct Git usage.
- The `github_actions` section includes the full `Yatzy` class, tests, and GitHub Actions configuration.
- The `github_issues` section documents issue tracking and collaboration.
- All documents are provided in `.pdf` format where necessary.
- Screenshots are in `.png` format for clarity.

---

# version_control_notes.pdf (Content Sample)

## Using Git and GitHub for Version Control
### Key Commands and Workflow
1. **Cloning a Repository**  
   ```bash
   git clone https://github.com/user/repository.git
   ```
2. **Creating a New Branch**  
   ```bash
   git checkout -b feature-branch
   ```
3. **Adding and Committing Changes**  
   ```bash
   git add .
   git commit -m "Added new feature"
   ```
4. **Pushing and Merging**  
   ```bash
   git push origin feature-branch
   git checkout main
   git merge feature-branch
   ```

---

# github_actions_notes.pdf (Content Sample)

## Automating Tests and Documentation with GitHub Actions
### Workflow Configuration
A `.github/workflows/test.yml` file is included to automate testing:
```yaml
name: Run Tests
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.8'
      - name: Install Dependencies
        run: pip install -r requirements.txt
      - name: Run Tests
        run: pytest
```
### Benefits
- Ensures code quality with automated testing.
- Generates documentation automatically.

---

# issues_report.pdf (Content Sample)

## Issue Tracking and Collaboration
### Reported Issues
| Issue ID | Description | Status |
|----------|------------|--------|
| #1 | Bug in `Yatzy.ones()` returning incorrect score | Fixed |
| #2 | Dice locking mechanism not working | Fixed |

### Fixing Issues
- Peer-reviewed code and identified the problem.
- Pushed a fix on a separate branch and merged after testing.
- Documented changes in the issue tracker.

---

This sample content ensures clarity, documentation, and professional presentation of the portfolio.

