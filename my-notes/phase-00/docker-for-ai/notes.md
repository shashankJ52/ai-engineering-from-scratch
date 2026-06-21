# Docker for AI Notes

## Main idea

Docker packages code, Python, dependencies, system libraries, and runtime settings into a reproducible container.

It solves the "works on my machine" problem.

## Mental model

- Dockerfile = recipe
- Image = built template
- Container = running instance of the image
- Volume = shared persistent folder
- Docker Compose = starts multiple services together

## Why Docker matters in AI

AI projects often depend on specific versions of:

- Python
- PyTorch
- CUDA
- transformers
- system libraries
- vector databases
- model-serving tools

Without Docker, the same project can work on one machine and fail on another.

## What I should use Docker for

Use Docker for:

- FastAPI AI backend
- RAG app deployment
- vector database setup
- production demos
- reproducible project environments
- sharing projects with recruiters or teammates

## What I can skip for now

Since I am on a Mac, I can skip:

- NVIDIA Container Toolkit
- CUDA Docker setup
- --gpus all
- large GPU image builds

I can learn GPU Docker later when using a Linux cloud GPU machine.

## Main rule

Use Docker when a project needs to run reliably across different machines.
Use volumes for models, datasets, and generated files so they do not disappear when containers stop.