# Project Pythia Foundations

This is the source repository for the Project Pythia Foundations content collection.

The rendered site can be found at https://foundations.projectpythia.org

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

All code is licensed under Apache 2.0 (including both infrastructure code and example code in the rendered Pythia Foundations book). All other content in Pythia Foundations is licensed under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)
