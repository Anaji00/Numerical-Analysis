import math

def newtons_method(p0, f, f_prime, tol, max_iter):
    i = 1
    while i <= max_iter:
        p = p0 - f(p0) / f_prime(p0)
        print(f"Iteration {i}: p = {p}")  # Display every iteration
        if abs(p - p0) < tol:
            return p
        p0 = p
        i += 1
    return "The method failed after {} iterations.".format(max_iter)

# Example usage:
def f(x):
    return math.cos(x)  - x

def f_prime(x):
    return -math.sin(x) - 1 

p0 = 1.5
tol = 0.000001
max_iter = 50

result = newtons_method(p0, f, f_prime, tol, max_iter)
print(result)