# Git Branches

The best practices for a simple workflow for sugesting changes to a GitHub repository are: create your own fork of the repository, make a branch from your fork where your changes are made, and then suggest these changes move to the upstream repository with a pull request. This section of the GitHub chapter assumes you have read all prior GitHub sections, are familiar with git commands and the vocabulary ("cloning," "forking," "merging," "pull request" etc), and that you have already created your own fork of the [GitHub Sandbox Repository](https://github.com/ProjectPythia/github-sandbox) hosted by Project Pythia. That fork is where you will make your first Git branch while following along with this chapter.

## Overview:

1. What are Git Branches
1. Creating a New Branch

## Prerequisites

| Concepts              | Importance | Notes |
| --------------------- | ---------- | ----- |
| Prior GitHub Sections | Necessary  |       |

- **Time to learn**: 30 minutes

---


## What are Git branches?

Git branches allow for non-linear or differing revision histories of a repository. At a point in time, you can split your repository into multiple development paths (branches) where you can make different commits in each, typically with the ultimate intention of merging these branches and development changes together at a later time.

One rule of thumb is for each development feature to have its own development branch until that feature is ready to be added to the upstream codebase. This allows you to compartmentalize your pull requests so that smaller working changes can be merged upstream independently of one another. For example, you might have a complete or near-complete feature on its own branch with an open pull request awaiting review. While you wait for feedback from the team before merging it, you can still work on a second feature on a second branch without affecting your first feature's pull request. **We encourage you to always do your work in a designated branch.**


## Creating a New Branch

From your terminal, navigate to your local clone of your `Github-Sandbox` Repository fork:
```
cd github-sandbox
```

Let's begin by checking the status of our repository:
```
git status
```

You will see that you are already on a branch called "main". And that this branch is up-to-date with "origin/main" and has nothign to commit.

Next, check all of your exising Git branches with:
```
git branch -a
```

You will see one local branch ("main") and your remote branch ("remotes/origin/HEAD" and "remotes/origin/main", where "HEAD" points to "main").

Now, before we make some sample changes to our codebase, let's create a new branch where we'll make these changes:
```
git branch newbranch
```

Check that this branch was created with:
```
git branch
```

This will display the current and the new branch. You'll notice that we are still on branch "main" and will need to switch branches to work in our "newbranch."



## Switching Branches

To switch branches use the command `git checkout` as in:
``` 
git checkout newbranch
```

To check your current branch type:
```
git status
```

Notice that `git status` doesn't say anything about being up-to-date, as beofre. This is because this branch only exists locally, not in our upstream GitHub fork.

Before we push this branch upstream, let's make some sample changes by creating a new Python file.
```
touch hello.py
```

You can check that this file has been created by comparing an `ls` before and after this command, and also with a `git status` that will show your new untracked file.


## Merging Branches

## Branch Management

## Branch Workflows

## Remote Branches

## Pushing

## Tracking Branches

## Pulling

## Deleting Branches

## Rebasing

---

## Summary

- Sum 1
- Sum 2

### What's Next?

Next lesson

## References

1. Ref 1
1. Ref 2
