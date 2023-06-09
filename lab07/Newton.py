import numpy as np

def f1(x):
    return x * np.cos(x) - 1

def df1(x):
    return np.cos(x) - x * np.sin(x)

def f2(x):
    return x**3 - 5*x - 6

def df2(x):
    return 3*x**2 - 5

def f3(x):
    return np.exp(-x) - x**2 + 1

def df3(x):
    return -np.exp(-x) - 2*x

def newton_raphson(func, dfunc, x0, max_iter=12):
    xn = x0
    solutions = []
    for n in range(max_iter):
        fxn = func(xn)
        dfxn = dfunc(xn)
        if dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/dfxn
        solutions.append(xn)
    return solutions

# Przykładowe użycie metody Newtona-Raphsona dla trzech równań:
x0_11 = 2  # Początkowe przybliżenie dla równania 1
x0_12 = 5  # Początkowe przybliżenie dla równania 1
x0_2 = 4  # Początkowe przybliżenie dla równania 2
x0_3 = 2  # Początkowe przybliżenie dla równania 3

solutions1 = newton_raphson(f1, df1, x0_11)
print("Solutions for equation 1 (x = 2):")
for n, sol in enumerate(solutions1, start=1):
    print(f'n = {n}: {sol}')
print()
solutions1 = newton_raphson(f1, df1, x0_12)
print("Solutions for equation 1 (x = 5):")
for n, sol in enumerate(solutions1, start=1):
    print(f'n = {n}: {sol}')
print()
solutions2 = newton_raphson(f2, df2, x0_2)
print("\nSolutions for equation 2 (x = 4):")
for n, sol in enumerate(solutions2, start=1):
    print(f'n = {n}: {sol}')
print()
solutions3 = newton_raphson(f3, df3, x0_3)
print("\nSolutions for equation 3 (x = 2):")
for n, sol in enumerate(solutions3, start=1):
    print(f'n = {n}: {sol}')
print()