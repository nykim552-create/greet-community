# Contributing to greet-community

## Set up for development

Activate a Python 3.11+ virtual environment, then run:

    python -m pip install -e .

## Run the tests

    python -c "from greet_community import greet; print(greet('Hee'))"

Expected output: `Hello, Hee!`

## Send a change

1. Create a branch from main: `git switch -c <branch> main`
2. Commit your change: `git commit -am "<message>"`
3. Push the branch: `git push -u origin <branch>`
4. Open a pull request from your branch into main.
