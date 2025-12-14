def getPoly(dataX, data_y):
    n_nodes = len(dataX)
    X = np.zeros((n_nodes, n_nodes))

    for row in range(len(dataX)):
      for col in range(n_nodes):
        X[row,col] = dataX[row] ** col

    print(X)
    X_inv = np.linalg.pinv(X)
    a = np.dot(X_inv, data_y)
    print(a)
    p = Polynomial(a)

    return p