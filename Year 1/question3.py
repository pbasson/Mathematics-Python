#Preetpal Basson UP416733

import math       #I started by importing math libery into python      
from math import sqrt #I then imported square root from the math liberies 

def vector_norm(x):
    n = len(x)              #len() command is used to list the number of variables.
    Z = 0.0                 #I set Z to equal to zero so I can create a running loop starting at this value.              
    for k in range(n):      #this uses the value worked out in len() for the range. 
        Z = Z + x[k]**2.0   
    return sqrt(Z)

def vector_normp(x, p): #similar to the function vector_norm except it uses 2 variables. 
    n = len(x)
    Z = 0.0
    for k in range(n):
        Z = Z + x[k]**p 
    return Z**(1.0/p)

def vector_dot(x, y): 
    n = len(x)
    assert n == len(y) #this line means that the vector size of both x & y must be the same for this function to run. 
    Z = 0.0
    for k in range(n):
        Z = Z + x[k]*y[k] #dot product is the must be multiplation of each value in x & y directly and then adding them. 
    return Z

def find_angle(x,y): #I needed to create a formula that found the angle between 2 vectors. I was initially told to find the angle from x.y=||x||.||y||cos(angle)
    return math.acos(vector_dot(x,y)/(vector_norm(x)*vector_norm(y)))*(180/math.pi) #I also used math terms from the libery such as math.acos & math.pi, to create this formula


def vector_zeros(n):
    v=[]
    for k in range(0,n):
        v.append(0.0)
    return v

def vector_max(x,y):
    n = len(x)  
    assert n == len(y)
    Z = vector_zeros(n)     #this creates the zero vector in the size of the len(x)
    for k in range(n):      #this then creates the loop that will add each variable in the vector, (e.g. x1+y1, x2+y2, x3+y3..)
        Z[k] = x[k] + y[k]  
    return Z




def main():
    x = [1.0,5.0,3.0,4.0,5.0,4.0,3.0,2.0,1.0]   #I used 4 vectors in the testing of the functions x,y,xx,yy. 
    y= [5.0,11.0,6.0,4.0,3.0,2.0,1.0,7.0,0.0]
    xx=[2.0,10.0,4.0]
    yy=[50.0,23.0,4.0]
    print("x",x)
    print("y",y)
    print("xx",xx)
    print("yy",yy)
    print("length of x",len(x))
    print("length of xx",len(xx))
    print("vector_norm of x",vector_norm(x))
    print("vector_norm of xx",vector_norm(xx))
    print("vector_normp x eg1",vector_normp(x,5.0))
    print("vector_normp x eg2",vector_normp(x,10.0))
    print("vector_normp xx eg1",vector_normp(x,8.0))
    print("vector_normp xx eg2",vector_normp(x,13.0))
    print("vector dot of x & y",vector_dot(x,y))
    print("vector dot of xx & yy",vector_dot(xx,yy))
    print("Angle of x & y",find_angle(x,y))
    print("Angle of xx & yy",find_angle(xx,yy))
    print('Vector Max of x & y',vector_max(x,y))
    print('Vector Max of xx & yy',vector_max(xx,yy))
    
if __name__ =="__main__":
    main()
    