import matplotlib.pyplot as plt
import numpy as np

class Polynomial:

  def __init__(self, coeff):

    self.coeff = coeff
    self.degree = len(coeff) - 1

  def __call__(self, xArrData):

    p_xArrData = []
    xNumPy = np.array(xArrData)
    resNum = np.zeros(len(xArrData))

    for i in range(len(self.coeff)):
      resNum += self.coeff[i]*(xNumPy**i)

    return resNum

  def __repr__(self):
    strRep = f'Polynomial of degree {self.degree}\np(x) = '
    for i in range(self.degree + 1):
        a_val = self.coeff[i]
        if i != 0:
            if a_val >= 0:
                strRep += f'+ {a_val}x^{i} '
            else:
                strRep += f'- {-a_val}x^{i} '
        else:
            strRep += f'{a_val}x^{i} '

    return strRep

  def get_degree(self):
    return self.degree


  def get_coeffs(self):
    return self.coeff
