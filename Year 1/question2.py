#Preetpal Basson UP416733

def magnitude(x): # in this function it produces modulus. Meaning any value below 0 is multipled by -x hence becoming x and any value above 0 is x.
    if x < 0.0:
        return -x
    return x

def maximum(x, y): #In this function if x is equal to or greater than y then return x however is y is greater it returns y.
    if x>=y:
        return x
    return y


def max_mag(x,y):   #In this function the values of x & y first go through the magnitude function making modulus the values. Then it runs in the maximum function whether x is greater or equal to y or y is greater. 
    return maximum(magnitude(x),magnitude(y))

def delta(i,j): #In this function it has prefined the conditions as if both i = j (== is used as assignment). It is the similar function as maximum however it does not return the variables value, but 1 or 0. 
    if i==j:
        return 1.0
    return 0.0


def main(): # testing the functions variables with values.   
    print('Magnitude',magnitude(-2.0), magnitude(-1.0),magnitude(0.0),magnitude(1.0),magnitude(2.0)) 
    print('Maximum',maximum(3.0,2.0),maximum(4.0,4.0),maximum(1.0,2.0))
    print('Max_mag',max_mag(-7.0,2.0),max_mag(-1.0,-1.0),max_mag(2.0,-8.0))
    print('Delta',delta(1.0,1.0),delta(2.0,1.0))

if __name__ =="__main__":
    main()
    