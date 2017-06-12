#Preetpal Basson UP416733

def a(x):           # Hashtag is used to tell python not to read this text 
    return 3.0*x      #Return command was used to go back to what the function was doing before its current command.
                
def b(x):
    return (7.0*x-5.0)/(2.0*x-7.0)
    
def d(x,y):                 #there are 2 variables being used which are labeled x, y and hence named in the function itself other wise python would not know what to do with the variable without assignment. 
    return (x**3.0)-(3.0*(x**2.0)*y)+(3.0*x*(y**2.0))-(y**3.0)

def single_compound(P,r,n):
    M=(1 + r)
    return (M^n)*P 



def main (): #Main function is where I call appoin the a function and use it some form. 
    #print('a',a(1.0),a(2.0),a(3.0))           #I use afew examples per function to test the results
   # print('b',b(0.0),b(1.0),b(2.0),b(3.0),b(4.0)) 
    #print('d',d(1.0,1.0),d(2.0,1.0),d(1.0,2.0),d(3.0,1.0)) #when using the variable I must use 2 values to represent x & y
    print(single_compound(5,0.05,2))

if __name__=="__main__":
    main() 