class Lagrange_Polynomial:
    def __init__(self, data_x, data_y):
        assert len(data_x) == len(data_y)
        self.data_x = data_x
        self.data_y = data_y
        self.degree = len(data_x) - 1


    def __repr__(self):

        strRep = f"Lagrange Poly of order {self.degree}\n"
        strRep += "p(x) = "
        for i in range(len(self.data_y)):
            if self.data_y[i] == 0:
                continue
            elif self.data_y[i] >= 0:
                strRep += f"+ {self.data_y[i]}*l_{i}(x) "
            else:
                strRep += f"- {-self.data_y[i]}*l_{i}(x) "
        return strRep

    def lagBasis(self, k, x):
        l_k = 1
        for j in range(len(self.data_x)):
            if j != k:
                l_k *= (x - self.data_x[j]) / (self.data_x[k] - self.data_x[j])

        return l_k

    def __call__(self, x):
        p_x = 0
        for k in range(len(self.data_x)):
            p_x += self.data_y[k] * self.lagBasis(k, x)
        return p_x