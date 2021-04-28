# Python in Jupyter

You'd like to learn to run Python in a Jupyter session. Here we will cover:

- Installing Python in Jupyter
- Running Python code in Jupyter

## Installing Python in Jupyter

To run a Jupyter session you will need to install some necessary packages into your Conda environment.
You can install `miniconda`. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

Then create a Conda environment with Python installed. In the terminal type:

```
conda create --name pythia_foundations python jupyterlab nb_conda_kernels
```

Test that you have installed everything correctly by first activating your environment and then launching a Jupyter Lab session:

```
conda activate pythia_foundations
jupyter lab
```

Or you can install the full [Anaconda](https://www.anaconda.com/products/individual), and select **LAUNCH** under the Jupyter panel in the GUI.

![Anaconda Navigator](../images/Anaconda.png)

In both methods, a new window should open automatically in your default browser. You can change the browser when launching from the terminal with (for example):

```
jupyter lab —browser=chrome
```

## Running Python in Jupyter

1. With your Conda environment activated and Jupyter session launched (see above),create a directory to store our work. Let's call it `pythia-foundations`.

   You can do this either in the GUI left side bar

   ![Jupyter GUI](../images/jupyter_gui.png)

OR in the Jupyter terminal with:

![Jupyter Terminal](../images/jupyter_terminal.png)

```
$ mkdir pythia-foundations
```

2. Go into the directory:

   ```
   $ cd pythia-foundations
   ```

3. Create a new `.ipynb` file:

   Again this can be done in the GUI or the terminal.

   ![Jupyter GUI](../images/jupyter_gui.png)

   ```
   $ touch mysci.py
   ```

4. And now that you've set up our workspace, edit the `mysci.ipynb` notebook by opening it in your Jupyter session:

   ![Jupyter Notebook](../images/jupyter_notebook.png)

5. Change the script to include the classic first command - printing, "Hello, world!".

   ```python
   print("Hello, world!")
   ```

6. Run your cell with **SHIFT ENTER** and see that the results are printed below the cell.

**Congratulations!** You have just set up your first Python environment and run your first Python code in a Jupyter notebook.
