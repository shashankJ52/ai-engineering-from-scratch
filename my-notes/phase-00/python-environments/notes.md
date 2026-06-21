# Python Environments Notes

## Main idea

Virtual environments isolate project dependencies so different projects can use different package versions without breaking each other.

## Mental model

Each project gets its own room.

- `.venv` = the room
- `source .venv/bin/activate` = enter the room
- `uv pip install package` = put tools inside the room
- `deactivate` = leave the room

## Why this matters in AI

AI projects often need different versions of packages like:

- torch
- transformers
- numpy
- langchain
- pydantic
- tensorflow

Without virtual environments, one project can break another.
