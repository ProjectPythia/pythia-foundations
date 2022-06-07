```{image} ../../images/Git-Logo-2Color.png
:alt: Git Logo
:width: 400px
```

# Basic Version Control with _git_

## Overview:

1. The need for version control
1. Basic git usage
1. Making your first git commit
1. Viewing and comparing across the commit history

## Prerequisites

| Concepts                                                   | Importance  | Notes                        |
| ---------------------------------------------------------- | ----------- | ---------------------------- |
| [What is GitHub?](what-is-github)                          | Necessary   | GitHub user account required |
| [GitHub Repositories](github-repos)                        | Necessary   |                              |
| [Issues and Discussions](github-issues)                    | Recommended |                              |
| [Cloning and Forking a Repository](github-cloning-forking) | Recommended |                              |
| [Configuring your GitHub Account](github-setup-advanced)   | Recommended |                              |

- **Time to learn**: 45 minutes

---

## About version control and git

### What is version control (and why should we care)?

[Version Control](https://en.wikipedia.org/wiki/Version_control) refers generally to systems for managing changes to documents or files. Version control systems let us keep track of what changes were made to a file, when they were made, and by whom. If you've ever used "Tracked changes" on a Word document with multiple authors, then you've seen a form of version control in action (though NOT one that is well suited to working with computer code!).

The need for version control is particularly acute when _working with computer code_, where small changes to the text can have huge impacts on the results of running the code.

Do you have a directory somewhere on your machine right now with five different versions of a Python script like this?

```
analysis_script_OLD.py
analysis_script.py
analysis_script_09122021.py
analysis_script_09122021_edit.py
analysis_script_NEW.py
```

A Version Control System (VCS) like git will replace this mess with a _well-ordered and labelled history_ of edits that you can freely browse through, and will greatly simply collaborating with other people on writing new code.

### What is git?

#### Git is not GitHub

That's the first thing to understand. GitHub is a web-based platform for hosting code and collaborating with other people. On the other hand, **git is a command-line Version Control System (VCS)** that you can download and install. It runs on your local computer as well as under the hood on GitHub. You need to understand something about version control with git in order to use many of GitHub's collaboration features.

#### A little history and nomenclature

Git has been around [since the mid-2000s](https://en.wikipedia.org/wiki/Git). It was originally written by Linus Torvalds specifically for use in development of the Linux kernel. Git is [FOSS](https://foundations.projectpythia.org/foundations/github/what-is-github.html#free-and-open-source-software-foss) and comes pre-installed on many Linux and Mac OS systems.

There are many other VCSs out there. A few that you might encounter in scientific codebases include [Subversion](https://subversion.apache.org), [Mercurial](https://www.mercurial-scm.org), and [CVS](http://cvs.nongnu.org). However, git is overwhelmingly the VCS of choice for open-source projects in the Scientific Python ecosystem these days (as well as among software developers more generally).

There is no universally agreed-upon meaning of the name "git". From the [git project's own README file](https://github.com/git/git/blob/master/README.md):

> The name "git" was given by Linus Torvalds when he wrote the very first version. He described the tool as "the stupid content tracker" and the name as (depending on your mood):
>
> - random three-letter combination that is pronounceable, and not actually used by any common UNIX command. The fact that it is a mispronunciation of "get" may or may not be relevant.
> - stupid. contemptible and despicable. simple. Take your pick from the dictionary of slang.
> - "global information tracker": you're in a good mood, and it actually works for you. Angels sing, and a light suddenly fills the room.
> - "goddamn idiotic truckload of sh\*t": when it breaks

#### Git is a distributed VCS

Aside from being free and widely deployed, an important distinguishing feature of git is that it is a distributed Version Control System. Essentially this means that every git directory on every computer is a complete independent repository with complete history.

When we cloned the [`github-sandbox`](https://github.com/ProjectPythia/github-sandbox) repository back in the [Cloning and Forking](github-cloning-forking) section, we not only copied the current repository files but also the entire revision history of the repo.

In this section we are going to explore basic git usage _on our local computer_. Nothing that we do here is going to affect other copies of the repositories stored elsewhere. _So don't worry about breaking anything!_

Later, we will explore how to collaborate on code repositories using GitHub. But in keep in mind the basic idea that _all git repos are equal and independent_! You will have separate copies of repos stored on your local machine and in your GitHub organization.

Now that we are oriented, let's dive into some basic git usage with the [`github-sandbox`](https://github.com/ProjectPythia/github-sandbox) repository!

## Inspect a git repository with `git status`

First, make sure you followed the steps in the [Cloning a repository](github-cloning-forking) lesson to make a clone of the `github-sandbox` repo on your local computer. Navigate to wherever you saved your copy of the repo.

Now meet your new best friend:

```bash
git status
```

which will always give you information about the current git repo. Try it! You should see something like this:

```bash
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

**Two really important things here**:

1. The first line show you the current _branch_ (here called `main`). We'll cover branching in more detail in the [next lesson](git-branches), but basically each branch is a completely independent version with its own history. When we start making changes to files, we'll have to pay attention to which branch we're currently on.
1. The last line `nothing to commit, working tree clean` tells us that we haven't made any changes to files.

You'll want to use

```bash
git status
```

frequently to keep track of things in your repos.

## Make some changes

Version control is all about keeping track of changes made to files. So let's make some changes!

You may have noticed that the file `sample.txt` in the `github-sandbox` repository contains a typo. Here we're going to fix the error and save it locally.

### Create a new feature branch

Before we start editing files, the first thing to do is to _create a new branch_ where we can safely make any changes we want.

```{tip}
While there's nothing stopping us from making changes directly to the `main` branch, it's often best to avoid this! The reason is that it makes collaboration trickier. See the [lesson on Pull Requests](github-pull-request).
```

Let's create and checkout a new branch in one line:

```bash
git checkout -b fix-typo
```

Now try your new best friend again:

```bash
git status
```

You should see something like this:

```bash
On branch fix-typo
nothing to commit, working tree clean
```

This tells us that we have switched over to a new branch called `fix-typo`, but there are not (yet) any changes to the files in the repo.

### Time to make some changes

Now do the following:

- Using your favorite text editor, open the file `github-sandbox/sample.txt`.
- Replace the word `Fxing` with the much more satisfying `Fixing`.
- Save the changes.
- Revisit your new best friend `git status`. It should now show something like this:

```bash
On branch fix-typo
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   sample.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

Here `git` is telling us that the file `sample.txt` does _not_ match what's in the repository.

Of course we know what changed in that file because we just finished editing it. But here's a quick and easy way to see the changes:

```bash
git diff
```

which should show you something like this:

```bash
diff --git a/sample.txt b/sample.txt
index 4bc074c..edc31c0 100644
--- a/sample.txt
+++ b/sample.txt
@@ -4,6 +4,6 @@ We can use it to demonstrate making pull requests or raising issues in a GitHub

 One good way to contribute to a project is to make additions and/or edits to documentation!

-Fxing something as simple as a typo is a great way to get started as a contributor!
+Fixing something as simple as a typo is a great way to get started as a contributor!

 Or, consider adding some more content to this file.
```

We can see here that `git diff` finds the line(s) where our current file differs from what's in the repo, along with a few lines before and after for context.

The next step is to add our changes to the "official" history of our repo. This is a two-step process (staging and committing).

## Stage and commit our changes

The `commit` is the centerpiece of the git workflow. Each commit is a specific set of changes, additions, and/or deletions of files that gets added to the official history of the repository.

### Staging

Before we make a commit, we must first stage our changes. Think of staging simply as "getting ready to commit". The two-step process can help avoid accidentally committing something that wasn't ready.

To stage our changes, we use `git add` like this:

```bash
git add sample.txt
```

and now our new best friend tells us

```bash
On branch fix-typo
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
	modified:   sample.txt

```

Now we see that all-important line `Changes to be committed`, telling us the contents of our staging area.

If you made a mistake (e.g., staged the wrong file), you can always unstage using `git restore` as shown in the `git status` output. Nothing is permanent until we commit!

(And if you accidentally commit the wrong thing? Don't worry, you can always "go back in time" to previous commits -- see below!)

### Committing

It's time to make a commitment. We can now permanently add our edit to the history of our `fix-typo` branch by doing this:

```bash
git commit -m 'Fix the typo'
```

```{note}
Every commit should have a "message" that explains briefly what the commit is for. Here we set the commit message with the `-m` flag and chose some descriptive text. Note, it's critical to have those quotes around `'Fix the typo'`. Otherwise the command shell will misinterpret what you are trying to do.
```

Now when we do `git status` we see

```bash
On branch fix-typo
nothing to commit, working tree clean
```

And we're back to a clean state! We have now added a new permanent change to the history of our repo (or more specifically, to this _branch_ of the repo).

## Going back in time

Each commit is essentially a snapshot in time of the state of the repo. So how can we look back on that history, or revert back to a previous version of a file?

### Viewing the commit history with `git log`

A simple way to see this history of the current branch is this:

```bash
git log
```

You'll see something like this:

```bash
commit 7dca0292467e4bbd73643556f83fd1c52b5c113c (HEAD -> fix-typo)
Author: Brian Rose <brose@albany.edu>
Date:   Mon Jan 17 11:31:49 2022 -0500

    Fix the typo

commit 35fcbd991f911e170df550db58f74a082ba18b50 (origin/main, origin/HEAD, main)
Author: Kevin Tyle <ktyle@albany.edu>
Date:   Thu Jan 13 11:29:40 2022 -0500

    Close docstring quote on sample.py

commit e56ea58071f150ec00904a50341a672456cbcb8f
Author: Kevin Tyle <ktyle@albany.edu>
Date:   Tue Jan 11 14:15:31 2022 -0500

    Create sample.md

commit f98d05e312d19a84b74c45402a2904ab94d86e45
Author: Kevin Tyle <ktyle@albany.edu>
Date:   Tue Jan 11 13:58:09 2022 -0500

    Create sample.py
```

which shows the last few commits on this branch, including the commit number, author, timestamp, and commit message. You can page down to see the rest of the history
or just press `Q` to exit `git log`!

```{note}
Every commit has a unique hexadecimal checksum code like `7dca0292467e4bbd73643556f83fd1c52b5c113c`. Your history will look a little different from the above!
```

### Checking out a previous commit

Let's say you want to retrieve the file `sample.txt` from the previous commit. Two possible reasons why:

1. You just want to take a quick look at something in the previous commit, but then go back to the current version. That's what we'll do here.
2. Maybe you don't like the most recent commit and want to do some new edits _starting from the previous commit_ -- in effect, undoing the most recent commit and going back in time. The simplest way to do this is to _create a new branch_ starting from the previous commit. We'll cover branches more fully in the next lesson.

To retrieve the previous commit, just use `git checkout` and the unique number code which you can just copy and paste from the `git log` output:

```bash
git checkout 35fcbd991f911e170df550db58f74a082ba18b50
```

You may see output that looks like this:

```bash
Note: switching to '35fcbd991f911e170df550db58f74a082ba18b50'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

HEAD is now at 35fcbd9 Close docstring quote on sample.py
```

(the details may vary depending on what version of git you are running).

By `detached HEAD`, git is telling us that we are NOT on the most recent commit in this branch.

If you inspect `sample.txt` in your editor, you will see that the typo `Fxing` is back!

As the git message above is reminding us, it's possible to create an entirely new branch with changes that we make from this point in the history using `git switch -c`. But for now, let's just go back to the most recent commit on our `fix-typo` branch:

```bash
git checkout fix-typo
```

## Comparing versions

We already saw one use of the `git diff` command to look at changes in a repo. By default `git diff` will compare the currently saved files against the most recent commit.

We can also use `git diff` to compare across commits within a branch, or between two different branches. Here are some examples.

### Compare across commits

To compare across any commits in our history, we again use the unique commit checksum that we listed with `git log`:

```bash
git diff HEAD 35fcbd991f911e170df550db58f74a082ba18b50
```

gives

```bash
diff --git a/sample.txt b/sample.txt
index edc31c0..4bc074c 100644
--- a/sample.txt
+++ b/sample.txt
@@ -4,6 +4,6 @@ We can use it to demonstrate making pull requests or raising issues in a GitHub

 One good way to contribute to a project is to make additions and/or edits to documentation!

-Fixing something as simple as a typo is a great way to get started as a contributor!
+Fxing something as simple as a typo is a great way to get started as a contributor!

 Or, consider adding some more content to this file.
```

```{note}
Here we use `HEAD` as an alias for the _most recent commit_.
```

### Compare across branches

Recall that, since we have done all our editing in a new branch, the `main` branch still has the typo!

We can see this with `git diff` using the `..` notation to compare two branches:

```bash
git diff main..fix-typo
```

The output is very similar:

```bash
diff --git a/sample.txt b/sample.txt
index 4bc074c..edc31c0 100644
--- a/sample.txt
+++ b/sample.txt
@@ -4,6 +4,6 @@ We can use it to demonstrate making pull requests or raising issues in a GitHub

 One good way to contribute to a project is to make additions and/or edits to documentation!

-Fxing something as simple as a typo is a great way to get started as a contributor!
+Fixing something as simple as a typo is a great way to get started as a contributor!

 Or, consider adding some more content to this file.
```

The `git diff` command is a powerful comparison tool (and maybe your second new best friend). For many more detail on its usage, see the [git documentation](https://git-scm.com/docs/git-diff).

## Git commands mini-reference

### Commands we used in this tutorial

- `git status`: see what branch we're on and what state our repo is in.
- `git checkout`: switch between branches (use the `-b` flag to create a new branch and check it out)
- `git diff`: compare files between current version and last commit (default), between two commits, or between two branches.
- `git add`: stage a file for a commit.
- `git commit`: create a new commit with the staged files.
- `git log`: see the commit history of our branch.

### Some other git commands you'll want to know

We'll cover many of these in subsequent sections.

- `git branch`: list all the branch in the repo
- `git mv` and `git rm`: git-enhanced versions of the `mv` (move file) and `rm` (remove file) commands. These will automatically stage the changes in your current branch.
- `git merge`: merge changes from one branch into another.
- `git push` and `git pull`: export or input changes between your local branch and a remote repository (e.g. hosted on GitHub).
- `git init`: create a brand-new repo in the current directory

---

## Summary

- Version control is an important tool for working with code files (or anything that is saved as plain text).
- git is the most common version control software in use today.
- `git status` is your new best friend because it gives you a quick view into what's going on in a git repository.
- Every branch of a git repository has a history which is a series of numbered and labelled commits.
- You can view this history with `git log`
- Making a new commit is a two-step process with `git add` and `git commit`.
- Commits are non-destructive, meaning you can always go back in time to previous commits.

### What's Next?

Next we'll explore the concept of branching in git repositories in more detail, including how to merge changes made on one branch into another branch.

## References

1. [Official git documentation](https://git-scm.com/doc)
1. [The Software Carpentries beginner lessons on git](https://swcarpentry.github.io/git-novice/)
