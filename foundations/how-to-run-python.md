# Installing and Running Python

This section provides an overview of different ways to run Python code, and quickstart guides for

- Choosing a Python platform
- Installing and running Python on various local platforms
- Installing and managing Python with Conda

## Choosing a Python Platform

There is no single official platform for the Python language. Here we provide a brief rundown of 3 popular platforms:

1. The terminal,
2. Jupyter notebooks, and
3. IDEs (integrated development environment).

Here we hope to provide you with enough information to understand the differences and similarities between each platform so that you can make the best chose for your work environment and learn along effectively, regardless of your Python platform preference.

In general, it is always best to test your programs in the same environment in which they will be run. The biggest factors to consider when choosing your platform are:

- What are you already comfortable with?
- What are the people around you using (peers, coworkers, instructors, etc)?

### Terminal

For learners who are familiar with basic [Linux commands](https://cheatography.com/davechild/cheat-sheets/linux-command-line/) and text editors, running Python in the terminal is the quickest route straight to learning Python syntax without the covering the bells and whistles of a new platform. If you are running Python on a super computer, through an HTTP request, or ssh tunneling you might want to consider learning in the terminal.

[How to Run Python in the Terminal](terminal.md)

### Jupyter Notebooks

We highly encourage the use of Jupyter notebooks; a free, open-source, interactive tool running inside a web browser that allows you to run Python code in "cells." This means that your workflow can alternate between code, output, and even Markdown-formatted explanatory sections that create an easy to follow analysis or "computational narrative" from start to finish. Jupyter notebooks are a great option for presentations or learning tools. For these reasons Jupyter is very popular among scientists. Most lessons in this book will be taught via Jupyter notebooks.

[How to Run Python in a Jupyter Session](jupyter.md)

### Other IDEs

If you code in other languages you might already have a favorite IDE that will work just as well in Python. [Spyder](https://www.spyder-ide.org) is a Python specific IDE that comes with the [Anaconda download](https://www.anaconda.com/products/individual). It is perhaps the most familiar IDE if you are coming from languages such as [Matlab](https://www.mathworks.com/products/matlab.html) that have a language specific platform and display a list of variables. [PyCharm](https://www.jetbrains.com/pycharm/) and [Visual Studio Code](https://code.visualstudio.com) are also popular IDEs. Many IDEs offer support for terminal execution, scripts, and Jupyter display. To learn about your specific IDE visit its official documentation.

_We recommend eventually learning how to develop and run Python code in each of these platforms._

## Installing and managing Python with Conda

Conda is an open-source, cross-platform, language-agnostic package manager and environment management system that allows you to quickly install, run, and update packages within your work environment(s). Conda is a vital component of the Python ecosystem, and understanding it is important regardless of the platform you chose to run your Python code.

[Learn more about Conda here](conda.md)
