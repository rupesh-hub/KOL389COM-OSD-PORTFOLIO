# Yatzy Game

## Version Control

Version control helps manage changes to the project and tracks the history of our code. It is essential for collaboration and maintaining different versions of our project.

This project uses **Git** for version control.

### How to Use Version Control in this Project

1. **Initialize Git**: Start by initializing a Git repository in our project directory:
```bash
git init
```
2. **Track Changes**: After making changes to the project files, we use the following command to see what’s changed:
```bash
git status
```

3. **Stage Changes**: Add files to the staging area to track them:
```bash
git add <filename>
```

Or stage all modified files:
```bash
git add .
```

4. **Commit Changes**: Once our changes are staged, commit them to our local repository:
```bash
git commit -m "Description of changes"
```

5. **View History**: We can view the commit history using:
```bash
git log
```

6. **Push Changes (Optional)**: If we're using a remote repository like GitHub, we can push our changes to it:
```bash
git push origin main
```

**Why Version Control?**
a. **Track Changes**: We can see what changes were made and by whom.

b. **Collaboration**: Multiple people can work on the project without conflicting with each other's work.

c. **Revert Changes**: If something goes wrong, we can go back to a previous version of the project.



