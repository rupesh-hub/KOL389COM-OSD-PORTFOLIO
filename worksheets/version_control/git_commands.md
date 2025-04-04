### Git Command Workflow for Yatzy Project (Step-by-Step)

1. **Set global Git configuration (only once per machine)**
```bash
git config --global user.name "Rupesh Dulal"
git config --global user.email "<EMAIL>"
```
This sets our Git identity, so our commits are properly attributed.

2. **Initialize a Git repository**
```bash
git init
```
Initializes a new local Git repository in our project folder.

3. **Create a new repository on GitHub**
(Do this via the GitHub website: https://github.com/new)
Give it a name (e.g., `KOL389COM-OSD-PORTFOLIO`) and choose visibility (public or private).

4. **Add the remote origin**
```bash
git remote add origin git@github.com:rupesh-hub/KOL389COM-OSD-PORTFOLIO.git
```
Connects our local repo to the remote repository on GitHub.

5. **Check the remote**
```bash
git remote -v
```
Verifies that our remote repository is set correctly.

6. **Add all files to staging**
```bash
git add .
```
Stages all the files (code, tests, README, CI) for the initial commit.

7. **Commit our changes**
```bash
git commit -m "Initial commit with Yatzy game and tests"
```
Commits our staged files with a descriptive message.

8. **Push to GitHub (first time)**
```bash
git push -u origin main
```
Pushes our local code to the `main` branch of our remote repo and sets upstream.

9. **Create a new branch (optional)**
```bash
git checkout -b feature/ci-workflow
```
Creates a new branch for specific features like adding CI without affecting main.

10. **Make changes and track them**
```bash
git status
```
Shows modified, new, and deleted files that are not committed yet.

11. **Add and commit updated files**
```bash
git add filename.py
```
```bash
git commit -m "Add scoring logic for full house"
```
Stages and commits specific file changes.

12. **Push our feature branch**
```bash
git push origin feature/ci-workflow
```
Pushes the feature branch to the remote repo.

13. **Create a pull request (PR)**
Do this via GitHub UI to merge `feature/ci-workflow` into `main`.

14. **Pull the latest changes**
```bash
git pull origin main
```
Updates our local main branch with the latest code from GitHub.

15. **Merge feature branch into main (if working locally)**
```bash
git checkout main
```
```bash
git merge feature/ci-workflow
```
Combines the feature branch into main locally.

16. **Delete merged branch**
```bash
git branch -d feature/ci-workflow
```
Deletes the feature branch locally after merge.

17. **Push final changes to GitHub**
```bash
git push origin main
```
Pushes the latest `main` branch with all merged code to the remote.

18. **Ignore specific files**
Create a `.gitignore` file and add entries like:
```
__pycache__/
*.pyc
.env
```
This tells Git to ignore unnecessary files and directories.

19. **Check Git log/history**
```bash
git log --oneline
```
Shows commit history in a concise format.

20. **Clone the repo (if working on another machine)**
```bash
git clone https://github.com/rupesh-hub/KOL389COM-OSD-PORTFOLIO.git
```
Creates a local copy of the repository.

21. **Fetch all remote branches**
```bash
git fetch --all
```
Retrieves latest branch data from GitHub without modifying our working directory.

---