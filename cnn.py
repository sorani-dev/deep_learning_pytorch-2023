# -*- coding: utf-8 -*-
"""CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1u8h9214AE_8aRYitmYStkAe0YHSjjFAL
"""

# Commented out IPython magic to ensure Python compatibility.
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
from torchvision.utils import make_grid

import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

# %matplotlib inline

# Convert MNIST Image Files into a Tensor of 4-Dimensions (# of images, Height, Width, Color Channel)
transform = transforms.ToTensor()

# Train Data
train_data = datasets.MNIST(root='/cnn_data', train=True, download=True, transform=transform)

# test Data
test_data = datasets.MNIST(root='/cnn_data', train=False, download=True, transform=transform)

train_data

test_data

pwd

ls

cd ../

ls

cd cnn_data

ls

cd /

ls

cd content/

ls -al