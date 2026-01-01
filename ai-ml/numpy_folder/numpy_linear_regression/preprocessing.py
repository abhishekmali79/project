import numpy as np
from data_generation import dataset,y,rng

mean = dataset.mean(axis=0)
std = dataset.std(axis=0)

# Standardization/normalization is a data preprocessing technique where each feature is transformed so that it has:

# Mean = 0

# Standard deviation = 1

# Standardization puts all features on the same scale.

# After standardization:

# Values tell how many standard deviations away they are from the mean

# Large-scale features stop dominating small-scale ones

stdr_dataset = (dataset - mean)/std

print(stdr_dataset)

# Short answer (intuition)

# We add a bias so the model can shift the prediction up or down, instead of being forced to pass through the origin (0).

print(stdr_dataset.shape)
dataset_bias = np.c_[np.ones(stdr_dataset.shape[0]),stdr_dataset]
print(dataset_bias.shape)


perm = rng.permutation(dataset.shape[0]) # rng.permutation(dataset.shape[0]) generates a random shuffle of row indices, used to reorder (shuffle) the dataset and labels together without breaking their correspondence.

dataset = dataset[perm]
y = y[perm]

print(dataset[:][:6],y[:][:6])

random_vals = rng.random(dataset.shape[0])
mask = random_vals > 0.20

training = dataset[mask]
testing = dataset[~mask]

print(training.shape,testing.shape)

