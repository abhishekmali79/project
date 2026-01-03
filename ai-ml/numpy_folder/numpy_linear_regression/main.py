import numpy as np
from data_generation import *
from model import *
from preprocessing import *
from train import *
from evaluation import *

rng = np.random.default_rng(42)
# dataset = generate_data(rng,3,4,500,4)

dataset = np.array([
    [3.5, 72, 6.5, 4],
    [5.0, 85, 7.0, 6],
    [2.0, 60, 6.0, 2],
    [6.5, 90, 7.5, 8],
    [4.0, 78, 6.8, 5],
    [7.0, 95, 8.0, 9],
    [1.5, 55, 5.5, 1],
    [5.5, 88, 7.2, 7],
    [3.0, 70, 6.0, 3],
    [6.0, 92, 7.8, 8],
    [4.5, 80, 7.0, 5],
    [2.5, 65, 6.2, 2]
], dtype=float)

y = np.array([
    63.5,
    78.2,
    51.0,
    89.4,
    71.8,
    94.1,
    46.2,
    84.6,
    58.9,
    91.3,
    74.0,
    54.7
], dtype=float)


# w_true,bias = generate_true_parameters(rng,dataset.shape[1])
# noise = generate_noise(rng,dataset.shape[0])
# y = generate_labels(dataset,w_true,bias,noise)

stdr_dataset = standardization(dataset)
dataset_bias = add_bias(stdr_dataset)
dataset_bias,y = shuffle_data(rng,dataset_bias,y)
train_dataset,test_dataset,train_y,test_y = train_test_split(rng,dataset_bias,y)

w = initial_weights(rng,train_dataset.shape[1])

w = training(train_dataset,w,train_y)

testing(test_dataset,w,test_y)


