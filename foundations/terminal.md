# Python in the Terminal

You'd like to learn to run Python in the terminal. Here we will cover:

- Installing Python in the terminal
- Running Python code in the terminal

## Installing Python in the Terminal

If running Python in the terminal, it is best to install Miniconda. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

[Learn more about Conda here](conda.md)

Then create a Conda environment with Python installed by typing the following into your terminal:

```
$ conda create --name pythia_foundations_env python
```

You can test this by running `python` in the command line.

## Running Python in the Terminal

On Windows, open **Anaconda Prompt**. On a Mac or Linux machine, simply open **Terminal**.

1. Activate your Conda environment:

   ```
   $ conda activate pythia_foundations_env
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
   $ nano mysci.py
   ```

6. Change the script to include the classic first command - printing, "Hello, world!".

   ```python
   print("Hello, world!")
   ```

7. In the terminal, execute your script:

   ```
   $ python mysci.py
   ```

**Congratulations!** You have just set up your first Python environment and run your first Python script in the terminal.
