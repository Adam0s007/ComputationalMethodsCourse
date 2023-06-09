import numpy as np
from random import uniform
from math import sqrt
from math import pi
EPSILON = 10 ** -6

def f1(x: float) -> float:
    return x ** 2 + x + 1

def f2(x: float) -> float:
    return sqrt(1 - x ** 2)

def f3(x: float) -> float:
    if abs(x) >= EPSILON:
        return 1 / sqrt(x)
    else:
        return 1

def hit_and_miss(fun, a: float, b: float, N: int=1000, M: float=0.001) -> float:
    hits = 0
    h = max(fun(x) for x in np.arange(a, b, M))
    
    for i in range(N):
        x = uniform(a, b)
        y = uniform(0, h)
        
        if y <= fun(x):
            hits += 1
    
    return hits / N * (b - a) * h

if __name__ == "__main__":
    a = 0
    b = 1

    N = 10
    M = 0.001
    real_res_f1:float = 11/6
    real_res_f2:float = pi/4
    real_res_f3:float = 2.0
    while N < 10e6:  
        result_f1 = hit_and_miss(f1, a, b, N, M)
        result_f2 = hit_and_miss(f2, a, b, N, M)
        result_f3 = hit_and_miss(f3, a, b, N, M)
        
        print("N=", N)
        print("f1(x) = x^2 + x + 1:",result_f1,"real_f1:", real_res_f1, " deltaY: ", abs(result_f1 - real_res_f1))
        print("f2(x) = sqrt(1 - x^2):",result_f2,"real_f2:", real_res_f2, " deltaY: ", abs(result_f2 - real_res_f2))
        print("f3(x) = 1 / sqrt(x):",result_f3,"real_f3:", real_res_f3, " deltaY: ", abs(result_f3 - real_res_f3))
        print("====================================")
        N*=10
