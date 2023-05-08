# Installing and Managing Python with Conda

---

## Overview

Conda is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s).

Here we will cover:

1.  What are packages?
2.  Installing Conda
3.  Creating a Conda environment
4.  Useful Conda commands

## Prerequisites

| Concepts                                                                                                  | Importance | Notes |
| --------------------------------------------------------------------------------------------------------- | ---------- | ----- |
| [Installing and Running Python](https://foundations.projectpythia.org/foundations/how-to-run-python.html) | Helpful    |       |

- **Time to learn**: 20 minutes

---

## What are Packages?

A Python package is a collection of modules, which, in turn, are essentially Python scripts that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax rules.

Package management is useful because you may want to update a package for one of your projects, but keep it at the same version in other projects to ensure that they continue to run as expected.

## Installing Conda

We recommend you install Miniconda. You can do that by following the [instructions for your machine](https://docs.conda.io/en/latest/miniconda.html).

Miniconda only comes with the `conda` package management system; it is a pared-down version of the full Anaconda Python distribution.

[Installing Anaconda](https://docs.anaconda.com/anaconda/install/) takes longer and uses up more disk space, but provides you with more functionality, including Spyder (a Python-specific integrated development environment or IDE) and Jupyter, in addition to other immediately installed packages. Also, the interface of Anaconda is great if you are uncomfortable with the terminal.

We recommend Miniconda for two reasons:

1. It's quicker and takes up less disk space.
2. It encourages you to install only the packages you need in reproducible isolated environments for specific projects. This is generally a more robust way to work with open source tools.

Once you have `conda` via the Miniconda installer, the next step is to create an environment and install packages.

## Creating a Conda Environment

A Conda environment is an interoperable collection of specific versions of packages or libraries that you install and use for a specific workflow. The Conda package manager takes care of dependencies, so everything works together in a predictable way. One huge advantage of using environments is that any changes you make to one environment will not affect your other environments at all, so you are much less likely to "break" something!

To create a new Conda environment, type `conda create --name` and the name of your environment in your terminal, and then specify any packages that you would like to have installed. For example, to install a Jupyter-ready environment called `sample_environment`, type

```
conda create --name sample_environment python jupyterlab
```

Once the environment is created, you need to _activate_ it in the current terminal session (see below).

It is a good idea to create a new environment for every project. Because Python is open source, new versions of the tools are released frequently. Isolated environments help guarantee that your scripts use the same versions of packages and libraries to ensure they run as expected. Similarly, it is best practice to NOT modify your `base` environment.

## Useful Conda commands

Some other Conda commands that you will find useful include:

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

You can find lots more information in the [Conda documentation](https://docs.conda.io/en/latest/) or this handy [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf).

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
- [Conda cheat sheet](https://docs.conda.io/projects/conda/en/latest/_downloads/843d9e0198f2a193a3484886fa28163c/conda-cheatsheet.pdf)
- [Anaconda](https://docs.anaconda.com/anaconda/install/)
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
