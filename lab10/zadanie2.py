import numpy as np

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

def run_test(prec):
    A = np.array([[10, -1, 2, -3],
                  [1, 10, -1, 2],
                  [2, 3, 20, -4],
                  [3, 2, 1, 20]])
    b = np.array([0, 5, -10, 15]).reshape(-1, 1)
    solves, res = jacobi_iteration(A, b, prec)
    print(len(res))

run_test(10e-4)
run_test(10e-5)
run_test(10e-6)
