import numpy as np

# Standardization/normalization is a data preprocessing technique where each feature is transformed so that it has:

# Mean = 0

# Standard deviation = 1

# Standardization puts all features on the same scale.

# After standardization:

# Values tell how many standard deviations away they are from the mean

# Large-scale features stop dominating small-scale ones

def standardization(dataset):
    mean = dataset.mean(axis=0)
    std = dataset.std(axis=0)
    std[std == 0] = 1
    
    stdr_dataset = (dataset - mean)/std

    return stdr_dataset

# Short answer (intuition)

# We add a bias so the model can shift the prediction up or down, instead of being forced to pass through the origin (0).
def add_bias(stdr_dataset):
    dataset_bias = np.c_[np.ones(stdr_dataset.shape[0]),stdr_dataset]

    return dataset_bias

def shuffle_data(rng,dataset_bias,y):
    perm = rng.permutation(dataset_bias.shape[0]) # rng.permutation(dataset.shape[0]) generates a random shuffle of row indices, used to reorder (shuffle) the dataset and labels together without breaking their correspondence.

    dataset_bias = dataset_bias[perm]
    y = y[perm]

    return dataset_bias,y

def train_test_split(rng,dataset_bias,y):
    random_vals = rng.random(dataset_bias.shape[0])
    mask = random_vals > 0.20

    training = dataset_bias[mask]
    testing = dataset_bias[~mask]
    y_training = y[mask]
    y_testing = y[~mask]

    return training,testing,y_training,y_testing

