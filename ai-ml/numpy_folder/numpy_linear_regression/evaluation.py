import numpy as np
from model import *

def testing(test_dataset,w,test_y):
    y_pred = pred(test_dataset,w)
    MSE = calc_loss(test_y,y_pred)

    print(f"Loss {MSE}")