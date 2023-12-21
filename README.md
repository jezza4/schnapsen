# Schnapsen platform - Project Intelligent Systems 2022-2023

[![PyPI version](https://badge.fury.io/py/schnapsen.svg)](https://badge.fury.io/py/schnapsen)

## Getting started

This is the improved platform for the schnapsen card game. To get to know the concept of the game, please visit
[this web page](https://www.pagat.com/marriage/schnaps.html).

To use the platform, your python version must be at least 3.10, we suggest installing conda to create a python environment.

### Installing from the PyPI server

[The schnapsen package is on the PyPI server](https://pypi.org/project/schnapsen/), which is accessible from anywhere in the world. This installation should be enough for you. You can simply run below to install the latest version:

```sh
pip install schnapsen
```

If you want to install a specific version, you can run something like `pip install schnapsen==0.0.3`.

### Installing from the source code

If you want to modify the source code, this might be the option for you.
First clone this repo by running:

```sh
git clone https://github.com/intelligent-systems-course/schnapsen.git
```

Go to the repo directory and install the schnapsen package and its dependencies in editable mode by running:

```sh
pip install -e .
```

To run the tests, run:

```sh
pip install -e '.[test]'  # on Linux / MacOS
pip install -e ".[test]"  # on Windows
pytest ./tests
```

If the above fails, try deactivating your environment and activating it again.
Then retry installing the dependencies.

## Running the CLI

After intalling, you can try the provided command line interface examples.
Most examples are bots playing against each other; read the code for details.

To run the CLI, run:

```sh
python executables/cli.py
```

This will list the available commands.

For example, if you want try a RandBot play against another RandBot, type
`python executables/cli.py random-game`.

## Running the GUI

The graphical user interface (GUI) lets you play visually against a bot (e.g., You vs. RandBot).

To start the GUI, run:

```sh
python executables/server.py
```

Now, open your webbrowser and type in the server address (i.e., http://127.0.0.1:8080).
By default, you are playing against RandBot. You can also play against other bots. Run

```sh
python executables/server.py --help
```

for more details.

## Implementing more bots

You will find bot examples in the [`src/schnapsen/bots`](./src/schnapsen/bots) folder.
You can look at the example_bot.py file for various methods provided to your bot.

## Troubleshooting

### Getting the right python

The first hurdle in getting the platform to run is getting the right python version on your system.
An easy way to get that is using virtual environments. We suggest you install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html) to manage them.
Then, you can use conda to create a new environment by running

```sh
conda create --name project_is python=3.10
```

With this environment created, you can start it

```
conda activate project_is
```

Inside this environment you can install the dependencies as instructed above.

### Run the right python

If you install conda and create an environment, you can run python by just running the `python` command.
However, often your system also provides a python version.
To know which python is running, use

```sh
which python    # on linux
where python    # on windows (untested)
```

Now, you want to look at the output and make sure that this executable is inside the anaconda folder and not where your system stores its executables.

<!--

Most of the time, when you read Github python repo READMEs, they won't tell you how to do things in detail, but simply tell you things like run `python bar`, run `pip install foo`, etc. All of these imply that you are running things in an isolated python environment. Often times this is easily done by creating virtual environments (e.g., venv, conda, etc.), where you know exactly what `python`, `pip`, and other modules you are running. If you are not familiar with it and still want to proceed on your current machine, especially on Windows, below are some tips.

1. **Be super specific with your python binary.**

   Don't just run `python bar` but do more like `python3.10 bar`. If you just run `python bar`, it's hard to know which python binary file your system is running.

2. **Be super specific with the modules (e.g., pip, pytest).**

   Don't just run `pip install foo` but do more like `python3.10 -m pip install foo`. Again, if you just run `pip install foo`, we don't know exactly which `pip` your system will run. `python3.10 -m pip install foo` specifies that you want your `python3.10` to run the module (i.e., `-m`) `pip` to do something. The same goes for `python3.10 -m pytest ./tests`, instead of `pytest ./tests`.

Things can be messy if you have multiple python3.10 versions (e.g., `python3.10.1`, `python3.10.10`, etc.). Things can get even more messy when your python binary can't be run as `python3.10` but more like `py3.10` or something. Good luck!
-->

## Documentation

The code is documented using reStructuredText. You can either read the documentation along the code, or generate a more suer friendly version.
A pregenerated version of the documentation can be found int he doc folder. It can be regenerated by runnign the following in the root of the repository.

```bash
pip install pdoc
pdoc --html src/schnapsen executables/ -o doc/
```

if above doesn't work, try pdoc3, instead of pdoc
