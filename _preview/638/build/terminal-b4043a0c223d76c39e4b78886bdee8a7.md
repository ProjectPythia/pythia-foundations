# Python in the Terminal

---

## Overview

You'd like to learn to run Python in the terminal. You also want to jump right in with some installation quick-start guidance before reading through our detailed chapter on [Installing and Managing Python with Conda](conda.md). This chapter is for you!

If you're more interested in jumping into {term}`Jupyter Notebook`s, feel free to skip ahead to the [next chapter](jupyter.md).

## Prerequisites

| Concepts                                                                                                  | Importance | Notes |
| --------------------------------------------------------------------------------------------------------- | ---------- | ----- |
| [Choosing a Python Platform](how-to-run-python.md) | Helpful    |       |

:::{tip} Time to learn
20 minutes
:::

---

## Installing Python with Miniforge: quickstart

If you are running Python in the terminal, it is best to install {term}`Miniforge`. You can do that by following the [instructions for your machine](https://github.com/conda-forge/miniforge).

:::{tip}For Windows users
When [installing Miniforge using the Windows installer](https://conda-forge.org/download/), make sure to check "Create start menu shortcuts (supported packages only)". Then in your start menu or search box, you will find the "Miniforge Prompt", where you will enter commands.
:::

:::{seealso}
More details about conda are provided in a later section ([Installing and Managing Python with conda](conda.md)). For now, we will introduce its basic functionality.
:::

Then create a {term}`conda` environment with Python installed by typing the following into your terminal:

```
conda create --name pythia_test_env python
```

You can test this by running `python` in the command line.

## Running Python in the Terminal

On Windows, open **Miniforge Prompt**. On a Mac or Linux machine, open **Terminal**.

1. Activate your conda environment:

   ```
   conda activate pythia_test_env
   ```

2. Create a directory to store our work. Let's call it `pythia_test`.

   ```
   mkdir pythia_test
   ```

3. Go into the directory:

   ```
   cd pythia_test
   ```

4. Create a new Python file:

   ```
   touch mysci.py
   ```
   On Windows:

   ```
   type nul > mysci.py
   ```

5. And now that you've set up our workspace, edit the `mysci.py` script using your favorite text editor (e.g., [nano](wiki:GNU_nano)):

   ```
   nano mysci.py
   ```
    On Windows, a quick option is to edit on Notepad:

   ```
   notepad mysci.py
   ```

6. Change the script to include the classic first command: printing, "Hello, world!".

   ```python
   print("Hello, world!")
   ```

7. Save your file and exit the editor. How to do this is dependent on your chosen text editor.

   - In [Vim](wiki:Vim_(text_editor)), revert to command mode by pressing `esc`. Then, the command is `:wq`.
   - In nano it is {kbd}`Ctrl`\+{kbd}`O` to save and {kbd}`Ctrl`\+{kbd}`X` to exit (where you will be prompted if you want to save it, if modified).
   - In Notepad, {kbd}`Ctrl`\+{kbd}`S` and close the window.

8. In the terminal, execute your script:

   ```
   python mysci.py
   ```

**Congratulations!** You have just set up your first Python environment and run your first Python script in the terminal.

---

## Summary

Running Python in the terminal is a good option if you are familiar with Linux commands or scripting on a supercomputer. It requires the use of a text editor.

### What's next?

- [How to Run Python in a Jupyter Session](jupyter.md)
- [Learn more about conda here](conda.md)

## Additional resources

- [Linux commands](https://cheatography.com/davechild/cheat-sheets/linux-command-line/)
