import numpy as np
from math import log
from math import pi
def f(x):
    return 1 / (x+1)


def rectangle(a,b):
    res = []
    for n in [1,3, 5]: #kwadratura zwykla n = 1
        h = (b-a)/n
        arr = np.linspace(0, 0+(b-a), num=n+1, endpoint=False)
        Integ = sum(map(lambda x: f(x) * h, arr[1::]))
        res.append([n,Integ,Integ - log(2)])
    return res

def trapeze(a,b):
    res = []
    for n in [2,3, 5]:  #kwadratura zwykla n = 2 
        h = (b-a) / (n - 1)
        arr = np.linspace(0, 0+(b-a), num=n, endpoint=True)
        Integ = sum(map(lambda x: (f(x) + f(x-h)) * h/2, arr[1::]))
        res.append([n,Integ,Integ - log(2)])
    return res

def simpson(a,b):
    res = []
    for n in [3, 5]:  #kwadratura zwykla n = 3 
        h = (b-a) / (n - 1)
        arr = np.linspace(0, 0+(b-a), num=int(n/2+1), endpoint=True)
        Integ = sum(map(lambda x: (f(x) + 4*f(x-h) + f(x-(2*h))) * (h/3), arr[1::]))
        res.append([n,Integ,Integ - log(2)])
    return res

def print_res(res):
    for n,Integ,err in res:
        print("n =", n, ": ", Integ, " blad bezwzgledny: ", err)


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
