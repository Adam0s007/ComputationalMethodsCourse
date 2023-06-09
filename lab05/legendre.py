import numpy as np
from scipy.integrate import quadrature

def generate_legendre_polynomials(n):
    polynomials = [np.poly1d([1]), np.poly1d([1, 0])]
    x_poly = np.poly1d([1, 0])
    
    for idx in range(1, n):
        next_poly = (((2 * idx + 1) / (idx + 1)) * polynomials[idx] * x_poly\
                      - (idx / (idx + 1)) * polynomials[idx - 1])
        polynomials.append(next_poly)
    
    return polynomials


def func(x):
    return 1 / (1 + x ** 2)

def approximate_function(n,a,b):
    legendre_polynomials = generate_legendre_polynomials(n)
    coefficients = []
    approximations = [np.poly1d([0])]
    
    for idx in range(0, n):
        coeff = quadrature((lambda x: func(x) * legendre_polynomials[idx](x)), a, b)[0]  \
        / quadrature((lambda x: legendre_polynomials[idx](x) ** 2), a, b)[0] #tutaj dzieli
        coefficients.append(coeff)
        approximations.append(coeff * legendre_polynomials[idx])
    
    return sum(approximations)

def calculate_integral(n,a,b):
    integral = approximate_function(n,a,b).integ()
    return integral(1) - integral(-1)

result = calculate_integral(8,-1,1)
print(result, result - np.pi / 2)


