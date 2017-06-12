import math
import numpy as np
import random

def time(T, n):
    dt = T/float(n)
    return dt

def twin_process(S_0, T, n, r, sigma):

    t = np.zeros(n+1, dtype=float)
    S = np.zeros(n+1, dtype=float)
    U = np.zeros(n+1, dtype=float)
    assert len(S) == n+1
    dt = time(T,n)

    t[0] = 0.0
    S[0] = S_0
    U[0] = S_0

    for k in range(n):
        z = random.normalvariate(0,1)
        dW = sigma*math.sqrt(dt)*z
        t[k+1] = t[k]+dt
        S[k+1] = S[k]*math.exp((r-float(0.5)*sigma**2)*dt + dW)
        U[k+1] = U[k]*math.exp((r-float(0.5)*sigma**2)*dt - dW)
    return t, S, U


def twin_monte(payoff_function, S_0, T, r, sigma, n, m):
    E = payoff_function
    def path_payoff(S, E):
        return max(E - min(S), 0)

    total = float(0.0)
    d = math.exp(-r*T)

    for j in range(m):
        t,S, U = twin_process(S_0,T,n,r,sigma)
        s_t = path_payoff(S,E)
        u_t = path_payoff(U,E)
        total = total + ((s_t + u_t)/float(2))
    v_0 =  d*((total)/float(m))
    return v_0


def bs_call(S_0, E, T, r, sigma, q):
    def N(d):
        a = (1/float(2))*(1+math.erf(d/float(2)**(1/float(2))))
        return a

    def calculate_d10_d20(S_0, E, T, r, sigma, q):
        a = math.log(S_0/float(E)) + ((r - q + ((1/float(2))*(sigma**2)))*T)
        b = sigma*((T)**(1/float(2)))
        d_10 = a/float(b)
        d_20 = d_10 - b
        return d_10, d_20

    d_10, d_20 = calculate_d10_d20(S_0, E, T, r, sigma, q)
    C = S_0*math.exp(-q*T)*N(d_10) - E*math.exp(-r*T)*N(d_20)
    return C

def quicksand_call(S, E, L, T):
    n = T/len(S)
    t = np.zeros(n+1, dtype=float)
    S = np.zeros(n+1, dtype=float)

    t[0]= 0.0
    S[0] = S
    d = min(S)
    for k in range(n+1):
        if (d<L):
            return 0
    else:
        return max(S-E, 0)


def quicksand(S_0, E, T, r, sigma, q, L):
    S_T = quicksand_call(S,E,L,T)

    tx = (S_0/float(L))**(1-(2*r)/(sigma**2))
    Q_0 = bs_call(S_0, E, T, r, sigma, q) - tx*bs_call((L**2)/float(S_0), E, T, r, sigma, q)
    return Q_0

if __name__ == '__main__':


    print("Twin process 1",twin_process(100, 1, 4, 0.05, 0.2))
    print("Twin process 2",twin_process(100, 1, 8, 0.05, 0.2))
    print("Twin process 3",twin_process(150, 1, 4, 0.05, 0.2))
    print("Twin process 3",twin_process(150, 1, 8, 0.05, 0.2))

    payoff_function = 90
    print("Twin Monte 1", twin_monte(payoff_function, 100, 1, 0.05, 0.2, 100, 100))
    print("Twin Monte 2", twin_monte(payoff_function, 100, 1, 0.05, 0.2, 1000, 1000))

    payoff_function = 95
    print("Twin Monte 3", twin_monte(payoff_function, 100, 1, 0.05, 0.2, 100, 100))
    print("Twin Monte 4", twin_monte(payoff_function, 100, 1, 0.05, 0.2, 1000, 1000))

    S = [100, 150, 90, 30]

    S = [100,110,95,125]

    print("Quicksand", quicksand(100, 80, 2, 0.1, 0.2, 0, 90))

    payoff_function = 80
    print("Twin Monte", twin_monte(payoff_function, 100, 2, 0.1, 0.2, 1000, 1000))
    print(bs_call(100,80,2,0.1,0.2, 0))
    print(quicksand_call(S, 90, 80,1))