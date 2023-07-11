# Python in the Terminal

---

## Overview

You'd like to learn to run Python in the terminal. Here we will cover:

1.  Installing Python in the terminal
2.  Running Python code in the terminal

## Prerequisites

| Concepts                                                                                                  | Importance | Notes |
| --------------------------------------------------------------------------------------------------------- | ---------- | ----- |
| [Installing and Running Python](https://foundations.projectpythia.org/foundations/how-to-run-python.html) | Helpful    |       |

- **Time to learn**: 20 minutes

---

## Installing Python in the Terminal

If you are running Python in the terminal, it is best to install Miniconda. You can do that by following the [instructions for your machine](https://docs.conda.io/en/latest/miniconda.html).

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

5. And now that you've set up our workspace, edit the `mysci.py` script using your favorite text editor (e.g., nano):

   ```
   $ nano mysci.py
   ```

6. Change the script to include the classic first command: printing, "Hello, world!".

   ```python
   print("Hello, world!")
   ```

7. Save your file and exit the editor. How to do this is dependent on your chosen text editor.

   - In Vim, revert to command mode by pressing `esc`. Then, the command is `:wq`.
   - In Nano it is {kbd}`Ctrl`\+{kbd}`O` to save and {kbd}`Ctrl`\+{kbd}`X` to exit (where you will be prompted if you want to save it, if modified).

8. In the terminal, execute your script:

   ```
   $ python mysci.py
   ```

**Congratulations!** You have just set up your first Python environment and run your first Python script in the terminal.

---

## Summary

Running Python in the terminal is a good option if you are familiar with Linux commands or scripting on a supercomputer. It requires the use of a text editor.

### What's Next?

- [How to Run Python in a Jupyter Session](jupyter.md)
- [Learn more about Conda here](conda.md)

## Resources and References

- [Linux commands](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
