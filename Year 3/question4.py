'''416733'''

import math                            # Importing libraries
import numpy as np
import random

def time(T, n):               # This function works out the time delta
    dt = T/float(n)
    return dt

def ito(S_0, T, n, r, sigma):       # Ito Function

    t = np.zeros(n+1, dtype=float)
    S = np.zeros(n+1, dtype=float)
    assert len(S) == n+1
    dt = time(T,n)                     # Use of time delta

    t[0] = 0.0                         # Start the Time at 0
    S[0] = S_0                         # Start With Initial S value

    for k in range(n):                  # For loop for in the range on n
        z = random.normalvariate(0,1)   # random variable between normal distribution
        dW = sigma*math.sqrt(dt)*z      # Calculate dW_t
        t[k+1] = t[k]+dt
        S[k+1] = S[k]*math.exp((r-float(0.5)*sigma**2)*dt+dW)
    return t, S                        # Returns the values of t & S


def path_payoff(S, E):                  # Path Payoff Function

    return max(E - min(S), 0)


def monte_carlo(payoff_function, S_0, T, r, sigma, n, m):   # Monte Carlo Function
    E = payoff_function
    total = float(0.0)          # Start at 0

    v_0 = math.exp(-r*T)
    for j in range(m):
        t,S = ito(S_0,T,n,r,sigma)
        v_t = path_payoff(S,E)
        total = total + v_t
    price =  v_0*((total)/float(m))
    return price, v_t



if __name__ == '__main__':
    # Testing all the functions with variables
    a = np.array([3,5,7,10,15])
    c = len(a)
    b = np.array([100,204,98,77,150])
    print("Path Payoff A",path_payoff(a,20))
    print("Path payoff A",path_payoff(a,15))
    print(b)
    print("Path payoff B",path_payoff(b,98))
    print("Path payoff B",path_payoff(b,68))

    print("ito 1",ito(100, 1, 4, 0.05, 0.2))
    print("ito 2",ito(200, 1, 4, 0.05, 0.2))
    print("ito 3",ito(150, 1, 8, 0.05, 0.2))

    payoff_function = 110
    print("Monte Carlo E = 100, m = 100", monte_carlo(payoff_function, 100, 1, 0.05, 0.2, 100, 100))
    print("Monte Carlo E = 100, m = 1000", monte_carlo(payoff_function, 100, 1, 0.05, 0.2, 1000, 1000))

    payoff_function = 120
    print("Monte Carlo E = 150, m = 1000", monte_carlo(payoff_function, 100, 1, 0.05, 0.2, 100, 100))
    print("Monte Carlo E = 150, m = 1000", monte_carlo(payoff_function, 100, 1, 0.05, 0.2, 1000, 1000))
