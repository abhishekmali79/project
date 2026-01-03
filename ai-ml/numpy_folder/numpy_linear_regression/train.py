import numpy as np
from model import *

def training(train_dataset,w,train_y):
    for epoch in range(1001):
        y_pred = pred(train_dataset,w)
        MSE = calc_loss(train_y,y_pred)
        gradient = calc_gredient(train_dataset,train_y,y_pred)
        w = update_weights(w,0.01,gradient)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss {MSE}")

    return w

