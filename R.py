import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial

def dh(f, h, x1):
    return (f(x1 + h) - f(x1 - h)) / (2 * h)

def dh1(f, h, x1):
    return (4 * dh(f, h / 2, x1) - dh(f, h, x1)) / 3

def error_2(f, h, x):
    f_prime = f.deriv(1)
    Y_actual = f_prime(x)
    dh_error, dh1_error = 0, 0
    dh_error = dh(f, h, x) - Y_actual
    dh1_error = dh1(f, h, x) - Y_actual

    return dh_error, dh1_error