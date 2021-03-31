# Using the Conda Package Manager

Conda is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s).

## What are packages?

A Python package is a collection of modules, which in turn, are essentially Python files that contain published functionality. There are Python packages for data input, data analysis, data visualization, etc. Each package offers a unique toolset and may have its own unique syntax rules.

Package management is useful because you may want to update a package for one of your projects, but keep it at the same version in other projects to ensure that they continue to run as expected.

## Installing Conda

We recommmend you install Miniconda. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

Miniconda is a paired down version of Anaconda. [Installing Anaconda](https://docs.anaconda.com/anaconda/install/) takes longer and takes up more disk space, but provides you with more functionality. Anaconda comes with a Jupyter and Spyder, a Python-specific integrated development platform (IDE), installations as well as other packages. The interface of Anaconda is great if you are uncomfortable with the terminal.

## Creating a Conda environment

A conda environment is a directory that contains a collection of packages or libraries that you would like installed and accessible for this workflow. To create a new Conda environment, type `conda create --name` and the name of your environment in your terminal, and then specify any packages that you would like to have installed. For example, to install a Jupyter-ready environment, type `conda create --name sample_environment python jupyterlab`.

It is a good idea to create new environments for different projects because since Python is open source, new versions of the tools you use may become available. This is a way of guaranteeing that your script will use the same versions of packages and libraries and should run the same as you expect it to.

Some other useful Conda commands are for checking what conda environments you have (`conda env list`), activating a specific environment (`conda activate sample_environment`), checking what packages are installed inside your environment (`conda list`), and deactivating your environment (`conda deactivate`).

The Anaconda navigator offers functionality for selecting environments and installing packages into them without using the command line.
