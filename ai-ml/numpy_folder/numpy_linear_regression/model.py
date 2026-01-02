import numpy as np

def initial_weights(rng,n_features):
    w = rng.normal(0,0.01,size=(n_features,1))
    print(w)
    return w

def pred(dataset_bias,w):
    print(dataset_bias.shape,w.shape)
    y_pred = dataset_bias @ w
    print(y_pred.shape,dataset_bias.shape,w.shape)
    print(y_pred[:6,:],dataset_bias[:6,:])
    return y_pred

def calc_loss(y,y_pred):
    y = y.reshape(-1,1)
    print(y.shape,y_pred.shape)
    MSE = np.mean((y - y_pred)**2)

    print(MSE)
    return MSE

def calc_gredient(dataset_bias,y,y_pred):
    n = dataset_bias.shape[0]
    y = y.reshape(-1,1)
    print(y.shape,y_pred.shape)
    gradient = (2/n) * dataset_bias.T @ (y_pred - y)
    
    print(gradient.shape)

    return gradient

def update_weights(w,learning_rate,gradient):
    w = w - learning_rate * gradient
    print(w.shape)  
    return w
    