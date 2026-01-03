import numpy as np

def generate_data(rng,mean,std,n_samples,n_features):
    dataset = rng.normal(mean,std,size=(n_samples,n_features))

    return dataset

def generate_true_parameters(rng,n_features):
    w_true = rng.normal(loc=0,scale=1.0,size=n_features) # (True weights represent the actual underlying relationship used to generate the target values)weights tells us how much a feature(column) contributes in the sample, its updated after calculating the gradient decent.
    bias = rng.normal(loc=0,scale=1.0) # bias is a set value such that even if the feature is 0 its still going to have an output

    return w_true,bias

def generate_noise(rng,n_samples):
    noise = rng.normal(loc=0,scale=0.01,size=n_samples) # noise is random offset added to the true dataset to check models robustness,error etc.

    return noise

def generate_labels(dataset,w_true,bias,noise):
    y = dataset @ w_true + bias + noise # y is the ground-truth target (labels)

    return y