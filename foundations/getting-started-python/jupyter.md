# Running Python in Jupyter

You'd like to learn Python in Jupyter. Here we will cover:

- Installing Python in the Jupyter
- Running Python code in the Jupyter

## Installing Python for Jupyter

To run a Jupyter session you will need to install some necessary packages into your Conda environment.
You can install `miniconda`. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

Then create a Conda environment with Python installed.
`conda create --name pythia_foundations python jupyterlab nb_conda_kernels`

Or you can install the full [Anaconda](https://www.anaconda.com/products/individual), and select Jupyter in the GUI. **have a screenshot of that here**

Test that you have installed everything correctly by activating your environment with `conda activate pythia_foundations` and running `jupyter lab`.

A new window should open automatically in your default browser. You can change the browser with `jupyter lab —browser=chrome`.

## Running Python in Jupyter
