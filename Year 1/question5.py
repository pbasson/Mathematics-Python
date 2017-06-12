#Preetpal Basson UP416733

def mid_point(a,b):
    return ((b+a)*0.5)
    
def func(x):                            #before the bisection step can be used, i must create a formula so that I can test the methods
    return 2*x**3-4*x**2+6*x-20   

def bisection_step(f,a,b):
    c=mid_point(a,b)        #c is assigned to the mid point.
    if f(a)*f(c)<=0:        #using the bisection method if the root lies between a & c then return a & c else c & b. 
        return a,c
    else:
        return b,c
    
def bisection_method(f,a,b,n):          #in this step a loop is created to do the bisection method N times.
    for k in range(1,n+1):
        (a,b)= bisection_step(f,a,b)
    r=mid_point(a,b)
    return r

def crossing_point(f,a,b):      #this creates the x value for the crossing point where y=0 based on the tangent line. 
    g=(f(b)-f(a))/(b-a)
    c=b-(f(b)/g)
    return c 

def chord_method(f,a,b,n):          #due to the a value being closer to the root then b, in N times the crossing point value will replace the b value. 
    for k in range(1,n+1):
        b=crossing_point(f,a,b)
    return b

def main():
    a,b= 2.0,3.0                            #in this main I have used the same formula but used 2 examples per function to test it. 
    print('a',a,'b',b)
    print('Mid Point',mid_point(10,20))
    print('Mid Point',mid_point(10,50))
    print('Bisection Method eg 1',bisection_method(func,a,b,10))
    print('Bisection Method eg 2',bisection_method(func,a,b,100))
    print('Crossing Point eg 1',crossing_point(func,2.0,3.0))
    print('Crossing Point eg 2',crossing_point(func,2.33,2.5))
    print('Chord Method eg 1',chord_method(func,a,b,10))
    print('Chord Method eg 2',chord_method(func,a,b,100))
    
if __name__ =="__main__":
    main()