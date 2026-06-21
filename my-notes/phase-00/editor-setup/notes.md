# Editor Setup Notes

## Main idea

VS Code is my control room for AI engineering.

It helps me:

- write Python code
- run Jupyter notebooks
- use the integrated terminal
- manage Git changes
- debug Python files
- connect to remote machines through SSH

## Important extensions

- Python: Python language support
- Pylance: autocomplete, type hints, diagnostics
- Jupyter: run notebooks inside VS Code
- GitLens: better Git history
- Remote SSH: work on remote GPU/cloud machines
- Debugpy: Python debugging
- Black Formatter: auto-format Python code
- Ruff: fast linting

## Important settings

- Use `.venv/bin/python` as the interpreter
- Enable format on save
- Enable basic type checking
- Enable notebook output scrolling
- Use integrated terminal with zsh

## Mental model

VS Code is the workspace.
`.venv` is the Python environment.
Pylance is the autocomplete brain.
Black is the code cleaner.
Ruff is the mistake detector.
Jupyter is the experiment lab.
GitLens is the history tracker.
Remote SSH is the cloud/GPU bridge.

## Main rule

Configure the editor once so every AI project is easier to build and debug.