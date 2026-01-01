import numpy as np

rng = np.random.default_rng(42)
dataset = rng.normal(5,1.5,(500,3))

print(dataset)

w_true = rng.normal(loc=0,scale=1.0,size=3) # (True weights represent the actual underlying relationship used to generate the target values)weights tells us how much a feature(column) contributes in the sample, its updated after calculating the gradient decent.
bias = rng.normal(loc=0,scale=1.0) # bias is a set value such that even if the feature is 0 its still going to have an output
noise = rng.normal(loc=0,scale=0.01,size=dataset.shape[0]) # noise is random offset added to the true dataset to check models robustness,error etc.

print(w_true,bias,noise)

y = dataset @ w_true + bias + noise # y is the ground-truth target (labels)

print(dataset.shape,y.shape,dataset[:][:6],y[:][:6])