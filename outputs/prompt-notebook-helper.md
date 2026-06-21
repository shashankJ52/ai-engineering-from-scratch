# Prompt Notebook Helper

## Purpose

This note helps debug common Jupyter notebook issues.

## 1. Notebook works only on my machine

Likely cause:
Cells were executed out of order or the notebook depends on hidden state.

Fix:
Use Kernel > Restart Kernel and Run All Cells before sharing.

## 2. Variable exists even after deleting the cell

Likely cause:
The variable is still stored in the running kernel memory.

Fix:
Restart the kernel.

## 3. Package not found inside notebook

Likely cause:
The notebook is using a different Python environment than the terminal.

Fix:
Check the notebook kernel and compare it with:

```bash
which python
```

The correct Python should point to the project `.venv`.

## 4. Plot does not show

Likely cause:
Matplotlib inline mode may not be enabled.

Fix:
Run:

```python
%matplotlib inline
```

Then use:

```python
plt.show()
```

## 5. Notebook is slow or memory is high

Likely cause:
Large variables, datasets, or models are still in memory.

Fix:
Delete large variables:

```python
del variable_name
```

Then run:

```python
import gc
gc.collect()
```

Or restart the kernel.

## 6. When to use notebooks

Use notebooks for:
- exploring data
- testing ideas
- visualizing results
- learning concepts
- course experiments

## 7. When to use scripts

Use scripts for:
- reusable functions
- production code
- training pipelines
- scheduled jobs
- code that other people need to run reliably

## Main rule

Explore in notebooks. Ship in scripts.