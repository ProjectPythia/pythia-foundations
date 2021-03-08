# Project Pythia Foundations

This is the source repository for the Project Pythia Foundations content collection.

The rendered site can be found (for now) at https://projectpythia.org/pythia-foundations/

The book is powered by [Jupyter Book](https://jupyterbook.org/intro.html).

## For Contributors

### Create conda environment

The first time you check out this repository, run:

```bash
$ conda env update -f environment.yml
```

This will create or update the dev environment (`pythia-book-dev`).

### `pre-commit` hooks

This repository includes `pre-commit` hooks (defined in `.pre-commit-config.yaml`). To activate/install these pre-commit hooks, run:

```bash
$ conda activate pythia-book-dev
$ pre-commit install
```

_NOTE_: The `pre-commit` package is already installed via the `pythia-book-dev` conda environment.

### Building the book locally

To build the book locally, run the following:

```bash
$ conda activate pythia-book-dev
$ jupyter-book build .
```
