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

def jacobi_iteration(A: np.array, b: np.array, precision: float):
    x = np.zeros(len(A[0])).reshape(-1, 1)
    D = np.diag(A).reshape(-1, 1)
    L_U = A - np.diagflat(np.diag(A))
    results = []
    norm_b = np.linalg.norm(b)
    norm_one = 2
    norm_two = 2
    i = 1
    while norm_one > precision or norm_two > precision:
        next_x = (b - L_U @ x) / D
        norm_one = np.linalg.norm(abs(x - next_x))
        norm_two = np.linalg.norm(A @ x - b) / norm_b
        results.append((i, norm_one, norm_two))
        x = next_x
        i += 1
    return x, results

def run():
    mA, mX = generate_matrices()
    A = np.array(mA)
    x = np.array(mX).reshape(-1, 1)
    b = A @ x
    solves, res = jacobi_iteration(A, b, 1e-7)
    print("Macierz A: ")
    print(A)
    print("Wektor b: ")
    print(b)
    print("Wektor x będący rozwiązaniem: ")
    print(solves)
    for t in res:
        print(t[0], "&", t[1], "&", t[2], "\\\\")

run()
