# Git Branches

The best practices for a simple workflow for suggesting changes to a GitHub repository are: create your own fork of the repository, make a branch from your fork where your changes are made, and then suggest these changes move to the upstream repository with a pull request. This section of the GitHub chapter assumes you have read the prior GitHub sections, are at least somewhat familiar with git commands and the vocabulary ("cloning," "forking," "merging," "pull request" etc), and that you have already created your own fork of the [GitHub Sandbox Repository](https://github.com/ProjectPythia/github-sandbox) hosted by Project Pythia. That fork is where you will make your first Git branch while following along with this chapter.

## Overview:

1. What are Git Branches
1. Creating a New Branch
1. Switching Branches
1. Setting up a Remote Branch
1. Merging Branches
1. Pulling
1. Deleting Branches

## Prerequisites

| Concepts                                                   | Importance  | Notes                        |
| ---------------------------------------------------------- | ----------- | ---------------------------- |
| [What is GitHub?](what-is-github)                          | Necessary   | GitHub user account required |
| [GitHub Repositories](github-repos)                        | Necessary   |                              |
| [Issues and Discussions](github-issues)                    | Recommended |                              |
| [Cloning and Forking a Repository](github-cloning-forking) | Necessary   |                              |
| [Advanced GitHub Setup](github-setup-advanced)             |             |                              |
| [Basic Version Control with Git](basic-git)                |             |                              |

- **Time to learn**: 30 minutes

---

## What are Git branches?

Git branches allow for non-linear or differing revision histories of a repository. At a point in time, you can split your repository into multiple development paths (branches) where you can make different commits in each, typically with the ultimate intention of merging these branches and development changes together at a later time.

Branching is one of git's methods for helping with collaborative document editing, much like "change tracking" in Google Docs or Microsoft Word. It enables multiple people to edit copies of the same document content, while reducing or managing edit collisions, and with the ultimate aim of merging everyones changes together later. It also allows the same person to edit multiple copies of the same document, but with different intentions. Some reasons for wanting to split your repository into multiple paths (i.e. branches) is to experiment with different methods of solving a problem (before deciding which method will ultimately be merged) and to work on different problems within the same codebase (without confusing which code changes are relevant to which problem). There are also some convenience bots on GitHub that, if installed in the repository, may not act as intended if your work is all on the `main` branch.

These branches can live on your computer (local) or on GitHub (remote). They are brought together through Git _pushes_, _pulls_, and _pull requests_. _Pushing_ is how you transfer changes from your local repository to a remote repository. _Pulling_ is how you fetch upstream changes into your branch. And _Pull Requests_ are how you suggest the changes you've made on your branch to the upstream codebase.

One rule of thumb is for each development feature to have its own development branch until that feature is ready to be added to the upstream (remote) codebase. This allows you to compartmentalize your pull requests so that smaller working changes can be merged upstream independently of one another. For example, you might have a complete or near-complete feature on its own branch with an open pull request awaiting review. While you wait for feedback from the team before merging it, you can still work on a second feature on a second branch without affecting your first feature's pull request. **We encourage you to always do your work in a designated branch.**

![basic branch](../../images/basicbranch.png)
The above flowchart demonstraties commits (C1 through C5) added to different branches of a personal fork of the upstream main repository. Different commits can be added to either branch in any order without depending on or knowing about each other.

## Creating a New Branch

```{admonition} Have you forked the repository?
:class: info
Having forked (NOT just cloned) the [GitHub Sandbox Repository](https://github.com/ProjectPythia/github-sandbox) is essential for following the steps in this book chapter. See the chapter on [GitHub Cloning and Forking](github-cloning-forking.md).
```

From your terminal, navigate to your local clone of your `Github-Sandbox` Repository fork:

```
cd github-sandbox
```

Let's begin by checking the status of our repository:

```
git status
```

![Git Status](../../images/1-gitstatus.png)

You will see that you are already on a branch called "main". And that this branch is up-to-date with "origin/main" and has nothing to commit.

```{admonition} The Main Branch
:class: info
Historically, the `main` branch was called the `master` branch. The name change was relatively recent, so all of your GitHub repositories may not reflect this yet. See instructions to change your branch name at [Github's Branch Renaming documentation](https://github.com/github/renaming).
```

Now check the status of your remote repository with

```
git remote -v
```

![Git Remote](../../images/2-gitremote.png)

We are set up to pull (denoted as 'fetch' in the output above) and push from the same remote repository.

Next, check all of your exising Git branches with:

```
git branch -a
```

![Git Branch](../../images/3-gitbranch.png)

You will see one local branch (`main`) and your remote branch (`remotes/origin/HEAD` and `remotes/origin/main`, where `HEAD` points to `main`). `HEAD` is the pointer to the current branch reference, or in essence, a pointer to your last commit. More on this in a later section.

Now, before we make some sample changes to our codebase, let's create a new branch where we'll make these changes:

```
git branch newbranch
```

Check that this branch was created with:

```
git branch
```

![Git NewBranch](../../images/4-gitnewbranch.png)

This will display the current and the new branch. You'll notice that we are still on branch `main` and will need to switch branches to work in our `newbranch`.

## Switching Branches

To switch branches use the command `git checkout` as in:

```
git checkout newbranch
```

To check your current branch use `git status`:

```
git status
```

![Git Checkout](../../images/5-gitcheckout.png)

Notice that `git status` doesn't say anything about being up-to-date, as before. This is because this branch only exists locally, not in our upstream GitHub fork.

## Setting up a Remote Branch

Before we push this branch upstream, let's make some sample changes by creating a new empty file, with the ending ".py".

```
touch hello.py
```

![Git Status](../../images/6-samplechange.png)

You can check that this file has been created by comparing an `ls` before and after this command, and also with a `git status` that will show your new untracked file.

`git add` and `git commit` your new file and check the status again.

![Git Add](../../images/6a-gitadd.png)

Your new branch is now one commit ahead of your main branch. You can see this with a `git log.`

![Git Log](../../images/6b-gitlog.png)

In a real workflow, you would continue making edits and git commits on a branch until you are ready to push up to GitHub.

Try to do this with

```
git push
```

![Git Push](../../images/6c-gitpush.png)

You will get an error message, "fatal: The current branch newbranch has no upstream branch." So what is the proper method for getting our local branch changes up to GitHub?

First, we need to set an upstream branch to direct our local push to:

```
git push --set-upstream origin newbranch
```

Thankfully, Git provided this command in the previous error message.

![Set Upstream](../../images/6d-setupstream.png)

We can see that this worked by doing a `git branch -a`

Notice the new branch called `remotes/origin/newbranch`. And when you do a `git status` you'll see that we are up to date with this new remote branch.

![Git Commit Status](../../images/7-github-branchandstatus.png)

On future commits you will not have to repeat these steps, as your remote branch will already be established. Simply push with `git push` to have your remote branch reflect your future local changes.

![remote](../../images/remote.png)
The above flowchart demonstrates adding commits locally (C3 and C4) before pushing them to the corresponding remote branch.

## Merging Branches

At this point, we will demonstrate how to merge branches via a Pull Request. Merging is how you bring your split branches of a repository back together again.

![PR](../../images/PR.png)
The above flowchart demonstrates a simple Pull Request (PR1), the upstream main repository has accepted the changes from the Feature 2 branch of your fork. The latest commit to the Upstream Main repository is now C4. Your Feature2 branch can now be safely deleted. This flowchart has simplified out the remote and local versions of the Feature2 branch.

The demonstration will move from your local terminal to GitHub. Go to your fork of the [GitHub Sandbox Repository](https://github.com/ProjectPythia/github-sandbox). One fast way to get to your fork, is to click the "fork" button and then follow the link underneath the message, "You've already forked github-sandbox."

When you've navigated to your fork, you should see a message box alerting you that your branch `newbranch` had recent changes with the option to generate an open pull request. This pull request would take the changes from your `newbranch` branch and suggest them for the original upstream ProjectPythia github-sandbox repository. You'll also notice that you are on branch `main`, but that there are now 2 branches.

![GitHub](../../images/8-github.png)

If you click on the branch `main` you'll see the list of these branches.

![GitHub Branches](../../images/9-github-seebranches.png)

There you can click on the branch `newbranch` to switch branches.

![New Branch](../../images/10-github-newbranch.png)

Here you will see the message, "This branch is 1 commit ahead of ProjectPythia:main." Next to this message you'll see either the option to "Contribute" (which opens a pull request) or "Fetch Upstream" (which pulls in changes from the original repository). And just above your files you'll see your most recent commit.

Click on the "Open a Pull Request" button under the "Contribute" drop-down.

![Contribute](../../images/11-newbranch-contribute.png)

This will send you to a new page. Notice that you are now in "ProjectPythia/github-sandbox" and not your fork.

![Compare](../../images/12-compare.png)

The page will have the two branches you are comparing with an arrow indicating which branch is to be merged into which. Here, `base` is the upstream origin and `head` is your forked repository. If you wanted, you could click on these branches to switch the merge configuration. Underneath that you'll see a green message, "Able to merge. These branches can be automatically merged." This message means that there are no conflicts. We will discuss conflicts in a later chapter.

In a one-commit pull request, the pull request title defaults to your commit message. You can change this if you'd like. There is also a space to add a commit message. This is your opportunity to explain your changes to the owners of the upstream repository.

![Message](../../images/13-message.png)

And if you scroll down, you'll see a summary of this pull request with every commit and changed file listed.

![Summary](../../images/14-prsummary.png)

Click the arrow next to "Create Pull Request" to change this to a draft pull request.

![To Draft](../../images/15-todraft.png)

Once you've clicked "Draft Pull Request," you will be directed to the page of your new pull request. Here you can add more comments or request reviews.

![Draft PR](../../images/16-draft.png)

Clicking "Files Changed" allows you to see all of the changes that would be merged with this pull request.

![Files](../../images/17-fileschanged.png)

If you are working in a repository that has automatic checks, it is a good idea to wait for these checks to pass successfully before you request reviewers or change to a non-draft pull request. Do this by clicking "Ready for Review."

![Review](../../images/18-review.png)

When working on a project with a larger team, do NOT merge your pull request before you have the approval of your teammates. Every team has their own requirements and best practice workflows, and will discuss/approve/reject pull requests together. We will cover more about the ways to interact with pull requests through conversations and reviews in a later section.

To someone with write permissions on the repository, the ability to merge will look like this green button:
![Green](../../images/20-green.png)

However, this pull request will NOT be merged, as the GitHub-Sandbox repository is intended to be static.

![remotePR](../../images/remotePR.png)
The above flowchart demonstrates a Pull Request (PR1) without simplifying out the remote vs local versions of the Feature2branch. Typically multiple pushes are made from your local to remote branch before a pull request is drafted to take all of those commits (C3, C4, C6, and C7) into the Upstream Main branch.

## Pulling

Once a team member's pull request has been merged, you will find that these upstream changes are not automatically included in your fork or your branches. In order to include the changes from the upstream main branch, you will need to do a `git pull`.

![pull](../../images/pull.png)
The above flowchart demonstrates pulling in the upstream changes from Upstream Main after the pull request PR1 has been merged. Before continuing to work, with new commits (C6), it is best to pull in the upstream changes. The local vs remote branches have been simplified out of this diagram.

First check if there are any upstream changes:

```
git status
```

Then, if there are no conflicts:

```
git pull
```

`git pull` is a combination of `git fetch` and `git merge`. That is it updates the remote tracking branches (`git fetch`) AND updates your current branch with any new commits on the remote tracking branch (`git merge`).

![team](../../images/team.png)
The above flowchart demonstrates pulling in the upstream changes from Upstream Main in a team setting. Multiple authors will have their own feature branches that merge into the same Upstream Main repository by pull requests. It is important for each author to do regular `git pulls` to stay up to date with each other's contributions. The local vs remote branches have been simplified out of this diagram.

## Deleting Branches

After the feature you worked on has been completed and merged, you may want to delete your branch.

To do this locally, you must first switch back to `main` or any non-target branch. Then you can enter

```
git branch -d <branch>
```

for example

```
git branch -d newbranch
```

To delete the branch remotely, type

```
git push <remote> --delete <branch>.
```

as in

```
git push origin --delete jukent/newbranch
```

---

## Summary

- Git Branches allow you to independently work on different features of a project via differing revision histories of a repository.
- A useful workflow is to create a new branch locally, switch to it and set up a remote branch. During your revision, push to your upstream branch and pull from main as often as necessary. Then suggest your edits via a pull request and, if desired, delete your branch after the merge.

### What's Next?

Opening a Pull Request on GitHub

## References

1. “GitHub.com Help Documentation.” GitHub Docs, https://docs.github.com/en.
2. Paul, Kevin. “Python Tutorial Seminar Series - Github.” Project Pythia, YouTube, 12 May 2021, https://www.youtube.com/watch?v=fYkPn0Nttlg.
