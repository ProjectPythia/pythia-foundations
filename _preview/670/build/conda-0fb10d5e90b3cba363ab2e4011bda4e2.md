# Installing and Managing Python with Conda

---

## Overview

Conda is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s).

Here we will cover:

1.  Packages and package managers
2.  Installing conda
3.  Creating a conda environment
4.  Useful conda commands

## Prerequisites

| Concepts                                                                                                  | Importance | Notes |
| --------------------------------------------------------------------------------------------------------- | ---------- | ----- |
| [Installing and Running Python](how-to-run-python.md)                                                     | Helpful    |       |

:::{tip icon=false} ⏱️ Time to learn
20 minutes
:::

---

## Packages and package managers

A Python package is a collection of modules, which, in turn, are essentially Python scripts that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax rules.

Many geoscience workflows tend to rely on relatively complex collections of Python packages and compiled libraries. Frequent updates to packages can also cause conflicts to arise between incompatible versions. For these reasons, it is often best to create tailored computing environments for each project. Keeping track of package dependencies and versions, and keeping incompatible environments isolated from each other, is the job of a package manager!

You may have encountered a few different package managers in the Python world:

- [pip](https://pip.pypa.io/en/stable/) is the most common method for installing Python packages, which can be used in combination with [venv](https://docs.python.org/3/library/venv.html) for creating isolated environments.
- [pixi](https://pixi.prefix.dev/latest/) and [uv](https://docs.astral.sh/uv/) are newer options that are gaining popularity&mdash;well worth exploring for the adventurous learner!
- {term}`conda` is widely used for scientific computing, and this is what we recommend.

A key advantage of {term}`conda` over pip is that it manages all types of package requirements, not just Python packages. The most reliable source of up-to-date, interoperable scientific packages are found in the community-maintained {term}`conda-forge` repository (see below).

:::{tip} TL;DR
We strongly recommend using {term}`conda` to install and manage Python and all your complex project-specific software.
:::

(installing-conda)=

## Installing conda

We recommend you start by [installing](https://conda-forge.org/download/) [Miniforge](https://github.com/conda-forge/miniforge). This is a specific version of the {term}`conda` package manager pre-configured to work with the {term}`conda-forge` package repository&mdash;our recommended source for most of the packages you will need.

You can install Miniforge by following the [instructions for your machine](https://github.com/conda-forge/miniforge#install).

:::{tip}For Windows users
When [installing Miniforge using the Windows installer](https://conda-forge.org/download/), make sure to check "Create start menu shortcuts (supported packages only)". Then in your start menu or search box, you will find the "Miniforge Prompt", where you will enter commands.
:::

A few reasons why we recommend installing Miniforge:

1. It's free, lightweight, and won't interfere with other installations on your computer.
2. It encourages you to install only the packages you need in reproducible isolated environments for specific projects. This is generally a more robust way to work with open source tools.
3. It uses {term}`conda-forge` as the default channel for packages, which is our recommended way to get up-to-date, interoperable packages.

Once you have {term}`conda` via the {term}`Miniforge` installer, the next step is to create an environment and install packages.

:::{note}
Users looking for a full-featured commercially licensed and supported Python environment manager should take a look at [Anaconda](https://www.anaconda.com/), which may be [free for academic usage](https://www.anaconda.com/blog/update-on-anacondas-terms-of-service-for-academia-and-research).

The conda package manager and our recommended Miniforge installation are open source, community-supported and free for all users.
:::

## Creating a conda environment

A conda environment is an interoperable collection of specific versions of packages or libraries that you install and use for a specific workflow. The conda package manager takes care of dependencies, so everything works together in a predictable way. One huge advantage of using environments is that any changes you make to one environment will not affect your other environments at all, so you are much less likely to "break" something!

To create a new conda environment, type `conda create --name` and the name of your environment in your terminal, and then specify any packages that you would like to have installed. For example, to install a Jupyter-ready environment called `sample_environment`, type

```
conda create --name sample_environment python jupyterlab
```

Once the environment is created, you need to _activate_ it in the current terminal session (see below).

It is a good idea to create a new environment for every project. Because Python is open source, new versions of the tools are released frequently. Isolated environments help guarantee that your scripts use the same versions of packages and libraries to ensure they run as expected. Similarly, it is best practice to NOT modify your `base` environment.

(conda-commands)=

## Useful conda commands

Some other {term}`conda` commands that you will find useful include:

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

You can find lots more information in the [conda documentation](https://docs.conda.io/en/latest/) or this handy [conda cheat sheet](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#cheatsheet).

:::{tip} What if the package you need is not available from {term}`conda-forge`?
If the package you are trying to use (`somepackage` in these examples) only mentions `pip install somepackage` in its docs, or you tried `conda install somepackage` and conda couldn't find it, it is likely that this package is not available via the {term}`conda-forge` channel.

As a plan B, after activating your custom conda environment you can install using pip like this:
```
conda install pip
pip install somepackage
```

Things can go wrong with managing package version dependencies this way, so it's best to do this only when necessary, and only in isolated environments. See more info [here in the conda docs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#pip-in-env).
:::

---

## Summary

Conda is a package and environment management system that allows you to quickly install, run, and update packages within your work environment(s). This is important for gathering all of the tools necessary for your workflow.

We recommend installing {term}`conda` via [Miniforge](https://github.com/conda-forge/miniforge) and using it manage packages in your terminal with the `conda` command.

### What's next?

- [How to Run Python in the Terminal](terminal.md)
- [How to Run Python in a Jupyter Session](jupyter.md)

## Additional resources

- [Linux commands](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
- [conda documentation](https://docs.conda.io/en/latest/)
- [conda cheat sheet](https://docs.conda.io/projects/conda/en/stable/user-guide/cheatsheet.html#cheatsheet)
- [Miniforge](https://github.com/conda-forge/miniforge)
- [conda-forge](https://conda-forge.org)
