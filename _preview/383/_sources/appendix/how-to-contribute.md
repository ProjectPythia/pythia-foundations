# Pythia Foundations Contributor's Guide

```{note}
This content is under construction!
```

General information on how to contribute to any Project Pythia repository
may be found [here][pythia contributor's guide].

A full contributor's guide will appear here, cross-referencing our tutorials on open Pull Requests on GitHub.

A simple way to comment on anything you find in this book is to use the "open issue" and "suggest edit" buttons under the GitHub Octocat logo at the top of each page. These links will take you to GitHub where the source material for the book is hosted. You'll need a free (and broadly useful) GitHub account. See
the main [Project Pythia Contributor's Guide][pythia contributor's guide].

You may also quickly provide feedback via this [Google form](https://docs.google.com/forms/d/e/1FAIpQLSeVa1TC9xM-dk7qIE2e8bsgSrIP82yYDNw3wew3J46eREJa4w/viewform?usp=sf_link).

## Contributing a new Jupyter Notebook

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
jupyter-book build .
```

Finally, you can view the book by opening the file `_build/html/index.html` with your favorite web browser. On most platforms you can simply run:

```bash
open _build/html/index.html
```

### Keeping your dev environment up to date

It's good practice to update the packages in your `pythia-book-dev` conda environment frequently to their latest versions, especially if it's been a while since you used it. If the `jupyter-book build .` command above generates error messages, that is a good indication that your conda environment may be out of date.

To update all packages in the currently activated environment to their latest versions, do this:

```bash
conda update --all
```

[pythia contributor's guide]: https://projectpythia.org/contributing.html
