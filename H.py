import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from numpy.polynomial import Polynomial

def l(k, x):
    n = len(x)
    assert (k < len(x))

    x_k = x[k]
    x_copy = np.delete(x, k)

    denominator = np.prod(x_copy - x_k)

    coeff = []

    for i in range(n):
        coeff.append(sum([np.prod(x) for x in combinations(x_copy, i)]) * (-1)**(i) / denominator)

    coeff.reverse()

    return Polynomial(coeff)


def h(k, x):
    l_k = l(k, x)
    l_k_sqr = l_k ** 2
    l_k_prime = l_k.deriv(1)

    l_k_prime_at_xk = l_k_prime(x[k])

    coeff = [1 + 2 * x[k] * l_k_prime_at_xk, -2 * l_k_prime_at_xk]
    p = Polynomial(coeff)


    return p * l_k_sqr

def h_hat(k, x):
    l_k = l(k, x)
    l_k_sqr = l_k ** 2

    
    coeff = [-x[k], 1]
    p = Polynomial(coeff)
    return p * l_k_sqr