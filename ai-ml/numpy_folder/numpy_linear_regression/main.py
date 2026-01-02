import numpy as np
from data_generation import *
from model import *
from preprocessing import *

rng = np.random.default_rng(42)
dataset = generate_data(rng,3,4,500,4)
w_true,bias = generate_true_parameters(rng,dataset.shape[1])
noise = generate_noise(rng,dataset.shape[0])
y = generate_labels(dataset,w_true,bias,noise)

stdr_dataset = standardization(dataset)
dataset_bias = add_bias(stdr_dataset)
dataset_bias,y = shuffle_data(rng,dataset_bias,y)

w = initial_weights(rng,dataset_bias.shape[1])
y_pred = pred(dataset_bias,w)
MSE = calc_loss(y,y_pred)
gradient = calc_gredient(dataset_bias,y,y_pred)
w = update_weights(w,0.01,gradient)

print(w.shape)