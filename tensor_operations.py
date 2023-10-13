# -*- coding: utf-8 -*-
"""Tensor_Operations.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fvYOXvRtHg0FIpq8RuYqH4L5yqobD-tV
"""

import torch

my_torch = torch.arange(10)
my_torch

"""## Reshape and View"""

# Reshape and View
my_torch = my_torch.reshape(2, 5)
my_torch

"""### **Reshape if the number of items is not known using -1\**"""

# Reshape if the number of items is not known using -1
my_torch2 = torch.arange(10)
my_torch2

my_torch2 = my_torch2.reshape(2, -1)
my_torch2

my_torch2 = torch.arange(15)
my_torch2

my_torch2 = my_torch2.reshape(3, -1)
my_torch2

"""### opposite direction"""

# opposite direction
my_torch2 = torch.arange(15)
my_torch2

my_torch2 = my_torch2.reshape(-1, 5)
my_torch2

my_torch2 = torch.arange(15)
print(my_torch2)
my_torch2 = my_torch2.reshape(-1, 5)
my_torch2

"""### **View**"""

# View
my_torch3 = torch.arange(10)
my_torch3

my_torch4 = my_torch3.view(2, 5)
my_torch4

"""#### Differences bewwen Shape and View:
[SO discussion](https://stackoverflow.com/questions/49643225/whats-the-difference-between-reshape-and-view-in-pytorch)

### With reshape and view, they will update
"""

# With reshape and view, they will update
my_torch5 = torch.arange(10)
my_torch5

my_torch6 = my_torch5.reshape(2, 5)
my_torch6

my_torch5[1] = 4141
my_torch5

my_torch6

"""## Slices"""

# Slices
my_torch7 = torch.arange(10)
my_torch7

"""#### Grab a specific item"""

# Grab a specific item
my_torch7[7]

"""Grab a slice"""

# Grab a slice
my_torch8 = my_torch7.reshape(5, 2)
my_torch8

# Get the second column
my_torch8[:, 1]

# Return a column
my_torch8[:, 1:]