import numpy as np

from math import cos, e,pi,sqrt,exp

def f(x):
    return (e**(-x**2))*cos(x)


def rectangle(a, b, n):
    h = (b - a) / n
    args = np.linspace(a, b - h, n) + h/2
    res = 2 * sum(map(lambda x: f(x)*h,args))
    ans = [res,abs(real_ans - res)]
    return ans

def trapeze(a, b, n):
    h = (b - a) / n
    args = np.linspace(a, b, n+1)
    res =2* sum((h/2)*(f(args[i]) + f(args[i - 1])) for i in range(1,n+1))
    return [res,abs(real_ans-res)]

def simpson(a, b, n):
    if n % 2 != 0:
        n += 1 #aby suma ponizej sie zgadzala
    h = (b - a) / n
    args = np.linspace(a, b, n+1)
    res = ((2 * h) / 3) * sum(f(args[2 * i - 2]) + 4 * f(args[2 * i - 1]) + f(args[2 * i]) for i in range(1, (n // 2) + 1))
    return [res,abs(real_ans-res)]


if __name__ == "__main__":
    a = 0
    b = 10000
    N = [10**6,5*10**6,int(7.5*10**6),10**7]
    for n in N:
        print("n=",n)
        real_ans = sqrt(pi) / exp(1/4)
        print("Metoda prostokatow ")
        ans = rectangle(a, b,n)
        print("wynik ",ans[0])
        print("blad bezwzgledny ",ans[1])
        print("Metoda trapezow ")
        ans = trapeze(a, b,n)
        print("wynik ",ans[0])
        print("blad bezwzgledny ",ans[1])
        print("Metoda Simpsona ")
        ans = simpson(a, b,n)
        print("wynik ",ans[0])
        print("blad bezwzgledny ",ans[1])
    