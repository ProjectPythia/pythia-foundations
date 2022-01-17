# Basic version control with git

```{note}
This content is under construction!
```

## Overview:

1. Overview 1
1. Overview 2

## Prerequisites

| Concepts              | Importance | Notes |
| --------------------- | ---------- | ----- |
| Prior GitHub Sections | Necessary  |       |

- **Time to learn**: 30 minutes

---

## What is version control (and why should we care)?

### git: some definitions and history

## Inspect a git repository with `git status`

First, make sure you followed the steps in the [Cloning a repository](https://foundations.projectpythia.org/foundations/github/github-cloning-forking.html) lesson to make a clone of the `github-sandbox` repo on your local computer.

Navigate to wherever you saved your copy of the repo. Remember, when you made the clone, you got a complete, independent copy of everything in the repo. So don't worry about breaking anything!

Your new best friend is

```bash
git status
```

which will always give you information about the current git repo. Try it! You should see something like this:

```bash
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

Two really important things here:

1. The first line show you the current _branch_ (here called `main`). We'll cover branching in more detail in the next lesson, but basically each branch is a completely independent version. When we start making changes to files, we'll have to pay attention to which branch we're currently on.
1. The last line `nothing to commit, working tree clean` tells us that we haven't made any changes to files.

You'll want to use

```bash
git status
```

frequently to keep track of things.

## Make some changes

- Create a new branch, warn reader to avoid working on `main` branch most of the time because it makes collaboration trickier
- Don't go into any detail about branching, just give a working example to follow.
- `git status` after checking out different branch
- Edit a file
- `git status` now shows something different

Now we're at the stage where we've _saved some changes_ to one or more files in the repo, but we haven't yet told git to keep track of those changes.

The next step is to add our changes to the "official" history of our repo. This is a two-step process (staging and committing).

## Stage and commit our changes

```bash
git add myfile
```

```bash
git commit -m 'commit message'
```

Now when we do `git status` we see...

We have now added a new permanent change to the history of our repo.

## Going back in time

Look at the history of the branch with

```bash
git log
```

Checkout a previous version with

```
git checkout <commit number>
```

## Comparing versions

Some examples of `git diff` across commits with a branch, and between branches.

## Creating a new repository

It's as simple as doing

```
git init
```

which turns the current working directory into a git repo (if you're not already in one).

... Elaborate, quick example of creating a new repo, adding a file, staging, committing.

---

## Summary

- Sum 1
- Sum 2

### What's Next?

Next we'll explore the concept of branching in git repositories in more detail.

## References

1. [Official git documentation](https://git-scm.com/doc)
1. [The Software Carpentries beginner lessons on git](https://swcarpentry.github.io/git-novice/)
