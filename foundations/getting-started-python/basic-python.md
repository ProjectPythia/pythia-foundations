# Quickstart: what is Python?

```{note}
This content is under construction!
```

This section will contain tutorials on some basics of Python syntax. We will not cover a comprehensive introduction to programming concepts, but will aim this material at people who have done at least some coding before but are new to Python.

We can use [Jupyter](jupyter) notebooks for much of the content, which will be rendered here as static pages but also be Binderized for interactive learning.

Here's a minimal example:

- [Fun with Python](Hello)

## An introduction to Python.

This section of the tutorial will focus on teaching you Python through the

### Reading a .txt File

In building your first Python script we will set up our workspace and read a `.txt` file.

1. Create a directory to store your work. We'll use the name `pythia_foundations`.

The following steps will assume you are using a Jupyter notebook. Open your Open a terminal.

On Windows, open **Anaconda Prompt**. On a Mac or Linux machine, simply open **Terminal**.

2. Activate your Conda environment:

   ```
   $ conda activate pythia_foundations
   ```

3. Create a directory to store our work. Let's call it `pythia-foundations`.

   ```
   $ mkdir pythia-foundations
   ```

4. Go into the directory:

   ```
   $ cd pythia-foundations
   ```

5. And create a data directory:

   ```
   mkdir data
   ```

6. Go into the data directory:

   ```
   $ cd data
   ```

7. Download sample data from the CU Boulder weather station:

   ```
   $ curl -kO https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt
   ```

   This weather station is a Davis Instruments wireless Vantage Pro2 located on the CU-Boulder east campus at the SEEC building (40.01 N, 05.24 W, 5250 ft elevation). The station is monitored by the Atmospheric and Oceanic Sciences (ATOC) department and is part of the larger University of Colorado ATOC Weather Network.

8. Go back to the top-level directory:

   ```
   $ cd ..
   ```

9. And now that you've set up our workspace, open a Jupyter notebook.

   ```
   jupyter lab
   ```

10. In the Jupyter session, create a blank Python script, called `mysci.py`, you can do this from the "File" drop-down menu.

11. In a code cell enter and execute the classic first command - printing, "Hello, world!".

    ```python
    print("Hello, world!")
    ```

You'll see that the cell output is executed right below each cell.

12. In a new cell, let's read the first 4 lines from our datafile.

    ```python
    # Read the data file
    filename = "data/wxobs20170821.txt"
    datafile = open(filename, 'r')

    print(datafile.readline())
    print(datafile.readline())
    print(datafile.readline())
    print(datafile.readline())

    datafile.close()

    ```

    First create a variable for your datafile name, which is a string - this can be in single or double quotes.

    Then create a variable associated with the opened file, here it is called `datafile`.

    The `'r'` argument in the open command indicates that we are opening the file for reading capabilities. Other input arguments for open include `'w'`, for example, if you wanted to write to the file.

    The readline command moves through the open file, always reading the next line.

    And remember to close your datafile.

    Comments in Python are indicated with a hash, as you can see in the first line `# Read the data file`. Comments are ignored by the interpreter.

13. In a new cell, read your whole data file:

    ```python
    # Read the data file
    filename = "data/wxobs20170821.txt"
    datafile = open(filename, 'r')

    data = datafile.read()

    datafile.close()

    # DEBUG
    print(data)
    print('data')
    ```

    Our code is similar as before, but now we've read the entire file. To test that this worked. We'll `print(data)`. Print statements in python require parenthesis around the object you wish to print, in this scenario the data object.

    Try `print('data')` as well. Now Python will print the string `data`, as it did for the hello world function, instead of the information stored in the variable data.

14. Let's read your whole data file using a context manager `with`, in a new cell:

    ```python
    # Read the data file
    filename = "data/wxobs20170821.txt"
    with open(filename, 'r') as datafile:
        data = datafile.read()

    # DEBUG
    print(data)
    ```

    Again this is a similar method of opening the datafile, but we now use `with open`. The `with` statement is a context manager that provides clean-up and assures that the file is automatically closed after you've read it.

    The indendation of the line `data = datafile.read()` is very important. Python is sensitive to white space and will not work if you mix spaces and tabs (Python does not know your tab width). It is best practice to use four spaces as opposed to tabs (tab width is not consistent between editors).

    Combined these two lines mean: with the datafile opened, I'd like to read it.

15. What did we just see? What is the data object? What type is data? How do we find out?

In a new cell print the type of our data:

    ```python
    print(type(data))
    ```

    Object types refer to `float`, `integer`, `string` or other types that you can create.

    Python is a dynamically typed language, which means you don't have to explicitly specify the datatype when you name a variable, Python will automatically figure it out by the nature of the data.

In this section you set up a workspace by creating your directory and activating your conda environment. You downloaded a .txt file and read it using the Python commands of `open()`, `readline()`, `read()`, `close()`, and `print()`, as well as the context manager `with`. You should be familiar with the `str` datatype.
