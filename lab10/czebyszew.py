from random import randint
import numpy as np

n = 5

def generate_matrices():
    M = [[0.0 for _ in range(n)] for _ in range(n)]
    X = [randint(-1, 0) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                if i == 0 or i == n - 1:
                    M[i][j] = 1
                else:
                    M[i][j] = 2
            elif i == j + 1:
                M[i][j] = 1 / (i + 1)
            elif j == i + 1:
                M[i][j] = 1 / (i + 2)
    return M, X

def Chebyshev_method(A: np.array, b: np.array, precision):
    x_prior = np.zeros(len(A[0])).reshape(-1, 1)
    t = []
    results = []
    eigs = np.linalg.eig(A)[0]
    p, q = np.min(np.abs(eigs)), np.max(np.abs(eigs))
    r = b - A @ x_prior
    x_posterior = x_prior + 2 * r / (p + q)
    r = b - A @ x_posterior
    t.append(1)
    t.append(-(p + q) / (q - p))
    beta = -4 / (q - p)
    i: int = 1
    norm_one = 2
    norm_two = 2
    norm_b = np.linalg.norm(b)

    while norm_one > precision or norm_two > precision:
        norm_one = np.linalg.norm(abs(x_posterior - x_prior))
        norm_two = np.linalg.norm(A @ x_posterior - b) / norm_b
        results.append((i, norm_one, norm_two))
        i += 1
        t.append(2 * t[1] * t[-1] - t[-2])
        alpha = t[-3] / t[-1]
        old_prior, old_posterior = x_prior, x_posterior
        x_prior = old_posterior
        x_posterior = (1 + alpha) * old_posterior - alpha * old_prior + (beta * t[-2] / t[-1]) * r
        r = b - A @ x_posterior
    return x_posterior, results

def run():
    mA, mX = generate_matrices()
    A = np.array(mA)
    x = np.array(mX).reshape(-1, 1)
    b = A @ x
    solves, res = Chebyshev_method(A, b, 1e-8)
    print("Macierz A:")
    print(A)
    print("Wektor b:")
    print(b)
    print("Wektor x będący rozwiązaniem:")
    print(solves)
    for t in res:
        print(t[0], "&", t[1], "&", t[2], "\\\\")

run()
