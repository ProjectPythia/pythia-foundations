<img src="../../images/GitHub-logo.png" alt="Github Logo" width="600px">

# GitHub Part 1: What is GitHub?

## Overview:

1.  What is GitHub?
1.  Free- and open-source software (FOSS)
1.  Version control systems (VCS)
1.  GitHub = FOSS + VCS + Web

## Prerequisites

| Concepts | Importance | Notes |
| -------- | ---------- | ----- |
| None     |            |       |

- **Time to learn**: 10 minutes

---

## What is GitHub?

[GitHub](https://github.com) is a web-based platform for the dissemination of free- and open-source software.

If you are reading this lesson, you are already using GitHub, as that is where Project Pythia hosts its content!

GitHub provides the following:

1. _Version control_ for free- and open-source software and other digital assets
1. Project _discussion forums_
1. _DevOps_ to facilitate building and testing software
1. _Bug_ reporting, patching, and tracking
1. _Documentation_ hosting
1. An environment that fosters _collaboration_

Although GitHub can host any digital asset, the most common use case for GitHub is for individuals or organizations to house _repositories_ of _free-_ and _open-source software_:

## Free- and open-source software (FOSS)

Much of what we term the _scientific Python software ecosystem_ consists of _free- and open-source software_. Often abbreviated as **FOSS**, this means:

1.  The software is free-of-charge, and
1.  The various files which contain the _software code_ are publicly available.

```{admonition} Did you know?
:class: info
The [Python language](https://python.org) itself is an example of *FOSS*!
```

FOSS is nothing new. For example, the [Linux kernel source code](https://kernel.org) has been available to download for many years.

```{admonition} Free $\neq$ open source!
:class: tip
Just because a software package may be free does not mean that its source code is open! For example, although Nvidia makes its video drivers available for free download, the source code for those drivers is proprietary.
```

Arguably, the greatest advantage of open-source software is that it enables _collaborative sharing_, and thus community feedback.

Types of community input may include the following:

1. _Issues_: usage questions, bug reports, feature requests
1. _Pull requests_: a user can ask that that their changes/additions be incorporated into the project
1. _Discussions_: a community forum on the open source project

## Version control systems (VCS)

We will discuss version control in more detail later in this series, but the need to track and manage changes to a project, especially one that involves software, has long been known. Over the years, FOSS developers have used VCS such as _cvs_, _svn_, and most recently, _git_. All of these systems are _command-line tools_.

## FOSS and VCS on the Internet

A successful FOSS project needs to be accessible via the web. As mentioned before, the Linux kernel and the Python language have long been available using first-generation remote access protocols such as FTP and HTTP, and SSH. Later, VCS tools such as cvs and svn established their own TCP protocols for remote access. With the advent of _git_, web-based services that supported HTTP(S) and SSH sprung up. Each of these VCS leverages the concept of a particular FOSS project as a <i>code repository</i>.

```{admonition} Did you know?
:class: info
Linus Torvalds, the original developer (and still the lead maintainer) of **Linux**, is also the original developer of [Git](https://git-scm.com)!
```

```{admonition} Stay tuned!
:class: tip
We will discuss version control and the use of **Git** via the command line later in this series.
```

## FOSS + VCS = GitHub

Perhaps the most popular web-based platform that uses Git for FOSS VCS is [GitHub](https://github.com). GitHub hosts all of the Python software packages that Project Pythia covers as code repositories (we'll use the term <i>Git repo</i>, or more generally just <i>repo</i> henceforth to represent a GitHub code repository).

For example, here is a screenshot from [Xarray's GitHub](https://github.com/pydata/xarray) Git repo:

<img src="../../images/XarrayGithub.png" alt="Xarray GitHub" width="600px">

---

## Summary

- GitHub serves as a web-based platform for digital assets, particularly FOSS.
- GitHub uses Git as its version control system.

### What's Next?

In the next lesson, we will explore some GitHub repositories.

## References

1. Ref 1
1. Ref 2
