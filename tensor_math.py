# -*- coding: utf-8 -*-
"""Tensor_Math.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14TxFJFeDM9Da1NGlI3zdEDUsfP5I9qZo

# TENSOR MATH OPERATIONS

- Add, Substract, Multiply, Divide, Remainders, Exponents
- Shorthand and Longhand expressions
- Reassingnment
"""

import torch
import numpy as np

tensor_a = torch.tensor([1,2,3,4])
tensor_b = torch.tensor([5,6,7,8])

# Addition
tensor_a + tensor_b

# Addition Longhand
torch.add(tensor_a, tensor_b)

# Another way to add Longhand
tensor_a.add(tensor_b)

# Substraction
tensor_b - tensor_a

# Substraction Longhand
torch.sub(tensor_b, tensor_a)

# Alias to sub
torch.subtract(tensor_b, tensor_a)

# Multplication
tensor_a * tensor_b

# Multplication Longhand
torch.mul(tensor_a, tensor_b)

# Multiplication Longhand
torch.multiply(tensor_a, tensor_b)

# Division
tensor_a / tensor_b

# Division Longhand
torch.divide(tensor_a, tensor_b)

torch.div(tensor_a, tensor_b)

# Remainder (Modulus)
tensor_b % tensor_a

# Remainder (Modulus) Longhand
torch.remainder(tensor_b, tensor_a)

# Exponent / power
tensor_a ** tensor_b

# Exponent / power Longhand
torch.pow(tensor_a, tensor_b)

# Reassignment
tensor_a = torch.tensor([1,2,3,4])
tensor_b = torch.tensor([5,6,7,8])
tensor_a = tensor_a +  tensor_b
tensor_a

# Reassignment with method add_
tensor_a = torch.tensor([1,2,3,4])
tensor_b = torch.tensor([5,6,7,8])
tensor_a.add_(tensor_b)
tensor_a