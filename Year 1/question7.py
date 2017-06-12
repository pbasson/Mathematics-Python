#Preetpal Basson UP416733

def calculate_dx(a,b,n):
    return (b-a)/float(n)


def squ(x):
    return x**3

def rect_rule(f,a,b,n):
    Z=0.0
    dx=calculate_dx(a,b,n)
    for k in range(0,n-1):
        x= 1
        Z=Z+ (dx*f(x))
    return Z

def trap_rule(f,a,b,n):
    Z=0.0
    dx=calculate_dx(a,b,n)
    for k in range(0,n-1):
        x= 3
        third=(f(a)+f(b))/2
        area=dx*(f(x)+third)
        Z=Z+ area
    return Z
    
#def six_sixteenths(f,a,b,n):
   # Z=0.0
    #dx=calculate_dx(a,b,n)
    #x#d=(6*dx)/16
#    for k in range(1,n,3):
#        
#        
#    for k in range(2,n,3):
    
#    for k in range(2,n,3):
 #   return Z


    
    
    
def main():
    #print(calculate_dx(0,8,100))
   # print(rect_rule(squ,0,15,10))
    print(trap_rule(squ,1,3,1000))
   # print(six_sixteenths(squ,0,10,10))


if __name__ =="__main__":
    main()
    