```{image} ../../images/GitHub-logo.png
:alt: GitHub Logo
:width: 400px
```

# Opening a Pull Request on GitHub

A Pull Request, aka a "merge request," is an event that occurs when a project contributor begins the process of merging new code changes from a feature branch with the main project repository.

## Overview:

1. What is a Pull Request?
1. Opening a Pull Request
1. Pull Request Features
1. GitHub Workflows

## Prerequisites

| Concepts                                      | Importance  | Notes |
| --------------------------------------------- | ----------- | ----- |
| [What is GitHub](what-is-github)              | Necessary   |       |
| [GitHub Repositories](github-repos)           | Necessary   |       |
| [Cloning and Forking](github-cloning-forking) | Necessary   |       |
| [Basic Version Control with _git_](basic-git) | Necessary   |       |
| [Issues and Discussions](github-issues)       | Recommended |       |
| [Branches](git-branches)                      | Necessary   |       |

- **Time to learn**: 60 minutes

---

## What is a Pull Request?

A Pull Request (PR) is a formal mechanism for requesting that changes
that you have made to one repository are integrated (merged) into
another repository. Typically, the changes are reviewed by the
maintainers of the destination repository, potentially triggering
a cycle of revisions, before the PR is “merged”, and your changes
become part of the destination repo.

Just like Issues, PRs have
their own discussion forum for communicating about the proposed
changes. In fact, not only can maintainers or collaborators communicate
about your PR via GitHub, they can also suggest changes and may
even be able to make changes of their own by pushing follow-up
commits. All of the activity, from start to finish, is tracked
inside of the PR and can be reviewed at any time.

When a contributor to a project creates a PR they are requesting
that the owners of another destination repository pull a git
branch from the contributor’s repository and merge the contents of
the branch into a branch of the destination repository. This means
that the contributor must provide four pieces of information: the
contributor’s repository, the contributor’s branch, the destination
repository, and finally, the destination branch.

A typical sequence of steps consists of the following:

1. A contributor clones a personal remote repository, creating a local copy
1. The contributor creates a new branch in their local repository
1. The contributor makes changes to the branch and commits them to
   their local repository
1. The contributor _pushes_ the branch to a remote repository
1. The contributor submits a PR via GitHub

After the maintainers or collaborators of the destination review
the changes, and any suggested revisions are made, the project
maintainer merges the feature into the destination repository and
closes the PR.

## Opening a Pull Request

The demonstration is a continuation from the [GitHub Branches chapter](github-branches). Here, we will move from your local terminal to GitHub.

### Navigate to Your Fork

Go to your fork of the [GitHub Sandbox Repository](https://github.com/ProjectPythia/github-sandbox). One fast way to get to your fork, is to click the "fork" button and then follow the link underneath the message, "You've already forked github-sandbox."

When you've navigated to your fork, you should see a message box alerting you that your branch `branchA` had recent changes with the option to generate an open Pull Request. This Pull Request would take the changes from your `branchA` branch and suggest them for the original upstream ProjectPythia github-sandbox repository. You'll also notice that you are on branch `main`, but that there are now 2 branches.

![GitHub](../../images/8-github.png)

### Switch Branches

If you click on the branch `main` you'll see the list of these branches.

![GitHub Branches](../../images/9-github-seebranches.png)

There you can click on the branch `branchA` to switch branches.

![New Branch](../../images/10-github-newbranch.png)

Here you will see the message, "This branch is 1 commit ahead of ProjectPythia:main." Next to this message you'll see either the option to "Contribute" (which opens a Pull Request) or "Fetch Upstream" (which pulls in changes from the original repository). And just above your files you'll see your most recent commit.

### Open a Draft Pull Request

Click on the "Open pull request" button under the "Contribute" drop-down.

![Contribute](../../images/11-newbranch-contribute.png)

This will send you to a new page. Notice that you are now in "ProjectPythia/github-sandbox" and not your fork.

![Compare](../../images/12-compare.png)

The page will have the two branches you are comparing with an arrow indicating which branch is to be merged into which. Here, `base` is the upstream origin and `head` is your forked repository. If you wanted, you could click on these branches to switch the merge configuration. Underneath that you'll see a green message, "Able to merge. These branches can be automatically merged." This message means that there are no conflicts. We will discuss conflicts in a later chapter.

In a one-commit PR, the PR title defaults to your commit message. You can change this if you'd like. There is also a space to add a commit message. This is your opportunity to explain your changes to the owners of the upstream repository.

![Message](../../images/13-message.png)

And if you scroll down, you'll see a summary of this PR with every commit and changed file listed.

![Summary](../../images/14-prsummary.png)

Click the arrow next to "Create Pull Request" to change this to a draft PR.

![To Draft](../../images/15-todraft.png)

Once you've clicked "Draft Pull Request," you will be directed to the page of your new PR. Here you can add more comments or request reviews.

![Draft PR](../../images/16-draft.png)

## Pull Request Features

Now let's look at the features and discussions in an open (draft) PR.
Clicking "Files Changed" allows you to see all of the changes that would be merged with this PR.

![Files](../../images/17-fileschanged.png)

If you are working in a repository that has automatic checks, it is a good idea to wait for these checks to pass successfully before you request reviewers or change to a non-draft PR. Do this by clicking "Ready for Review."

![Review](../../images/18-review.png)

When working on a project with a larger team, do NOT merge your Pull Request before you have the approval of your teammates. Every team has their own requirements and best practice workflows, and will discuss/approve/reject Pull Requests together. We will cover more about the ways to interact with PRs through conversations and reviews in a later section.

To someone with write permissions on the repository, the ability to merge will look like this green button:
![Green](../../images/20-green.png)

However, this PR will NOT be merged, as the GitHub-Sandbox repository is intended to be static.

## GitHub Workflows

The above demonstration is an example of the Git **Forking Workflow**, because we forked the [GitHub Sandbox repository](https://github.com/ProjectPythia/github-sandbox) before making our feature branches. This is most common when you do NOT have write-access to the upstream repository.

This differs from the **Feature Workflow**, where all contributors work on a single, remote GitHub repository in specific feature branches. This is common when all contributors DO have write-access to the upstream repository.

The steps leading up to creating your PR depend on your workflow. The main difference in creating the PR is that
the contributor now, for the Feature Workflow, navigates to the upstream, remote
repository, not a personal remote fork, and initiates the PR there.

We will cover [GitHub Workflows](github-workflows) in greater detail in the next chapter.

---

## Summary

- A Pull Request (PR) is a formal mechanism for requesting that changes
  that you have made to one repository are integrated (merged) into
  another repository.
- The steps that lead up to
  the PR depend your GitHub Workflow.

### What's Next?

In the next lesson we will learn more about [Reviewing Pull Requests](review-pr).

## References

1. GitHub's [Collaborating with Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
