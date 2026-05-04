# Installing and Managing Python with Conda

---

## Overview

{term}`Conda` is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s).

Here we will cover:

1.  What are packages?
2.  Installing Conda
3.  Creating a Conda environment
4.  Useful Conda commands

## Prerequisites

| Concepts                                                                                                  | Importance | Notes |
| --------------------------------------------------------------------------------------------------------- | ---------- | ----- |
| [Installing and Running Python](how-to-run-python.md)                                                     | Helpful    |       |

- **Time to learn**: 20 minutes

---

## What are Packages?

A Python package is a collection of modules, which, in turn, are essentially Python scripts that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax rules.

Many geoscience workflows tend to rely on relatively complex collections of Python packages and compiled libraries. Frequent updates to packages can also cause conflicts to arise between incompatible versions. For these reasons, it is often best to create tailored computing environments for each project. Keeping track of package dependencies and versions, and keeping incompatible environments isolated from each other, is the job of a package manager!

In Foundations, we use {term}`Conda`, but there are a few other ways to manage packages that you may have encountered before. [pip](https://pip.pypa.io/en/stable/) is probably the most popular option for installing Python packages, which can be used in combination with [venv](https://docs.python.org/3/library/venv.html) for creating isolated environments. We recommend against pip here due to the prevalence of dependencies on compiled libraries in geoscience workflows. Newer options include [pixi](https://pixi.prefix.dev/latest/) and [uv](https://docs.astral.sh/uv/).

(installing-conda)=

## Installing Conda

We recommend you start by installing [Miniforge](https://github.com/conda-forge/miniforge). This is a specific version of the {term}Conda package manager pre-configured to work with the `conda-forge` package repository -- our recommended source for most of the packages you will need.

You can install Miniforge by following the [instructions for your machine](https://github.com/conda-forge/miniforge#install).

Miniforge uses the `conda` package management system and is based on Miniconda, which is a pared-down version of the full Anaconda Python distribution.



A few reasons why we recommend installing Miniforge:

1. It's free, lightweight, and won't interfere with other installations on your computer.
2. It encourages you to install only the packages you need in reproducible isolated environments for specific projects. This is generally a more robust way to work with open source tools.
3. It uses `conda-forge` as the default channel for packages, which is our recommended way to get up-to-date, interoperable packages.

Once you have `conda` via the Miniconda installer, the next step is to create an environment and install packages.

## Creating a Conda Environment

A Conda environment is an interoperable collection of specific versions of packages or libraries that you install and use for a specific workflow. The Conda package manager takes care of dependencies, so everything works together in a predictable way. One huge advantage of using environments is that any changes you make to one environment will not affect your other environments at all, so you are much less likely to "break" something!

To create a new Conda environment, type `conda create --name` and the name of your environment in your terminal, and then specify any packages that you would like to have installed. For example, to install a Jupyter-ready environment called `sample_environment`, type

```
conda create --name sample_environment python jupyterlab
```

Once the environment is created, you need to _activate_ it in the current terminal session (see below).

It is a good idea to create a new environment for every project. Because Python is open source, new versions of the tools are released frequently. Isolated environments help guarantee that your scripts use the same versions of packages and libraries to ensure they run as expected. Similarly, it is best practice to NOT modify your `base` environment.

(conda-commands)=

## Useful Conda commands

Some other {term}`Conda` commands that you will find useful include:

- Activating a specific environment

  ```
  conda activate sample_environment
  ```

- Deactivating the current environment

  ```
  conda deactivate
  ```

- Checking what packages/versions are installed in the current environment

  ```
  conda list
  ```

- Installing a new package into the current environment

  ```
  conda install somepackage
  ```

- Installing a specific version of a package into the current environment

  ```
  conda install somepackage=0.17
  ```

- Updating all packages in the current environment to the latest versions

  ```
  conda update --all
  ```

- Checking what conda environments you have

  ```
  conda env list
  ```

- Deleting an environment

  ```
  conda env remove --name sample_environment
  ```

You can find lots more information in the [Conda documentation](https://docs.conda.io/en/latest/) or this handy [Conda cheat sheet](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#cheatsheet).

If you're not a command line user, the Anaconda navigator offers GUI functionality for selecting environments and installing packages.

---

## Summary

Conda is a package and environment management system that allows you to quickly install, run, and update packages within your work environment(s). This is important for gathering all of the tools necessary for your workflow. Conda can be managed in the command line or in the Anaconda GUI.

### What's Next?

- [How to Run Python in the Terminal](terminal.md)
- [How to Run Python in a Jupyter Session](jupyter.md)

## Resources and References

- [Linux commands](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
- [Conda documentation](https://docs.conda.io/en/latest/)
- [Conda cheat sheet](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#cheatsheet)
- [Anaconda](https://docs.anaconda.com/anaconda/install/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
