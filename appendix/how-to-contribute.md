# Pythia Foundations contributor's guide

```{note}
This content is under construction!
```

General information on how to contribute to any Project Pythia repository
may be found [here](https://projectpythia.org/pages/contributing.html).

A full contributor's guide will appear here, cross-referencing our tutorials on open Pull Requests on GitHub.

A simple way to comment on anything you find in this book is to use the "open issue" and "suggest edit" buttons under the GitHub Octocat logo at the top of each page. These links will take you to GitHub where the source material for the book is hosted. You'll need a free (and broadly useful) GitHub account. See
the main [Project Pythia Contributor's Guide](https://projectpythia.org/pages/contributing.html).

## Contributing a new Jupyter Notebook

If you'd like to contribute a Jupyter Notebook to these materials, please reference our [template](template) viewable on the next page. This template is available to you in `appendix/template.ipynb` if you've cloned the repository, or available as a download [directly from GitHub](https://github.com/ProjectPythia/pythia-foundations/raw/main/appendix/template.ipynb).

Basic instructions on how to build the JupyterBook locally can be found on the README page of the book's [source repository on GitHub](https://github.com/ProjectPythia/pythia-foundations).

## Building the site

### Create a conda environment

The first time you check out this repository, run:

```bash
$ conda env update -f environment.yml
```

This will create or update the dev environment (`pythia-book-dev`).

### Install `pre-commit` hooks

This repository includes `pre-commit` hooks (defined in `.pre-commit-config.yaml`). To activate/install these pre-commit hooks, run:

```bash
$ conda activate pythia-book-dev
$ pre-commit install
```

This is also a one-time step.

_NOTE_: The `pre-commit` package is already installed via the `pythia-book-dev` conda environment.

### Building the book locally

To build the book locally, run the following:

```bash
$ conda activate pythia-book-dev
$ jupyter-book build .
```

Finally, you can view the book by opening the file `_build/html/index.html` with your favorite web browser. On most platforms you can simply run:

```
open _build/html/index.html
```

All code is licensed under Apache 2.0 (including both infrastructure code and example code in the rendered Pythia Foundations book). All other content in Pythia Foundations is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
