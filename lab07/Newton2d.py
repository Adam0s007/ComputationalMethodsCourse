import numpy as np

def f(x, y):
    return x**2 + x*y**3 - 9

def g(x, y):
    return 3*x**2*y - y**3 - 4

def jacobian(x, y):
    return np.array([[2*x + y**3, 3*x*y**2],
                     [6*x*y, 3*x**2 - 3*y**2]])

def newton_raphson_system(x0, y0, f, g, jacobian, tol=1e-6, max_iter=100):
    x, y = x0, y0
    for _ in range(max_iter):
        J = jacobian(x, y)
        F = np.array([f(x, y), g(x, y)])
        delta_x, delta_y = -np.linalg.solve(J, F)
        x, y = x + delta_x, y + delta_y
    return x, y

def main():
    x0, y0 = 2, 2  # Początkowe przybliżenie
    for max_iter in range(1, 13):
        x, y = newton_raphson_system(x0, y0, f, g, jacobian, max_iter=max_iter)
        print(f"Rozwiazanie dla max_iter = {max_iter} to: x = {x:.16f}, y = {y:.16f}")

if __name__ == "__main__":
    main()
