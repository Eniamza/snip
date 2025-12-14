def forward_diff(f, h, x):
    return (f(x + h) - f(x)) / h

def backward_diff(f, h, x):
    return (f(x) - f(x - h)) / h

def central_diff(f, h, x):
    return (f(x + h) - f(x - h)) / (2 * h)

def error_1(f, f_prime, h, x):
    Y_correct = f_prime(x)
    f_error, b_error, c_error = 0, 0, 0

    f_error = forward_diff(f, h, x) - Y_correct
    b_error = backward_diff(f, h, x) - Y_correct
    c_error = central_diff(f, h, x) - Y_correct
    return f_error, b_error, c_error