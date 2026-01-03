import numpy as np

def initial_weights(rng,n_features):
    w = rng.normal(0,0.01,size=(n_features,1))

    return w

def pred(dataset_bias,w):
    y_pred = dataset_bias @ w

    return y_pred

def calc_loss(y,y_pred):
    y = y.reshape(-1,1)
    MSE = np.mean((y - y_pred)**2)

    return MSE

def calc_gredient(dataset_bias,y,y_pred):
    n = dataset_bias.shape[0]
    y = y.reshape(-1,1)
    gradient = (2/n) * dataset_bias.T @ (y_pred - y)

    return gradient

def update_weights(w,learning_rate,gradient):
    w = w - learning_rate * gradient

    return w
    