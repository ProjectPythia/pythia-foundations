# Basic Python Syntax

```{note}
This content is under construction!
```

This section will contain tutorials on some basics of Python syntax. We will not cover a comprehensive introduction to programming concepts, but will aim this material at people who have done at least some coding before but are new to Python.

We can use [Jupyter](jupyter) notebooks for much of the content, which will be rendered here as static pages but also be Binderized for interactive learning.

Here's a minimal example:

- [Fun with Python](Hello)

## The Road to Python

What brings you here? Are you a scientist who knows how to code, but not in Python? Are you new to coding entirely? Do you have a specific problem you are trying to solve?

## Why Python?

You're already here because you want to learn to use Python for your data analysis and visualizations. Python can be compared to other high-level, interpreted, object-oriented languages, but is especially great because it is free and open source!

**High level languages:**
Other high level languages include MatLab, IDL, and NCL. The advantage of high level languages is that the provide functions, data structures, and other utilities that are commonly used, which means it takes less code to get real work done. The disadvantage of high level languages is that they tend to obscure the low level aspects of the machine such as: memory use, how many floating point operations are happening, and other information related to performance. C and C++ are all examples of lower level languages. The "higher" the level of language, the more computing fundamentals are abstracted.

**Interpreted languages:**
Most of your work is probably already in interpreted languages if you've ever used IDL, NCL, or MatLab (interpreted languages are typically also high level). So you are already familiar with the advantages of this: you don't have to worry about compiling or machine compatability (it is portable). And you are probably familiar with their deficiencies: sometimes they can be slower than compiled languages and potentially more memory intensive.

**Object Oriented languages:**
Objects are custom datatypes. For every custom datatype, you usually have a set of operations you might want to conduct. For example, if you have an object that is a list of numbers you might want to apply a mathematical operation, such as sum, onto this list object in bulk. Not every function can be applied to every datatype; it wouldn't make sense to apply a logarithm to a string of letters or to capitalize a list of numbers. Data and the operations applied to them are grouped together into one object.

**Open source:**
Python as a language is open source which means that there is a community of developers behind its codebase. Anyone can join the developer community and contribute to deciding the future of the language. When someone identifies gaps to Python's abilities, they can write up the code to fill these gaps. The open source nature of Python means that Python as a language is very adaptable to shifting needs of the user community.

Python is a language designed for rapid prototyping and efficient programming. It is easy to write new code quickly with less typing.

## Chosing a Python Platform

Through is no single official platform for the Python language. You can run Python from the terminal command line, through a Jupyter session, in Spyder, and in your favorite IDE (integraged develpment platform). Here we will briefly review each interface and how to choose. In general, it is always best to test your programs in the same environment in which they will be run. The biggest factors to consider when chosing your platform are:

1. What are you already comfortable with?
2. What are the people around you using (peers, coworkers, instructors, etc)?

### Terminal

There are a few reasons one might chose to run Python in the terminal. For learners who are familiar with basic [Linix commands](https://cheatography.com/davechild/cheat-sheets/linux-command-line/).and text editors, this is the quickest route to learn Python syntax without the having to cover the bells and whistles of your new platform. If you are runing Python on a super computer, through an HTTP request, or ssh tunneling you might want to consider learning in the terminal.

### Jupyter Session

Jupyter Notebooks are very popular among data scientists. It is a free, open-source, interactive tool that allows you to run Python code in "cells." This means that your workflow can alternate between code, output, and even Markdown-formatted explanatory sections that create an easy to follow analysis from start to finish. Jupyter notebooks are a great option for presentations or learning tools. For this reason many of the lessons in this book will be taught via Jupyter.

### Spyder

Spyder is a Python specific IDE that comes with the Anaconda download. It is perhaps the most familiar IDE if you are coming from languages such as Matlab that have a language specific platform. Many classes at universities are taught in the Spyder interface.

### Other IDEs

If you already code in other languages you might already have a favorite IDE, such as Visual Studio Code, that will work just as well in Python. PyCharm is an IDE that is very popular and Python-specific.

## Installation

The installation may look slightly different depending on the Python platform you are using. Please follow the instructions underneath the platform you chosee.

### Terminal

If running Python in the terminal it is best to install Miniconda. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

Then create a Conda environment with Python installed by typing the following into your terminal:
`conda create --name pythia-foundations python`

A conda environment is a directory that contains a collection of packages or libraries that you would like installed and accessible for this workflow. Type `conda create --name` and the name of your environment, and then specify that you would like to install Python in the virtual environment for this project.

It is a good idea to create new environments for different projects because since Python is open source, new versions of the tools you use may become available. This is a way of guaranteeing that your script will use the same versions of packages and libraries and should run the same as you expect it to.

### Jupyter Session

To run a Jupyter session you will need to install some necessary packages into your Conda environment.
You can install `miniconda`. You can do that by following the [instructions for you machine](https://docs.conda.io/en/latest/miniconda.html).

Then create a Conda environment with Python installed.
`conda create --name pythia-foundations python jupyterlab nb_conda_kernels`

Or you can install the full [Anaconda](https://www.anaconda.com/products/individual), and select Jupyter in the GUI. **have a screenshot of that here**

### Spyder

Install the full [Anaconda](https://www.anaconda.com/products/individual), and select Spyder in the GUI. **have a screenshot of that here**

### Other IDEs

**Add notes or links to documentation for each IDE.**

## First Python Script in the Terminal

This section of the tutorial will focus on teaching you Python through the creation of your first script. I think I want to review how to execute Python in each cell, and then change this document to be platform agnostic.

### Reading a .txt File

In building your first Python script we will set up our workspace and read a `.txt` file.

1. Open a terminal.

   On Windows, open **Anaconda Prompt**. On a Mac or Linux machine, simply open **Terminal**.

2. Activate your Conda environment:

   ```
   $ conda activate pythia_foundations
   ```

3. Create a directory to store our work. Let's call it `pythia_foundations`.

   ```
   $ mkdir pythia_foundations
   ```

4. Go into the directory:

   ```
   $ cd python_tutorial
   ```

5. And create a data directory:

```
mkdir data
```

6. Go into the data directory:
   `

```
$ cd data
```

7. Download sample data from the CU Boulder weather station:

```
$ curl -kO https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt
```

This weather station is a Davis Instruments wireless Vantage Pro2 located on the CU-Boulder east campus at the SEEC building (40.01 N, 05.24 W, 5250 ft elevation). The station is monitored by the Atmospheric and Oceanic Sciences (ATOC) department and is part of the larger University of Colorado ATOC Weather Network.

7. Go back to the top-level directory:

```
$ cd ..
```

8. And now that you've set up our workspace, create a blank Python script, called `mysci.py`:

```
$ touch mysci.py
```

If you are working on a Windows machine it is possible that `touch` will not be recognized as an internal or external command. If this is the case, run `conda install m2-base` to enable unix commands such as `touch`.

9. Edit the `mysci.py` file using nano, vim, or your favorite text editor to include the classic first command - printing, "Hello, world!".

```python
print("Hello, world!")
```

On a Windows machine, it is possible `nano` or `vim` are not recognized as text editors within your terminal. In this case simply try to run `mysci.py` to open a notepad editor.

10. To run a Python script from the command line type, "python" and then the name of your script:

```
$ python mysci.py
```

11. You probably won't need to run your Hello World script again, so delete the `print("Hello, world!")` line and start over with something more useful - we'll read the first 4 lines from our datafile.

Change the `mysci.py` script to read:

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

12. Run your script by typing:

```
$ python mysci.py
```

Testing of your script with `python mysci.py` should be done every time you wish to execute the script. This will no longer be specified as a unique step in between every change to our script.

13. Change the `mysci.py` script to read your whole data file:

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

Don't forget to execute with :bash:`python mysci.py`.

14. Change the `mysci.py` script to read your whole data file using a context
    manager with:

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

And execute with `python mysci.py`.

15. What did we just see? What is the data object? What type is data? How do we find out?

Change the DEBUG section of our script to:

```python
# DEBUG
print(type(data))
```

And execute with `python mysci.py`.

Object types refer to `float`, `integer`, `string` or other types that you can create.

Python is a dynamically typed language, which means you don't have to explicitly specify the datatype when you name a variable, Python will automatically figure it out by the nature of the data.

In this section you set up a workspace by creating your directory and activating your conda environment. You downloaded a .txt file and read it using the Python commands of `open()`, `readline()`, `read()`, `close()`, and `print()`, as well as the context manager `with`. You should be familiar with the `str` datatype.
