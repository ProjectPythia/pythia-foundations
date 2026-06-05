# Jupyter Components

---

## Overview

This short chapter introduces the four main components of the Jupyter ecosystem: {term}`Jupyter Notebook`, {term}`Jupyter Kernels`, {term}`JupyterLab`, and {term}`JupyterHub`. We then give a basic orientation to the two ways we can execture Python code in a Jupyter session: local and remote.

## Prerequisites

| Concepts | Importance | Notes |
| --- | --- | --- |
| [Installing and Running Python: Python in Jupyter](jupyter.md) | Helpful | |

:::{tip} Time to learn
10 minutes
:::
---

## The four key components

### Jupyter notebooks

The {term}`Jupyter Notebook` software [@https://doi.org/10.3233/978-1-61499-649-1-87] is an open-source web application that allows you to create and share notebook files (`*.ipynb` files). Jupyter Notebooks contain executable code, LaTeX equations, visualizations (e.g., plots, pictures), and narrative text. The code does not have to just be Python, other languages such as Julia or R are supported as well.

Jupyter Notebooks are celebrated for their interactive output that allows movement between code, code output, explanations, and more code - similar to how scientists think and solve problems. Jupyter Notebooks can be thought of as a living, runnable publication and make for a great presentation platform.

### Jupyter kernels
Software engines and their environments (e.g., {term}`conda` environments) that execute the code contained in {term}`Jupyter Notebook`s.

The kernel is where your Python code is interpreted and the outputs are generated, which may be either on your local computer or a remote host (see below).

### JupyterLab

A popular web application on which users can create and execute {term}`Jupyter Notebook` files, as well as explore data, install software, etc.
See the [next section](jupyterlab.ipynb) for more guidance on getting started with JupyterLab

### JupyterHub

A web-based platform that authenticates users and launches {term}`JupyterLab` applications for users on remote systems.

## Executing Jupyter

### Local execution model

You can launch {term}`JupyterLab` from a terminal; it will open up in a web browser. The application will then be running in that web browser. When you open a notebook, Jupyter opens a kernel which can be tied to a specific coding language.

To launch the JupyterLab interface in your browser, follow the instructions in [Installing and Running Python: Python in Jupyter](jupyter.md).

![Local Execution Model](../images/local-execution-model.gif)

### Remote execution model

In the remote execution model, you start out in the browser, then navigate to a specific URL that points to a {term}`JupyterHub`. On JupyterHub, you authenticate on the remote system, and then {term}`JupyterLab` is launched and redirected back to your browser. The interface appears the same as if you were running Jupyter locally.

![Remote Execution Model](../images/remote-execution-model.gif)

---

## Summary

Jupyter consists of four main components:
- Jupyter Notebooks (the `*.ipynb` files),
- Jupyter Kernels (the work environment),
- JupyterLab (a popular web application and interface creating and running notebooks),
- JupyterHub (an application and launcher for remote execution).

We interact with JupyterLab through a web browser and the interface is the same whether we are running a local JupyterLab session or logged in to a remote session via JupyterHub.

### What's next?

- [A JupyterLab Tour](jupyterlab.ipynb)

## Additional resources

- [Jupyter Documentation](https://jupyter.org/)
- [Xdev Python Tutorial Seminar Series - Jupyter Notebooks](https://youtu.be/xSzXvwzFsDU)
