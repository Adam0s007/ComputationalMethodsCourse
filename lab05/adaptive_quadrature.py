import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2) * np.cos(x)

def simpson(f, a, b):
    h = b - a
    middle = (a + b) / 2
    return h * (f(a) + 4 * f(middle) + f(b)) / 6


def adaptive_quadrature(f, a, b, epsilon):
    mid = (a + b) / 2
    diff = abs(simpson(f, a, b) - simpson(f, a, mid) - simpson(f, mid, b))
    if diff < 15 * epsilon:
        return simpson(f, a, mid) + simpson(f, mid, b)
    return adaptive_quadrature(f, a, mid, epsilon / 2) + adaptive_quadrature(f, mid, b, epsilon / 2)


def adaptive_quadrature_points(f, a, b, epsilon, points):
    s_q = simpson
    mid = (a + b) / 2
    diff = abs(s_q(f, a, b) - s_q(f, a, mid) - s_q(f, mid, b))
    if diff < 15 * epsilon:
        points.update([a, mid, b])
        return s_q(f, a, mid) + s_q(f, mid, b)
    return adaptive_quadrature_points(f, a, mid, epsilon / 2, points) + adaptive_quadrature_points(f, mid, b, epsilon / 2, points)

def plot_adaptive_points(f, a, b, epsilon, ax):
    points = set()
    adaptive_quadrature_points(f, a, b, epsilon, points)

    x_axis = np.linspace(a, b, 500)
    ax.plot(x_axis, f(x_axis), color='maroon', linewidth=3)
    points = np.array(list(points))
    ax.scatter(points, f(points), zorder=5, color="darkblue")
    ax.set_title(f'epsilon: {epsilon}')

if __name__ == "__main__":
    a = -5
    b = 5
    _, ax = plt.subplots(1, 3, figsize=(18, 5))
    plot_adaptive_points(f, a, b, 1e-5, ax[0])
    plot_adaptive_points(f, a, b, 1e-8, ax[1])
    plot_adaptive_points(f, a, b, 1e-16, ax[2])
    plt.show()
