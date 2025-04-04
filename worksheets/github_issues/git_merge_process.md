# Git Merging Process and Pull vs Fetch

## Git Merging Process

Merging in Git is the process of combining changes from one branch into another. It is usually done when we want to integrate new features or fixes from a feature branch into the main branch.

### Steps to Merge in Git

1. **Switch to the Branch we Want to Merge Into**: First, make sure we are on the branch we want to merge changes into (usually `main` or `master`):
```bash
git checkout main
```

2. **Pull the Latest Changes (Optional)**: It’s a good idea to pull the latest changes from the remote repository before merging:
```bash
git pull origin main
```

3. **Merge the Branch**: Now, merge the branch with the changes we want to integrate (e.g., feature-branch) into our current branch:
```bash
git merge feature-branch
```

4. **Resolve Conflicts (If Any)**: If there are merge conflicts, Git will ask us to resolve them manually. Once resolved, mark the conflicts as resolved:
```bash
git add <resolved-files>
```

5. **Commit the Merge**: After resolving conflicts, commit the merge:
```bash
git commit -m "Merge feature-branch into main"
```

6. **Push the Changes**: Finally, push the merged changes to the remote repository:
```bash
git push origin main
```

**Difference Between git pull and git fetch**
**git fetch**: This command fetches the latest changes from the remote repository but does not merge them into our local branch. It only updates the remote-tracking branches in our local repository. we can then review the changes before deciding to merge them.
```bash
git fetch origin
```

**git pull**: This command is essentially a combination of git fetch followed by git merge. It fetches the latest changes from the remote repository and automatically merges them into our current branch.
```bash
git pull origin main
```

**Summary**:
**git fetch**: Updates local references of remote branches (does not merge).
**git pull**: Fetches and merges changes from the remote repository into our current branch.