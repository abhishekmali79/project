from data_generation import *
from preprocessing import *

w = rng.normal(0,0.01,size=(4,1))
print(w)

print(dataset_bias.shape,w.shape)

y_pred = dataset_bias @ w
print(y_pred.shape,y.shape,dataset_bias.shape,w.shape)
print(y_pred[:6,:],dataset_bias[:6,:])


y = y.reshape(-1,1)
print(y.shape,y_pred.shape)
MSE = np.mean((y - y_pred)**2)

print(MSE)

n = dataset_bias.shape[0]
print(y.shape,y_pred.shape)
gradient = (2/n) * dataset_bias.T @ (y_pred - y)
print(gradient.shape)

learning_rate = 0.01

w = w - learning_rate * gradient
print(w.shape)
