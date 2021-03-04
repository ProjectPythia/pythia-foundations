# Basic Python Syntax

```{note}
This content is under construction!
```

This section will contain tutorials on some basics of Python syntax. We will not cover a comprehensive introduction to programming concepts, but will aim this material at people who have done at least some coding before but are new to Python.

We can use [Jupyter](jupyter) notebooks for much of the content, which will be rendered here as static pages but also be Binderized for interactive learning.

Here's a minimal example:

- [Fun with Python](Hello)

-----------
Why Python?
-----------

You're already here because you want to learn to use Python for your data
analysis and visualizations. Python can be compared to other high-level,
interpreted, object-oriented languages, but is especially great because it is
free and open source!

High level languages:
    Other high level languages include MatLab, IDL, and NCL. The advantage of
    high level languages is that they provide functions, data structures, and
    other utilities that are commonly used, which means it takes less code to
    get real work done. The disadvantage of high level languages is that they
    tend to obscure the low level aspects of the machine such as: memory use,
    how many floating point operations are happening, and other information
    related to performance. C and C++ are all examples of lower level
    languages. The "higher" the level of language, the more computing
    fundamentals are abstracted.

Interpreted languages:
    Most of your work is probably already in interpreted languages if you've
    ever used IDL, NCL, or MatLab (interpreted languages are typically also
    high level). So you are already familiar with the advantages of this: you
    don't have to worry about compiling or machine compatability (it is
    portable). And you are probably familiar with their deficiencies: sometimes
    they can be slower than compiled languages and potentially more memory
    intensive.

Object Oriented languages:
    Objects are custom datatypes. For every custom datatype, you usually have
    a set of operations you might want to conduct. For example, if you have an
    object that is a list of numbers you might want to apply a mathematical
    operation, such as sum, onto this list object in bulk. Not every function
    can be applied to every datatype; it wouldn't make sense to apply a
    logarithm to a string of letters or to capitalize a list of numbers. Data
    and the operations applied to them are grouped together into one object.

Open source:
    Python as a language is open source which means that there is a community
    of developers behind its codebase. Anyone can join the developer community
    and contribute to deciding the future of the language. When someone
    identifies gaps to Python's abilities, they can write up the code to fill
    these gaps. The open source nature of Python means that Python as a
    language is very adaptable to shifting needs of the user community.

Python is a language designed for rapid prototyping and efficient programming.
It is easy to write new code quickly with less typing.

-------------------------
First Python Script
-------------------------

This section of the tutorial will focus on teaching you Python through the
creation of your first script.  You will learn about syntax and the reasoning
behind why things are done the way they are along the way.  We will also
incorporate lessons on the use of Git because we highly recommend you version
controling your work.

We are assuming you are familiar with bash and terminal commands. If not
`here is a cheat sheet <https://cheatography.com/davechild/cheat-sheets/linux-command-line/>`_.

~~~~~~~~~~~~~~~~~~~
Reading a .txt File
~~~~~~~~~~~~~~~~~~~

In building your first Python script we will set up our workspace, read a
:code:`.txt` file, and learn Git fundamentals.

Here is a video recording of the live tutorial covering "Reading a .txt File":

.. youtube:: Jog7ybd6amw
   :height: 315
   :width: 560
   :align: center

..

.. seealso::

   `Questions and Answers from the live "Reading a .txt File" tutorial <https://ncar.github.io/xdev/posts/python-tutorial-faq/>`_.

..

Let's begin.

1. Open a terminal.

   .. note::

      On Windows, open **Anaconda Prompt**. On a Mac or Linux machine, simply open **Terminal**.

   ..

2. Create a directory:

   .. code-block:: bash

      $ mkdir python_tutorial

   ..

   The first thing we have to do is create a directory to store our work.
   Let's call it :code:`python_tutorial`.

3. Go into the directory:

   .. code-block:: bash

      $ cd python_tutorial

4. Create a virtual environment for this project:

   .. code-block:: bash

     $ conda create --name python_tutorial python

   ..

   A conda environment is a directory that contains a collection of packages
   or libraries that you would like installed and accessible for this workflow.
   Type :bash:`conda create --name` and the name of your project, here that is
   :code:`python_tutorial`, and then specify that you would like to install Python
   in the virtual environment for this project.

   It is a good idea to create new environments for different projects because
   since Python is open source, new versions of the tools you use may become
   available. This is a way of guaranteeing that your script will use the same
   versions of packages and libraries and should run the same as you expect it
   to.

   .. seealso::

      `More information on Conda environments <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_

   ..

5. And activate your Conda environment:

   .. code-block:: bash

     $ conda activate python_tutorial

   ..

6. Make the directory a Git repository:

   .. code-block:: bash

      $ git init .

   ..

   A Git repository tracks changes made to files within your project. It looks
   like a :code:`.git/` folder inside that project.

   This command adds version control to this new python_tutorial directory
   and all of its contents.

   .. seealso::

      `More information on Git repositories <https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>`_

   ..

7. Create a data directory:

   .. code-block:: bash

      $ mkdir data

   ..

   And we'll make a directory for our data.

8. Go into the data directory:

   .. code-block:: bash

      $ cd data

9. Download sample data from the CU Boulder weather station:

   .. code-block:: bash

      $ curl -kO https://sundowner.colorado.edu/weather/atoc8/wxobs20170821.txt

   ..

   This weather station is a Davis Instruments wireless Vantage Pro2 located on
   the CU-Boulder east campus at the SEEC building (40.01 N, 05.24 W, 5250 ft
   elevation). The station is monitored by the Atmospheric and Oceanic Sciences
   (ATOC) department and is part of the larger University of Colorado ATOC
   Weather Network.

10. Check the status of your repository:

    .. code-block:: bash

       $ git status

    ..

    You will see the newly created :bash:`data` directory (which is listed as
    :bash:`./`, since you are currently *in* that directory) is listed as
    "untracked," which means all of the files you added to that directory are
    *also* untracked by Git.  The :bash:`git status` command will tell you what
    to do with untracked files. Those instructions mirror the next 2 steps:

11. Add the file to the Git staging area:

    .. code-block:: bash

       $ git add wxobs20170821.txt

    ..

    By adding this datafile to your directory, you have made a change that is
    not yet reflected in our Git repository. Every file in your working directory is classified
    by git as "untracked", "unmodified", "modified", or "staged."
    Type :bash:`git add` and then the name of the altered file to stage your change,
    i.e. moving a file that is either untracked or modified to the staged category so they can be committed.

    .. seealso::

       `More information on git add <https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository>`_

    ..

12. Check your git status once again:

    .. code-block:: bash

       $ git status

    ..

    Now this file is listed as a "change to be commited," i.e. staged. Staged
    changes can now be commited to your repository history.

13. Commit the file to the Git repository:

    .. code-block:: bash

       $ git commit -m "Adding sample data file"

    ..

    With :bash:`git commit`, you've updated your repository with all the changes
    you staged, in this case just one file.

    .. note::

       On a Windows machine you may see the following: :bash:`warning: LF will be replaced by CRLF.` The file will have its original line endings in your working directory.
       Do not worry too much about this warning. CR refers to "Carriage Return Line Feed" and LF refers to "Line Feed." Both are used to indicate line termination.
       In Windows both a Carriage Return and Line Feed are required to note the end of a line, but in Linux/UNIX only a Line Feed is required. Most text editors can account for line ending differences between opperating systems, but sometimes a conversion is necessary.
       To silence this warning you can type :bash:`git config --global core.autocrlf false` in the terminal.

    ..

14. Look at the Git logs:

    .. code-block:: bash

       $ git log

    ..

    If you type :bash:`git log` you will show a log of all the commits, or changes
    made to your repository.

15. Go back to the top-level directory:

    .. code-block:: bash

       $ cd ..

    ..

16. And now that you've set up our workspace, create a blank Python script,
    called :code:`mysci.py`:

    .. code-block:: bash

       $ touch mysci.py

    ..

    .. note::

       If you are working on a Windows machine it is possible that :bash:`touch` will not be
       recognized as an internal or external command. If this is the case, run
       :bash:`conda install m2-base` to enable unix commands such as :bash:`touch`.

    ..

17. Edit the :code:`mysci.py` file using nano, vim, or your favorite text editor:

    .. code-block:: python
       :linenos:

       print("Hello, world!")

    ..

    Your classic first command will be to print :python:`Hello, world!`.

    .. note::

       On a Windows machine, it is possible `nano` or `vim` are not recognized as text editors within your terminal. In this case simply try to run `mysci.py` to open a notepad editor.

    ..

18. Try testing the script by typing :bash:`python` and then the name of your script:

    .. code-block:: bash

       $ python mysci.py

    ..

    **Yay!** You've just created your first Python script.


19. You probably won't need to run your Hello World script again, so delete the
    :python:`print("Hello, world!")` line and start over with something more useful -
    we'll read the first 4 lines from our datafile.

    Change the :code:`mysci.py` script to read:

    .. code-block:: python
       :linenos:

       # Read the data file
       filename = "data/wxobs20170821.txt"
       datafile = open(filename, 'r')

       print(datafile.readline())
       print(datafile.readline())
       print(datafile.readline())
       print(datafile.readline())

       datafile.close()

    ..

    First create a variable for your datafile name, which is a string - this
    can be in single or double quotes.

    Then create a variable associated with the opened file, here it is called
    :python:`datafile`.

    The :python:`'r'` argument in the open command indicates that we are opening
    the file for reading capabilities. Other input arguments for open include
    :python:`'w'`, for example, if you wanted to write to the file.

    The readline command moves through the open file, always reading the next
    line.

    And remember to close your datafile.

    Comments in Python are indicated with a hash, as you can see in the first
    line :python:`# Read the data file`. Comments are ignored by the interpreter.

    .. seealso::

       `More information on the open() function <https://docs.python.org/3/library/functions.html#open>`_

    ..

20. And test your script again by typing:

    .. code-block:: bash

       $ python mysci.py

    ..

    Testing of your script with :bash:`python mysci.py` should be done every time
    you wish to execute the script. This will no longer be specified as a
    unique step in between every change to our script.

21. Change the :code:`mysci.py` script to read your whole data file:

    .. code-block:: python
       :linenos:

       # Read the data file
       filename = "data/wxobs20170821.txt"
       datafile = open(filename, 'r')

       data = datafile.read()

       datafile.close()

       # DEBUG
       print(data)
       print('data')

    ..

    Our code is similar as before, but now we've read the entire file. To
    test that this worked. We'll :python:`print(data)`. Print statements in python
    require parenthesis around the object you wish to print, in this scenario the data object.

    Try :python:`print('data')` as well. Now Python will print the string
    :code:`data`, as it did for the hello world function, instead of the
    information stored in the variable data.

    Don't forget to execute with :bash:`python mysci.py`.

22. Change the :code:`mysci.py` script to read your whole data file using a context
    manager with:

    .. code-block:: python
       :linenos:

       # Read the data file
       filename = "data/wxobs20170821.txt"
       with open(filename, 'r') as datafile:
          data = datafile.read()

       # DEBUG
       print(data)

    ..

    Again this is a similar method of opening the datafile, but we now use :python:`with open`.
    The :python:`with` statement is a context manager that provides clean-up and
    assures that the file is automatically closed after you've read it.

    The indendation of the line :python:`data = datafile.read()` is very important.
    Python is sensitive to white space and will not work if you mix spaces and
    tabs (Python does not know your tab width). It is best practice to use
    spaces as opposed to tabs (tab width is not consistent between editors).

    Combined these two lines mean: with the datafile opened, I'd like to read
    it.

    And execute with :bash:`python mysci.py`.

    .. seealso::

       `More information on context managers <https://book.pythontips.com/en/latest/context_managers.html>`_

    ..

23. What did we just see? What is the data object? What type is data? How do we
    find out?

    Change the DEBUG section of our script to:

    .. code-block:: python
       :lineno-start: 6

       # DEBUG
       print(type(data))

    ..

    And execute with :bash:`python mysci.py`

    Object types refer to :python:`float`, :python:`integer`, :python:`string`
    or other types that you can create.

    Python is a dynamically typed language, which means you don't have to
    explicitly specify the datatype when you name a variable, Python will
    automatically figure it out by the nature of the data.

24. Now, clean up the script by removing the DEBUG section, before we commit
    this to Git.

25. Let's check the status of our Git repository

    .. code-block:: bash

       $ git status

    ..

    .. note::

       Take a look at which files have been changed in the repository!

    ..

26. Stage these changes:

    .. code-block:: bash

       $ git add mysci.py

    ..

27. Let's check the status of our Git repository,again. What's different from
    the last time we checked the status?

    .. code-block:: bash

       $ git status

    ..

28. Commit these changes:

    .. code-block:: bash

       $ git commit -m "Adding script file"

    ..

    Here a good commit message :code:`-m` for our changes would be
    :code:`"Adding script file"`

29. Let's check the status of our Git repository, now. It should tell you that
    there are no changes made to your repository (i.e., your repository is
    up-to-date with the state of the code in your directory).

    .. code-block:: bash

       $ git status

    ..

30. Look at the Git logs, again:

    .. code-block:: bash

       $ git log

    ..

    You can also print simplified logs with the :code:`--oneline` option.

-----

That concludes the first lesson of this virtual tutorial.

In this section you set up a workspace by creating your directory, conda
environment, and git repository. You downloaded a .txt file and read it using
the Python commands of :python:`open()`, :python:`readline()`, :python:`read()`,
:python:`close()`, and :python:`print()`, as well as the context manager
:python:`with`. You should be familiar with the :python:`str` datatype. You
also used fundamental git commands such as :bash:`git init`, :bash:`git status`,
:bash:`git add`, :bash:`git commit`, and :bash:`git log`.


.. seealso::

   - `Conda environments <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>`_
   - `Git repositories <https://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository>`_
   - `The open() function <https://docs.python.org/3/library/functions.html#open>`_
   - `Context managers <https://book.pythontips.com/en/latest/context_managers.html>`_

..
