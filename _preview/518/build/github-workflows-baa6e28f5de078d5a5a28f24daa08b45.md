```{image} ../../images/Git-Logo-2Color.png
:alt: Git Logo
:width: 400px
```

# GitHub Workflows

A workflow is a series of activities or tasks that must be completed sequentially or parallel to achieve the desired outcome. Here we outline two different GitHub workflows that take you through the steps leading up to opening a Pull Request.

## Overview:

1. GitHub workflows overview
1. Git Feature Branch Workflow
1. Forking workflow

## Prerequisites

| Concepts                                      | Importance  | Notes |
| --------------------------------------------- | ----------- | ----- |
| [What is GitHub](what-is-github)              | Necessary   |       |
| [GitHub Repositories](github-repos)           | Necessary   |       |
| [Cloning and Forking](github-cloning-forking) | Necessary   |       |
| [Basic Version Control with _git_](basic-git) | Necessary   |       |
| [Issues and Discussions](github-issues)       | Recommended |       |
| [Branches](git-branches)                      | Necessary   |       |
| [Pull Requests](github-pull-request)          | Necessary   |       |
| [Reviewing Pull Requests](review-pr)          | Recommended |       |

- **Time to learn**: 60 minutes

---

## GitHub workflows

GitHub, together with Git, are powerful tools for managing and
collaborating on all kinds of digital assets, such as software,
documentation, and even manuscripts for research papers. Like other
complex software environments, often these tools can be employed
in many different ways to accomplish the same goal. In order to
effectively and consistently use Git and GitHub, over the years a
variety of best practices have evolved for supporting different
modes of collaboration. Collectively these different models, or
recipes, are referred to as _workflows_.

A typical sequence of workflow steps consists of the following:

1. A contributor clones a personal remote repository, creating a local copy
1. The contributor creates a new branch in their local repository
1. The contributor makes changes to the branch and commits them to
   their local repository
1. The contributor _pushes_ the branch to a remote repository
1. The contributor submits a PR via GitHub

The sequence of steps
outlined above provides a general framework for submitting a PR.
But the precise set of steps is highly dependent on the choice of
workflow for a given project. In this chapter we describe Pull
Requests for two commonly used workflows: The **Git Feature Branch
Workflow** and the **Forking Workflow**. The former is simpler and often
used by teams when everyone on the team is an authorized contributor
to the destination repository. I.e. all of the contributors have
write access to the remote repository hosted by GitHub. The latter
is typically what is needed to contribute to external projects for
which the contributor is not authorized (i.e. does not have write
access) to make changes to the destination repository. We briefly
describe both workflows below, and include the steps necessary to
make a PR on each.

## Git Feature Branch Workflow

The **Git Feature Branch Workflow** is one of the simplest and oldest
collaborative workflows that is used for small team projects. The
key idea behind this workflow, which is also common to the **Forking
Workflow**, is that all development (all changes) should take place
on a dedicated Git _feature_ branch, not the _main_ (historically
referred to as _master_) branch. The motivation behind this is that
one or more developers can iterate over a feature branch without
disturbing the contents of the main branch. Consider using the **Git
Feature Branch Workflow** for GitHub’s most widely used purpose,
software development. Software modifications are liable to introduce
bugs. Isolating them to a dedicated branch until they can be fixed
ensures that a known, or official, version of the software is always
available and in working order.

```{note}
Avoiding making edits directly on the `main` branch is considered best practice for most workflows and projects!
```

### Working with the Git Feature Branch Workflow

This model assumes a single, remote GitHub repository with a branch
named `main`, that contains the official version of all of the digital
assets, along with a history of all of the changes made. When a
contributor wishes to make changes to the remote repository, they
clone the repo and create a descriptively named feature branch,
such as `my-new-feature` or perhaps `issue-nnn`, where `nnn` is the
number of an issue opened on the repository that this new feature
branch will address. Changes by the contributor are then made to
the feature branch in a local copy of the repository. When ready,
the new branch is pushed to the remote repository.

At this point,
the new branch can be viewed, discussed, and even changed by
contributors with write access to the remote repository. When the
author of the feature branch thinks the changes are ready to be
merged into `main` on the remote repository, they create a PR. The
PR signals the project maintainers that the contributor would like
to merge their feature branch into `main`, and invites review of the
changes made in the branch. GitHub simplifies the process of viewing
the changes by offering a variety of ways to see context differences
(diffs) between `main` and the feature branch. Discussion between
the reviewers and the contributor inside a PR discussion forum
occurs in the same way that discussion over GitHub [Issues](github-issues) takes
place inside a discussion forum associated with a particular issue.
If additional changes are requested by the reviewers, these can be
made by the contributor in their local repository, committed, and
then pushed to the remote using the same processes they used with
the initial push. Once reviewers are satisfied with the changes, a
project maintainer can merge the feature branch with `main`.

##### Cloning the remote repository

If you don’t have a local copy of the remote repository, you’ll want
to create one by [cloning the
remote](github-cloning-forking)
to your local computer. This can be done with the git command line
tools and the general form of the command looks like this:

```
git clone repository-url local-directory-name
```

Where `repository-url` is the URL for the GitHub repo that you want
to clone, and `local-directory-name` is the directory path on your
local machine into which you want to create the clone. The local
directory need not already exist. The clone command will create the
local directory for you. If you don’t know the URL for your
repository, navigate your web browser to your GitHub repository,
and click on the `Code` button. The URL will be displayed.

For example, let's clone the [Project Pythia sandbox repository](https://github.com/ProjectPythia/github-sandbox):

```
git clone https://github.com/ProjectPythia/github-sandbox.git
```

Note, we did not specify a `local-directory_name` here, so git will
use the `base name` of the `repository_url`, "github-sandbox" as
the local directory.

##### Start with the main branch

Continuing with our example above, make sure you are on the main
branch and that it is up to date with the remote repository main:

```
cd github-sandbox
git checkout main
git pull
```

You should see output that looks like:

```
Already on 'main'
Already up to date.
```

Remember you can read more about [GitHub branches](github-branches) in our previous chapter.

##### Create a new branch

Create a separate branch for every new capability you work on:

```
git checkout -b my-new-feature
```

This command will create a new branch named `my-new-feature`, if it
doesn’t exist already, or switch to the existing branch if it does.
Either way, any changes you make will occur in the branch `my-new-feature`,
not in `main`. The output should look something like:

```
Switched to a new branch 'my-new-feature'
```

##### Make changes and commit

Next, we'll make changes and commit them to the `my-new-feature branch` in
the local git repository.

Use your favorite editor to edit the file "sample.py". Add the line:

```
print ("Do you like to rock the party?")
```

after the existing `print` statement in the file.

Run the command `git status` and look at the output. You should see
something like:

```
On branch my-new-feature
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   sample.py

no changes added to commit (use "git add" and/or "git commit -a")
```

Another helpful command is `git diff`, which should give output
that looks like:

```
diff --git a/sample.py b/sample.py
index b2a3b61..bf89419 100644
--- a/sample.py
+++ b/sample.py
@@ -1,5 +1,6 @@
 """This is a text file that contains a sample Python script"""
 print ("Hello, Python learners!")
+print ("Do you like to rock the party?")
 a = 2
 b = 8
```

It's probably obvious that `git status` will show you which files have been modified and are
ready to be committed, while `git diff` will show you how your changes
to `my-new-feature` branch differ from the `main` branch in the local
repository. Once you are ready, commit your changes to the local
repository:

```
git add sample.py
git commit -m "having fun yet?" .
```

After a successful commit you should see a message like:

```
[my-new-feature 69162bc] having fun yet?
 1 file changed, 1 insertion(+)
```

##### Push the feature branch to the remote repository

After running `git commit` your changes have been captured in your
local repository. But most likely only you can see them, and if
your local file system fails your changes may be lost. To make your
changes visible to others, and safely stored on your remote GitHub
repository, you need to push them. However, remember at the beginning
of this section we said that the **Git Feature Branch Workflow** works
when you have write access to the remote repository? Unless you are
a member of Project Pythia you probably don't have write access to
the `github-sandbox` remote repo. So you won't be able to push your
changes to it. That's OK. We can still run the `push` command. It won't
break anything. In the next section on **Forking Workflow** we will
discuss how to make changes on remote repositories that you do NOT
have write access to, such as the one we're using in this example. Here
is the `push` command that we expect to fail:

```
git push --set-upstream origin my-new-feature
```

You should get a helpful error message like:

```
remote: Permission to ProjectPythia/github-sandbox.git denied to clyne.
fatal: unable to access 'https://github.com/ProjectPythia/github-sandbox.git/': The requested URL returned error: 403

```

The use of the ‘--set-upstream’ option is a one-time operation when
you push a new branch. Later, if you want to push subsequent changes
to the remote you can simply do:

```
git push
```

If you are feeling unsatisfied about not having `git push` succeed, there
is a simple solution: create a GitHub repository owned by you. The
GitHub Quickstart guide provides an excellent [tutorial](https://docs.github.com/en/get-started/quickstart/create-a-repo) on how to
do this.

##### Making a Pull Request

Finally, after cloning a remote repository, creating a feature
branch, making your changes, committing them to your local repository,
and pushing your commits back to the remote repository, you are now
ready to issue a PR requesting that the remote repository maintainers
review your changes for potential merger into the main branch on
the remote. This final action must be performed from within your
web browser. After
navigating to your repo do the following:

1. Click on “Pull Requests” in the top navigation bar
1. Click on “New Pull Request”
1. Under “Compare changes”, make sure that `base` is set to `main`, and `compare` is set to the name of your feature branch, `my-new-feature`
1. Click on “Create Pull Request”
1. A PR window should open up. Provide a descriptive title, and any helpful comments that you want to communicate with the reviewers
1. Click on “Create Pull Request” in the PR window.

That’s it! You’re done! Sit back and wait for comments from reviewers.
If changes are requested, simply repeat the steps above. Once your
PR is merged you’ll receive notification from GitHub.

##### Safety tip on synchronization

Over time your local repository will diverge from the remote. Before
starting on a new feature, or if the `main` branch on remote may have
been updated while you were working on `my-new-feature`, it is a good
idea to periodically sync up with the remote `main`. Make sure all
of your changes to `my-new-feature` have been committed to the local
repository, and then do:

```
git checkout main
git pull
git checkout my-new-feature
git merge main
```

## Forking Workflow

The **Git Feature Branch Workflow** described above, along with the
steps needed to submit a PR, work when you have write access to the
remote repository. But as we saw, if you don't have write access
you will not be able to push your changes to the remote repo. So,
if you are contributing to an open source project, such as Project
Pythia for example, a slightly different workflow is required.
The **Forking Workflow** is the one most commonly used for public open
source projects. The primary difference between the **Forking Workflow**
and the **Git Feature Branch Workflow** is that with the former, two
remote repositories are involved: one managed by the developers of
the project that you wish to contribute to, and one owned by you.
To help keep things clear we will refer to these remotes as the
upstream repository and the personal repository, respectively. Not
surprisingly, the personal repository will be a clone of the project
repository that you own and can push changes too. The personal
repository must be public, so that the maintainers of the upstream
repository can pull changes from it. Other than a couple of additional
steps required at the beginning and the end, the process of submitting
a PR when using the **Forking Workflow** is identical to that of the
**Git Feature Branch Workflow**. The basic steps are as follows:

1. A contributor _forks_ the upstream repository, creating a remote clone that is owned by the contributor: the personal repository
1. The contributor then clones the newly created personal remote repository, creating a local copy. Yup, that is two clones.
1. The contributor creates a new branch in their local repository
1. The contributor makes changes to the branch and commits them to their local repository
1. The contributor pushes the branch to their personal remote repository that was created in step 1
1. The contributor submits a PR via GitHub to the upstream repository

Note that steps 2 through 5 are identical to steps 1 through 4 for
the **Git Feature Branch Workflow**. Hence, here we only discuss the
first step, and last step.

### Forking the upstream repository

GitHub makes it really easy to fork a remote repository. Simply
navigate your web browser to the upstream repository that you want
to fork, and click on Fork. GitHub will create a clone of the
upstream repository in the remote destination selected by you on
GitHub, and will then redirect your browser to the newly created
forked, personal repository. The personal repository is owned by
you. Any changes made here will not impact the upstream repository
until you are ready to submit a PR. Let's try it. Follow
the steps under Forking a repository [here](github-cloning-forking).

### Clone, branch, change, commit, push

The next steps are the same as described above for the **Git Feature
Branch Workflow**. Clone a local copy of the newly created remote,
personal repository, create a feature branch, make your changes,
commit your changes, and push the new branch with your commits to your personal repository.

### Making a Pull Request

Once the new feature branch has been pushed to the contributor’s
personal repository, a PR can be created that asks the maintainers
of the upstream repository to merge the contents of the feature
branch on the contributor’s repository into the main branch on the
upstream repository. This step is remarkably similar to making a
PR in the **Git Feature Branch Workflow**. The only difference is that
the contributor navigates their browser to the upstream, remote
repository, not the personal remote, and initiates the PR there.
Specifically, the following steps are once again followed, but
performed on the upstream remote:

1. Click on “Pull Requests” in the top navigation bar
1. Click on “New Pull Request”
1. Under “Compare changes”, make sure that `base` is set to `main`, and `compare` is set to the name of your feature branch, `my-new-feature`
1. Click on “Create Pull Request”
1. A PR window should open up. Provide a descriptive title, and any helpful comments that you want to communicate with the reviewers
1. Click on “Create Pull Request” in the PR window.

### Safety tip on synchronization

Just like with the **Git Feature Branch Workflow** model, over time
your local repository will diverge from the remote(s). Before
starting on a new feature, or if the main branch on remote may have
been updated while you were working on `my-new-feature`, it is a good
idea to periodically sync up with the remote `main`. When working
with forks things get a little more complicated than when only a
single remote is involved. Before syncing with the upstream remote
you must first configure your local repository by running the
following commands from within your local copy of the repo:

```
git remote -v
```

This should produce an output that looks similar to the following:

origin https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)

Next, specify a new remote upstream repository that will be synced with the fork.

```
git remote add upstream upstream-url
```

Where `upstream-url` is the URL of the upstream repository.

Finally, rerun the `git remote -v` command and you should see output
that looks like this:

```
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (fetch)
origin    https://github.com/YOUR_USERNAME/YOUR_FORK.git (push)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (fetch)
upstream  https://github.com/ORIGINAL_OWNER/ORIGINAL_REPOSITORY.git (push)
```

After performing the above steps, you can then synchronize your
local repository with the upstream remote by running the following:

```
git fetch upstream
git checkout main
git merge upstream/main
```

---

## Summary

- The steps that lead up to
  the PR depend your GitHub Workflow.
- Two commonly used GitHub Worflows are **Git Feature Branch Workflow** and
  **Forking Workflow**. The former is appropriate for teams of collaborators
  where everyone has write access to the GitHub repository. The latter
  is commonly used when a developer wishes to contribute to a public GitHub
  project for which they do not have write access to the repository.

### What's Next?

In the next lesson we will put the **Forking Workflow** to work and show you
how to use it to [contribute to Project Pythia](contribute-to-pythia).

## References

1. Atlassian's tutorial on [workflows](https://www.atlassian.com/git/tutorials/comparing-workflows)
1. GitHub's [Collaborating with Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)
