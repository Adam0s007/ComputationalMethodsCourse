import numpy as np
import math
from math import cos,e

real_ans = math.sqrt(math.pi) / math.exp(1/4)

def f(x):
    return (e**(-x**2))*cos(x)

def simpson(a, b, n=10000000):
    n1 = n+1
    h = (b - a) / n
    args = np.linspace(a, b, n+2) 
    res = 2 * sum((h/3)*(f(args[2 * i - 2]) + 4 * f(args[2 * i - 1]) + f(args[2 * i])) for i in range(1, (n1 // 2) + 1))
    return [res,math.fabs(real_ans-res)]


def fun1(x): return np.vectorize(lambda x: math.exp(-x**2) * math.cos(x))(x)
def simpson_rule():
    print("simpson rule >>>> ")
    for n in N1:
        m = n + 1
        width = (b1 - a1) / n
        intervals = np.linspace(a1, b1, m+1)
        approx = 0.0
        for i in range(1, m//2+1):
            approx += width * (fun1(intervals[2*i-2]) + 4*fun1(intervals[2*i-1]) + fun1(intervals[2*i])) / 3
        approx *= 2
        print(f"n = {n}, S = {approx}, Err = {abs(real_ans - approx)}")

    print()


a1, b1, N1 = 0, 10**5, [10**6,10**7]
#simpson_rule()
res = simpson(a1,b1)
print(res)