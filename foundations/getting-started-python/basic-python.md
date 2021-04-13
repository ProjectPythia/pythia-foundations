# Quickstart: what is Python?

```{note}
This content is under construction!
```

This section will contain tutorials on some basics of Python syntax. We will not cover a comprehensive introduction to programming concepts, but will aim this material at people who have done at least some coding before but are new to Python.

We can use [Jupyter](jupyter) notebooks for much of the content, which will be rendered here as static pages but also be Binderized for interactive learning.

Here's a minimal example:

- [Fun with Python](Hello)

## An introduction to Python.

This section of the tutorial will focus on teaching you Python through in a Jupyter notebook.

If you are using a terminal, you will need to edit your script in a text editor and execute with the command "python SCRIPTNAME.PY".

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

9. And now that you've set up our workspace, open a Jupyter notebook called `mysci.ipynb`.

   ```
   jupyter lab
   ```

   Then, in the Jupyter session, create a blank notebook from the "File" drop-down menu.

10. In a code cell enter and execute the classic first command - printing, "Hello, world!".

    ```python
    print("Hello, world!")
    ```

    You'll see that the cell output is executed right below each cell.

11. In a new cell, let's read the first 4 lines from our datafile.

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

12. In a new cell, read your whole data file:

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

13. Let's read your whole data file using a context manager `with`, in a new cell:

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

14. What did we just see? What is the data object? What type is data? How do we find out?

    In a new cell print the type of our data:

    ```python
    print(type(data))
    ```

    Object types refer to `float`, `integer`, `string` or other types that you can create.

    Python is a dynamically typed language, which means you don't have to explicitly specify the datatype when you name a variable, Python will automatically figure it out by the nature of the data.

In this section you set up a workspace by creating your directory and activating your conda environment. You downloaded a .txt file and read it using the Python commands of `open()`, `readline()`, `read()`, `close()`, and `print()`, as well as the context manager `with`. You should be familiar with the `str` datatype.

---

## Creating a Data Dictionary

You have just commited your new script file that reads in the data from a file as a string. You will now manipulate your data into a more usable format - a dictionary. In doing so you will learn how to write iterative for loops and about Python data structures.

1. One big string isn't very useful, so use `str.split()` to parse the data file into a data structure you can use.

   With your `mysci.ipynb` Jupyter notebook open and `python_tutorial` environment activated, add a new code cell:

   ```python
   # Initialize my data variable
   data = []

   # Read and parse the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:

      # Read the first three lines (header)
      for _ in range(3):
         datafile.readline()

      # Read and parse the rest of the file
      for line in datafile:
         datum = line.split()
         data.append(datum)

   # DEBUG
   for datum in data:
      print(datum)
   ```

   The first thing that is different in this code block is an initialized data variable; `data = []` creates the variable data as an empty `list` which we will populate as we read the file. Python `list` objects are a collection data type that contain ordered and changeable - meaning you can call information out of the `list` by its index and you can add or delete elements to your `list`. Lists are denoted by square brackets, `[]`.

   Then with the datafile open for reading capabilities, we are going to write two separate `for` loops. A `for` loop is used for iterating over a sequence (such as a list). It is important to note the syntax of Python `for` loops: the `:` at the end of the `for` line, the tab-indentation of all lines within the `for` loop, and perhaps the absence of an `end for` that is found in languages such as Matlab.

   In your first `for` loop, loop through the dummy variable `_` in `range(3)`. The `range` function returns a sequence of numbers, starting at 0 and incrementing by 1 (by default), ending at the specified length. Here if you were to `print(_)` on each line of the for loop you would see:

   ```
      0
      1
      2
   ```

   Try it out in a new cell, if you are unsure of how this works. Here the `_` variable is a placeholder, meaning the variable is never called within the loop.

   So again, in the first `for` loop, you execute the `readline` command (which you will remember moves down to the next line each time it is consecutively called) 3 times to read through the file header (which is 3 lines long).

   **Yay!** You have just written your first `for` loop!

   Then in a second `for` loop, you loop through lines in the remainder of your datafile. On each line, split it along white space. The `string.split()` method splits a string into a list on a specified separator, the default being white space. You could use any character you like, but other useful options are `/t` for splitting along tabs or `,` along commas.

   Then you `append` this split line list to the end of your data `list`. The `list.append()` method adds a single item to the end of your `list`. After every line in your `for` loop iteration, the data `list` that was empty is one element longer. Now we have a `list` of `list`\s for our data variable - a `list` of the data in each line for multiple lines.

   When you print each datum in data, you'll see that each datum is a `list` of `string` values.

   We just covered a lot of Python nuances in a very little bit a code!

2. Now, to practice list indexing, get the first, 10th, and last row in data in a new code cell:

   ```
   print(data[0])
   print(data[9])
   print(data[-1])
   ```

   Index your list by adding the number of your index in square brackets, `[]`, after the name of the `list`. Python is 0-indexed so `data[0]` refers to the first index and `[-1]` refers to the last index.

3. Now, to practice slice indexing, get the first 10 rows in data in a new code cell:

   ```
   for datum in data[0:10]:
      print(datum)
   ```

   Using a colon, `:`, between two index integers `a` and `b`, you get all indexes between `a` and `b`. See what happens when you print `data[:10]`, `data[0:10:2]`, and `data[slice(0,10,2)]`. What's the difference?

4. Now, to practice nested indexing, get the 5th, the first 5, and every other column of row 9 in the data object.

   ```
   print(data[8][4])
   print(data[8][:5])
   print(data[8][::2])
   ```

   In nested `list` indexing, the first index determines the row, and the second determines the element from that row. Also try printing `data[5:8][4]`, why doesn't this work?

5. Can you remember which column is which? Is time the first column or the second? Which column is the temperature?

   Each column is a time-series of data. We would ideally like each time-series easily accessible, which is not the case when data is row-column ordered (like it currently is). (Remember what happens when you try to do something like `data[:][4]`!)

   Let's get our data into a more convenient named-column format.

   ```
   # Initialize my data variable
   data = {'date': [],
   'time': [],
   'tempout': []}

   # Read and parse the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:

      # Read the first three lines (header)
      for _ in range(3):
         datafile.readline()

      # Read and parse the rest of the file
      for line in datafile:
         split_line = line.split()
         data['date'].append(split_line[0])
         data['time'].append(split_line[1])
         data['tempout'].append(split_line[2])

   # DEBUG
   print(data['time'])
   ```

   First we'll initialize a dictionary, `dict`, indicated by the curly brackets, `{}`. Dictionaries, like `list`\s, are changeable, but they are unordered. They have keys, rather than positions, to point to their elements. Here you have created 3 elements of your dictionary, all currently empty `list`\s, and specified by the keys `date`, `time`, and `tempout`. Keys act similarly to indexes: to pull out the `tempout` element from data you would type `data['tempout']`.

   Grab date (the first column of each line), time (the second column of each line), and temperature data (the third column), from each line and `append` it to the `list` associated with each of these data variables.

6. Now it's easy to get the time-series information for each column that we are interested in grabbing, and we can get each column by name. However, everything read from the text file is a `str`. What if we want to do math on this data, then we need it to be a different data type!

   So, let's convert the tempout time-series to be a `float` by changing the line:

   ```
   data['tempout'].append(split_line[2])
   ```

   to:

   ```
   data['tempout'].append(float(split_line[2]))
   ```

   The `float` datatype refers to floating point real values - the datatype of any numbers with values after a decimal point. You could also change the datatype to `int`, which will round the values down to the closest full integer.

7. `print(data['tempout'])`

   Do you see a difference? It should now be a list of floats.

8. This seems great, so far! But what if you want to read more columns to ourdata later? You would have to change the initialization of the data variable (at the top of `mysci.py`\) and have to add the appropriate line in the "read and parse" section. Essentially, that means you need to maintain 2 parts of the code and make sure that both remain consistent with each other.

   This is generally not good practice. Ideally, you want to be able to change only one part of the code and know that the rest of the code will remain consistent. So, let's fix this.

   ```
   # Column names and column indices to read
   columns = {'date': 0, 'time': 1, 'tempout': 2}

   # Data types for each column (only if non-string)
   types = {'tempout': float}

   # Initialize my data variable
   data = {}
   for column in columns:
      data[column] = []

   # Read and parse the data file
   filename = "data/wxobs20170821.txt"
   with open(filename, 'r') as datafile:

      # Read the first three lines (header)
      for _ in range(3):
         datafile.readline()

      # Read and parse the rest of the file
      for line in datafile:
         split_line = line.split()
         for column in columns:
            i = columns[column]
            t = types.get(column, str)
            value = t(split_line[i])
            data[column].append(value)

      # DEBUG
      print(data['tempout'])

   ```

   You have now created a columns `dict` that points each data variable to its column-index. And a types `dict`, that indicates what type to convert the data when necessary. When you want new variables pulled out of the datafile, change these two variables.

   Initializing the data `dict` now includes a `for` loop, where for each variable specified in columns, that key is initialized pointing to an empty `list`. This is the first time you have looped over a `dict` and added key-value pairs to a `dict` via assignment.

   When reading and parsing the file, you created your first nested `for` loop. For every line of the datafile, split that line - and then for every desired variable in the columns `dict` (date, time, tempout): grab the datum from the current split line with the specified index (0, 1, 2), use the `dict.get()` method to find the desired datatype if specified (avoiding `key-not-found` errors and defaulting to `str` if unspecified), convert the datum to the desired datatype, and `append` the datum to the `list` associated with each column key within the data `dict`.

---

In this section you saved the variables of date, time, and tempout in a data dictionary.

You should now be familiar with the data structures `list`\s (as well as list indexing, nested lists, and the command `list.append()`), `dict`\s (their keys and the command `dict.get()`), and `range`\s. You also learned to write `for` loops, about the `float` datatype, and using the Python commands `str.split()`.

## Writing Functions

You have just commited your new script that reads the file, saving the variables of date, time, and tempout in a data dictionary. In this section you will compute wind chill index by writing your first function and learning about basic math operators.

1. Now that you've read the data in a way that is easy to modify later, it is time to actually do something with the data.

   Compute the wind chill factor, which is the cooling effect of the wind. As wind speed increases the rate at which a body loses heat increases. The formula for this is:

   $$WCI = a + (b t) - (c v^{0.16}) + (d t v^{0.16})$$

   Where _WCI_ refers to the Wind Chill in degrees F, _t_ is temperature in degrees F, _v_ is wind speed in mph, and the other variables are as follows: _a_ = 35.74, _b_ = 0.6215, _c_ = 35.75, and _d_ = 0.4275. Wind Chill Index is only defined for temperatures within the range -45 to +45 degrees F.

   You've read the temperature data into the tempout variable, but to do this calculation, you also need to read the windspeed variable from column 7.

   With your terminal open and :code:`python_tutorial` environment activated, modify columns variable in :code:`mysci.py` to read:

   ```
   # Column names and column indices to read
   columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7}
   ```

   and modify the types variable to be:

   ```
   # Data types for each column (only if non-string)
   types = {'tempout': float, 'windspeed': float}
   ```

2. Now, let's write our first function to compute the wind chill factor. We'll add this function to the bottom of the file.

   ```
   # Compute the wind chill temperature
   def compute_windchill(t, v):
      a = 35.74
      b = 0.6215
      c = 35.75
      d = 0.4275

      v2 = v ** 2
      wci = a + (b * t) - (c * v2) + (d * t * v2)
      return wci
   ```

   To indicate a function in python you type `def` for define, the name of your function, and then in parenthesis the input arguments of that function, followed by a colon. The preceding lines,the code of your function, are all tab-indented. If necessary specify your return value.

   Here is your first introduction to math operators in Python. Addition, subtraction, and multiplication look much like you'd expect. A double astericks, `**`, indicates an exponential. A backslash, `/`, is for division, and a double backslash, `//`, is for integer division.

   And then let's compute a new list with windchill data at the bottom of `mysci.ipynb`\:

   ```
   # Compute the wind chill factor
   windchill = []
   for temp, windspeed in zip(data['tempout'], data['windspeed']):
      windchill.append(compute_windchill(temp, windspeed))
   ```

   Now we'll call our function. Initialize a `list` for wind chill with empty square brackets, `[]`. And in a `for` loop, loop through our temperature and wind speed data, applying the function to each `tuple` data pair. `tuple`\s are ordered like `list`\s, but they are indicated by parenthesis, `()`, instead of square brackets and cannot be changed or appended. `tuple`\s are generally faster than `list`\s.

   We use the `zip` function in Python to automatically unravel the `tuple`\s. Take a look at `zip([1,2], [3,4,5])`. What is the result?

   And finally, add a DEBUG section to see the results:

   ```
   # DEBUG
   print(windchill)
   ```

3. Now, the wind chill factor is actually in the datafile, so we can read it from the file and compare that value to our computed values. To do this, we need to read the windchill from column 12 as a `float`:

   Edit the columns and types `dict`:

   ```
   # Column names and column indices to read
   columns = {'date': 0, 'time': 1, 'tempout': 2, 'windspeed': 7, 'windchill': 12}
   ```

   and

   ```
   # Data types for each column (only if non-string)
   types = {'tempout': float, 'windspeed': float, 'windchill': float}
   ```

   Then, in a DEBUG section at the end of your script, compare the twomdifferent values (one from data and one computed by our function):

   ```
   # DEBUG
   for wc_data, wc_comp in zip(data['windchill'], windchill):
      print(f'{wc_data:.5f}   {wc_comp:.5f}   {wc_data - wc_comp:.5f}')
   ```

   Using an `f-string` with float formatting you can determine the precision to which to print the values. The `.5f` means you want 5 places after the decimal point.

   Test the results. What do you see?

4. Now, format the output so that it's easy to understand and rename this script to something indicative of what it actually does.

   In a new cell, add:

   ```
   # Output comparison of data
   print('                ORIGINAL  COMPUTED')
   print(' DATE    TIME  WINDCHILL WINDCHILL DIFFERENCE')
   print('------- ------ --------- --------- ----------')
   zip_data = zip(data['date'], data['time'], data['windchill'], windchill)
   for date, time, wc_orig, wc_comp in zip_data:
      wc_diff = wc_orig - wc_comp
      print(f'{date} {time:>6} {wc_orig:9.6f} {wc_comp:9.6f} {wc_diff:10.6f}')
   ```

   Here you used f-string formatting with more f-string formatting options. The `>6` indicates that you'd like the characters of the string to be right-justified and to take up 6 spaces.

   The `9f` specifies that you want the value to fill 9 spaces, so `9.6f` indicates you'd like the value to fill 9 spaces with 6 of them being after the decimal point. Same concept for `10.6f`.

   You now have your first complete Python script!

---

That concludes the "First Python Script" virtual tutorial where you learned to write your first Python script.

In this section you calculated wind chill index by writing and calling your first function. You also learned about Python math operators, the `zip()` command, `tuple` datastructure, f-string formatting, and how to push your repository to GitHub.
