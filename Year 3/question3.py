'''416733'''

import math

def n(x):           #Normal probability

    a = math.exp((-1/float(2))*x**2)
    b = (2*math.pi)**(1/float(2))
    print'a',(a)
    print'b',(b)
    return  a/float(b)


def N(d):                       #Normal probability
    a = (1/float(2))*(1+math.erf(d/float(2)**(1/float(2))))
    return a


def calculate_d10_d20(S_0, E, T, r, sigma, q):  #Calculating d_10 & d_20
    a = math.log(S_0/float(E)) + ((r - q + ((1/float(2))*(sigma**2)))*T)
    b = sigma*((T)**(1/float(2)))
    d_10 = a/float(b)
    d_20 = d_10 - b
    return d_10, d_20



def bs_call(S_0, E, T, r, sigma, q):        #BS function
    d_10, d_20 = calculate_d10_d20(S_0, E, T, r, sigma, q)
    C = S_0*math.exp(-q*T)*N(d_10) - E*math.exp(-r*T)*N(d_20)
    return C


def commodity_call(S_0, E, T, r, sigma, Q): #Combination of Calculate d_10 & d_20 & Adjusted BS
    def commodity_d10_d20(S_0, E, T, r, sigma, Q):
        a = math.log(S_0/float(E)) + ((r + Q + ((1/float(2))*(sigma**2)))*(T))
        b = sigma*((T)**(1/float(2)))
        d_10 = a/float(b)
        d_20 = d_10 - b
        return d_10, d_20
    d_10, d_20 = commodity_d10_d20(S_0,E,T,r,sigma,Q)
    C = S_0*math.exp(Q*(T))*N(d_10) - E*math.exp(-r*(T))*N(d_20)
    return C


if __name__ == '__main__':
    # Testing all the functions with variables
    print("n",n(1))
    print("n",n(2))
    print("n",n(3))
    print("N",N(-1),N(0), N(1))
    print("N",N(-2),N(0), N(3))
    print("N",N(-5),N(0), N(6))
    print("Calculate", calculate_d10_d20(100, 90, 1, 0.05, 0.2, 0))
    print("Calculate", calculate_d10_d20(150, 90, 1, 0.05, 0.2, 0))
    print("BS Call", bs_call(100,80,2, 0.1, 0.2, 0))
    print("BS Call", bs_call(100,90,1,0.05, 0.2, 0))
    print("BS Call", bs_call(150,130,1,0.05, 0.2, 0))
    print("Commodity Call"), commodity_call(100, 90, 0.25, 0.05, 0.2, 0)
    print("Commodity Call"), commodity_call(100, 90, 1, 0.05, 0.2, 0)
    print("Commodity Call"), commodity_call(100, 90, 1, 0.05, 0.2, 0.2)
    print("Commodity Call"), commodity_call(100, 90, 1, 0.05, 0.2, 0.5)
    print("Commodity Call"), commodity_call(348, 350, 0.25, 0.07, 0.3, 0.04)