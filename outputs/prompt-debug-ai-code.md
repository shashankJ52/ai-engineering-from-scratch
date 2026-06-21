# Prompt Debug AI Code

## Purpose

Use this checklist to diagnose AI and ML bugs that may not crash but silently produce bad results.

## 1. Tensor shape bugs

Check:

* What is the input shape?
* What shape does each model layer expect?
* What shape does each layer output?
* Is the batch dimension correct?

Useful command:

```python
print(tensor.shape)
```

## 2. NaN or Inf values

Check:

* Does the loss become NaN?
* Do model outputs contain NaN?
* Do gradients contain NaN or Inf?
* Is the learning rate too high?
* Is there division by zero?
* Is there log of zero?

Useful command:

```python
torch.isnan(tensor).any()
torch.isinf(tensor).any()
```

## 3. Device mismatch

Check:

* Is the model on CPU or GPU?
* Are all tensors on the same device as the model?
* Is training slow because tensors stayed on CPU?

Useful command:

```python
next(model.parameters()).device
tensor.device
```

## 4. Data leakage

Check:

* Are train and test samples overlapping?
* Is future information used to predict the past?
* Did the target label accidentally get included as a feature?
* Is the test accuracy suspiciously high?

## 5. Loss curve problems

If loss is not decreasing:

* learning rate may be too low
* model may be too small
* labels may be wrong
* preprocessing may be broken

If loss oscillates:

* learning rate may be too high
* batch size may be too small

If train loss decreases but validation loss increases:

* model is overfitting

## 6. Performance problems

Check:

* Is data loading slower than training?
* Is preprocessing repeated unnecessarily?
* Is batch size too large or too small?
* Is memory usage growing every step?

Useful tools:

* time.perf_counter
* cProfile
* tracemalloc
* TensorBoard

## 7. Debugging workflow

Before training:

* check data shapes
* check one sample manually
* check train/test split
* run one forward pass

First few steps:

* print loss
* check outputs
* check gradients
* check NaNs

During training:

* log loss and metrics
* track learning rate
* watch gradient norms
* use TensorBoard for curves

When something breaks:

* use breakpoint()
* inspect tensor shapes
* inspect tensor values
* inspect devices
* inspect gradients

## Main rule

AI bugs often do not crash. They silently train on bad data or bad tensors.

Always check:

* shape
* dtype
* device
* min/max/mean
* NaN/Inf
* loss trend
