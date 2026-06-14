# Contributing to Foundations

General information on how to contribute to any Project Pythia repository
may be found in the [Contributing to Project Pythia](https://projectpythia.org/contributing) guide.

As GitHub {term}`pull request`s are an important part of contributing to Pythia, this guide will cross-reference tutorials from our chapters on [Getting Started with GitHub](../foundations/getting-started-github.md).

A quick and easy way to find the Pythia Foundations source repository on GitHub while you are browsing the book is to look for the GitHub Octocat logo near the top right of each page. This will link directly to our [main source repository on GitHub](https://github.com/ProjectPythia/pythia-foundations). 

In order to [open issues](../foundations/github/github-issues.md) or create [pull requests](../foundations/github/github-pull-request.md) to suggest changes, you must have a [free GitHub account](../foundations/github/what-is-github.md). This guide is strictly for Pythia Foundations; for general Project Pythia contribution guidelines, see the main guide for [Contributing to Project Pythia](https://projectpythia.org/contributing).

To quickly provide feedback about minor issues without the use of GitHub, you can also use this [Google Form](https://docs.google.com/forms/d/e/1FAIpQLSeVa1TC9xM-dk7qIE2e8bsgSrIP82yYDNw3wew3J46eREJa4w/viewform?usp=sf_link).

## Contributing a new Jupyter notebook

If you'd like to contribute a Jupyter Notebook to these materials, please reference our [template](template) viewable on the next page. This template is available to you in `appendix/template.ipynb` if you've cloned the [source repository](https://github.com/ProjectPythia/pythia-foundations), or available as a download [directly from GitHub](https://github.com/ProjectPythia/pythia-foundations/raw/main/appendix/template.ipynb).

## Building the site

### Create a conda environment

The first time you check out this repository, run:

```bash
conda env update -f environment.yml
```

This will create or update the dev environment (`pythia-book-dev`).

### Install `pre-commit` hooks

This repository includes `pre-commit` hooks (defined in `.pre-commit-config.yaml`). To activate/install these pre-commit hooks, run:

```bash
conda activate pythia-book-dev
pre-commit install
```

This is also a one-time step.

_NOTE_: The `pre-commit` package is already installed via the `pythia-book-dev` conda environment.

### Building the book locally

To build the book locally, run the following:

```bash
conda activate pythia-book-dev
myst start --execute
```

Finally, you can view the book by opening the localhost link that should be generated in your terminal.

### Keeping your dev environment up to date

It's good practice to update the packages in your `pythia-book-dev` conda environment frequently to their latest versions, especially if it's been a while since you used it. If the `myst start --execute` command above generates error messages, that is a good indication that your conda environment may be out of date.

To update all packages in the currently activated environment to their latest versions, do this:

```bash
conda update --all
```

[Contributing to Project Pythia]: https://projectpythia.org/contributing
