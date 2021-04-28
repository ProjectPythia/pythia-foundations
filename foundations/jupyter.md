# Python in Jupyter

You'd like to learn to run Python in a Jupyter session. Here we will cover:

- Installing Python in Jupyter
- Running Python code in Jupyter

## Installing Python in Jupyter

To run a Jupyter session you will need to install some necessary packages into your Conda environment.
You can install `miniconda`. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

Then create a Conda environment with Python installed.

```
conda create --name pythia_foundations python jupyterlab nb_conda_kernels
```

Or you can install the full [Anaconda](https://www.anaconda.com/products/individual), and select **LAUNCH** under the Jupyter panel in the GUI.

![Anaconda Navigator](../images/Anaconda.png)

Test that you have installed everything correctly by first activating your environment:

```
conda activate pythia_foundations
jupyter lab
```

A new window should open automatically in your default browser. You can change the browser with (for example):

```
jupyter lab —browser=chrome
```

## Running Python in Jupyter

You can test that this by running `python` in the command line.

## Running Python in Jupyter

On Windows, open **Anaconda Prompt**. On a Mac or Linux machine, simply open **Terminal**.

1. Activate your Conda environment:

   ```
   $ conda activate pythia_foundations
   ```

2. Create a directory to store our work. Let's call it `pythia-foundations`.

   ```
   $ mkdir pythia-foundations
   ```

3. Go into the directory:

   ```
   $ cd pythia-foundations
   ```

4. Create a new Python file:

   ```
   $ touch mysci.py
   ```

5. And now that you've set up our workspace, edit the `mysci.py` script using your favorite text editor (nano, e.g.):

   ```
   nano mysci.py
   ```

6. Change the script to include the classic first command - printing, "Hello, world!".

   ```python
   print("Hello, world!")
   ```

7. In the terminal, execute your script:

   ```
   python mysci.py
   ```

**Congratulations!** You have just set up your first Python environment and run your first Python script in the terminal.
