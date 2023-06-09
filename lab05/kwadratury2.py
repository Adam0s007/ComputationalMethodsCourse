
import numpy as np
from math import pi
def f(x):
    return 1 / ((x**2)+1)


def rectangle(a,b):
    h = 0.1
    arr = np.linspace(0, 0+(b-a), num=10, endpoint=False)
    Integ = sum(map(lambda x: f(x) * h, arr[1::]))
    res = [Integ,Integ - (pi/4)]
    return res

def trapeze(a,b):
    h = 0.1
    arr = np.linspace(0, 0+(b-a), num=11, endpoint=True)
    Integ = sum(map(lambda x: (f(x) + f(x-h)) * h/2, arr[1::]))
    res = [Integ,Integ - (pi/4)]
    return res

def simpson(a,b):
    h = 0.1
    arr = np.linspace(0, 0+(b-a), num=6, endpoint=True)
    Integ = sum(map(lambda x: (f(x) + 4*f(x-h) + f(x-(2*h))) * (h/3), arr[1::]))
    res = [Integ,Integ - (pi/4)]
    return res

def print_res(res):
    print(f"{res[0]:.12f} blad bezwzgledny: {res[1]:.12f}")


if __name__ == "__main__":
    print("Metoda prostokatow")
    res = rectangle(0,1)
    print_res(res)
    print("Metoda trapezow")
    res = trapeze(0,1)
    print_res(res)
    print("Metoda Simpsona")
    res = simpson(0,1)
    print_res(res)


def F(x):
    return 1/(((x+1)/2)+3)

a1 = 0.652145154862546
a2 = 0.652145154862546
a3 =0.3478548451374538
a4 =0.3478548451374538

x1 = -0.3399810435848563
x2 =  0.3399810435848563
x3 = -0.8611363115940526
x4 =  0.8611363115940526

print((a1*F(x1) + a2*F(x2) + a3*F(x3) + a4*F(x4))/2)