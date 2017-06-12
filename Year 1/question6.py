#Preetpal Basson UP416733

def cubic(a,b,c,d,x):
    return (a*x**3)+(b*x**2)+(c*x)+d

def poly_degree(a):
    return len(a)-1

def poly_eval(a,x):
    m=len(a)
    z=0.0
    for k in range(0,m):
        z= z+ (a[k])*(x**k)
    return z

def poly_horner(a,x):

    pass


def main():
    a=[1,1,1]
    b=[2,2]
    #print('Cubic eg 1',cubic(1,1,1,1,1))
    #print('Cubic eg 2',cubic(1,1,1,1,2))
    print(poly_eval(a,2))
    print(poly_degree(b))


if __name__ == "__main__":
    main()
