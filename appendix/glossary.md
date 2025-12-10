---
title: Glossary
description: Glossary of terms used in Pythia Foundations.
---

:::{glossary}

[Binder](https://jupyter.org/binder)
: An open-source service that allows users to create sharable, interactive computing environments from {term}`Jupyter Notebooks` and other repositories. Binder can reproduce a computational environment directly from a GitHub repository, providing a seamless way to share and interact with code and data.

: The public service to run Binder is on <https://mybinder.org>, which is running {term}`BinderHub`. The Binder links on most Project Pythia pages point to <https://binder.projectpythia.org>, which is a Pythia-specific implementation of {term}`BinderHub` running on the NSF-supported [Jetstream2](https://jetstream-cloud.org/) cloud computing service.

BinderHub
: The underlying technology and infrastructure that powers {term}`Binder`. BinderHub deploys and manages the interactive computing environments for {term}`Jupyter Notebooks`, ensuring that users can access and share reproducible computational work.

Conda
: Conda is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s). To install `conda`, we recommend {term}`miniconda`.
: See [Conda documentation](https://docs.conda.io/en/latest/) and the [Conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/) and @conda-commands in the context of Project Pythia.

Jupyter Notebooks
: The Jupyter Notebook software is an open-source web application that allows you to create and share Jupyter Notebooks (`*.ipynb` files). Jupyter Notebooks contain executable code, LaTeX equations, visualizations (e.g., plots, pictures), and narrative text. The code does not have to just be Python, other languages such as Julia or R are supported as well. Jupyter Notebooks are celebrated for their interactive output that allows movement between code, code output, explanations, and more code - similar to how scientists think and solve problems. Jupyter Notebooks can be thought of as a living, runnable publication and make for a great presentation platform. See also {term}`Jupyter Kernels`, {term}`Jupyter Lab`, {term}`Jupyter Hub`, {term}`Binder`, and {term}`BinderHub`.

Jupyter Kernels
: Software engines and their environments (e.g., conda environments) that execute the code contained in {term}`Jupyter Notebooks`.

Jupyter Lab
: A popular web application on which users can create and write their {term}`Jupyter Notebooks`, as well as explore data, install software, etc. You can find more information on running Jupyter Lab [here](https://jupyter.org/install).

: See @installing-python-in-jupyter for more.

Jupyter Hub
: A web-based platform that authenticates users and launches {term}`Jupyter Lab` applications for users on remote systems.

Miniconda
: [Miniconda](https://docs.conda.io/en/latest/miniconda.html) is a free minimal installer for {term}`Conda`. Miniconda only comes with the {term}`Conda` package management system; it is a pared-down version of the full Anaconda Python distribution.
: See @installing-conda.

Miniforge
: Miniforge is the community driven and more permissively licensed minimal installer.

[NCL](https://www.ncl.ucar.edu/)
: The NCAR Command Language (NCL) is an interpreted language designed specifically for scientific data analysis and visualization.

Python package
: A Python package is a collection of modules, which, in turn, are essentially Python scripts that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax rules. You can install Python packages with {term}`conda`.
:::
