---
title: Glossary
description: Glossary of terms used in Pythia Foundations.
---

:::{glossary}

[Binder](https://jupyter.org/binder)
: An open-source service that allows users to create sharable, interactive computing environments from {term}`Jupyter Notebooks` and other repositories. Binder can reproduce a computational environment directly from a {term}`GitHub` repository, providing a seamless way to share and interact with code and data.

: The public service to run Binder is on <https://mybinder.org>, which is running {term}`BinderHub`. The Binder links on most Project Pythia pages point to <https://binder.projectpythia.org>, which is a Pythia-specific implementation of {term}`BinderHub` running on the NSF-supported [Jetstream2](https://jetstream-cloud.org/) cloud computing service.

BinderHub
: The underlying technology and infrastructure that powers {term}`Binder`. BinderHub deploys and manages the interactive computing environments for {term}`Jupyter Notebooks`, ensuring that users can access and share reproducible computational work.

branch
: A separate workspace to make and track changes without impacting other branches of the code {term}`repository`.

bug
: An error or flaw in software.

checkout
: A {term}`Git` command used to change branches.

clone
: A {term}`Git` command used to create a local copy of a remote repository.

command-line tools
: Text-based programs that users interact with via the terminal application or command line.

commit
: A snapshot of your Git repository at a specific time.

Conda
: Conda is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s). To install `conda`, we recommend {term}`miniconda`.
: See [Conda documentation](https://docs.conda.io/en/latest/), particularly the [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/user-guide/cheatsheet.html), and @conda-commands in the context of Project Pythia.

DevOps
: The integration and automation of practices and processes for software development and operations.

discussions
: An optional feature of {term}`GitHub` repositories that allows for things like sharing project related announcements, gauging opinions through polls, hosting planning discussions, and Q&A.

documentation
: Software documentation is descriptive content (e.g., text, images, videos) that is either embedded in the software code or distributed alongside the corresponding software.

Feature Branch Workflow
: A collaborative development workflow where new development takes place on dedicated branches rather than the main branch.

fork
: A copy of another project hosted on a collaborative development platform such as {term}`GitHub`.

Forking Workflow
: A collaborative development workflow where new development takes place on forked repositories rather than the main project repository.

free and open-source software
: Software that is free of charge and where the underlying code is publicly available.

Git
: A popular, distributed {term}`version control system`.

GitHub
: A web platform for collaborative software development.

issue
: A common feature of collaborative development platforms such as {term}`GitHub` used to track bugs, request features, and manage work related for a specific repository.

Jupyter Notebooks
: The Jupyter Notebook software is an open-source web application that allows you to create and share Jupyter Notebooks (`*.ipynb` files). Jupyter Notebooks contain executable code, LaTeX equations, visualizations (e.g., plots, pictures), and narrative text. The code does not have to just be Python, other languages such as Julia or R are supported as well. Jupyter Notebooks are celebrated for their interactive output that allows movement between code, code output, explanations, and more code - similar to how scientists think and solve problems. Jupyter Notebooks can be thought of as a living, runnable publication and make for a great presentation platform. See also {term}`Jupyter Kernels`, {term}`JupyterLab`, {term}`JupyterHub`, {term}`Binder`, and {term}`BinderHub`.

Jupyter Kernels
: Software engines and their environments (e.g., conda environments) that execute the code contained in {term}`Jupyter Notebooks`.

JupyterLab
: A popular web application on which users can create and write their {term}`Jupyter Notebooks`, as well as explore data, install software, etc. You can find more information on running JupyterLab [here](https://jupyter.org/install).

: See @installing-python-in-jupyter for more.

JupyterHub
: A web-based platform that authenticates users and launches {term}`JupyterLab` applications for users on remote systems.

Linux
: A free and open-souce operating system based on [Unix](wiki:Unix).

local
: Refering to something, such as a {term}`Git` repository, on your computer rather than a remote server.

merge
: A specific type of commit that combines changes from two branches.

Miniconda
: [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a free minimal installer for {term}`Conda`. Miniconda only comes with the {term}`Conda` package management system; it is a pared-down version of the full Anaconda Python distribution.
: See @installing-conda.

Miniforge
: Miniforge is the community driven and more permissively licensed minimal installer.

[NCL](https://www.ncl.ucar.edu/)
: The NCAR Command Language (NCL) is an interpreted language designed specifically for scientific data analysis and visualization.

origin
: The name for the default remote {term}`Git` repository where you plan to publish commits.

pull
: A {term}`Git` command used to download and integrate changes into your local repository.

pull request
: A mechanism to propose code changes to be merged into a repository.

push
: A {term}`Git` command to upload local commits to a remote repository.

Python package
: A Python package is a collection of modules, which, in turn, are essentially Python scripts that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax rules. You can install Python packages with {term}`conda`.

repository
: A storage space containing all of the files and revision history for a software project. Also known as a repo.

remote
: A repository hosted on a server such as {term}`GitHub`.

scientific Python ecosystem
: A collection of open source Python packages that support analysis, manipulation, and visualization of scientific data.

upstream
: The project repository from which a fork was created.

version control
: A software practice for tracking and managing changes to code and other information stored in {term}`repositories <repository>`

version control system
: Software tools that track and manage changes to project code and files over time.

:::
