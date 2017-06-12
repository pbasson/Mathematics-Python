#Preetpal Basson UP416733

def matrix_shape(a):
    m = len(a)          #len() notes the amount of variables in the list
    n = len(a[0])       #this len() lists the number of variables in the column of a matrix
    return (m,n)


def matrix_zeros(m,n):
    rows = []                    #[] is an empty list which can be any number can be added to
    for i in range(m):          #this means going across the rows hence why it is assigned as i.
        row = []
        for j in range(n):          #this means going down the columns hence why it is assigned as j.
            row.append(0.0)        #this is the value that is going to be appended in the column.
        rows.append(row)           #hence appending the rows list
    return rows

def matrix_lower(n):
    b = matrix_zeros(n,n)
    for i in range(n):
        for j in range(n):
            if i>j:
                b[i][j]=1.0
            else:
                b[i][j]=0.0

    return b


def matrix_transpose(a):
    (m, n) = matrix_shape(a)        #I started with creating len() for rows and columns
    b = matrix_zeros(n, m)          #next used the len() values to create a zero matrix
    for i in range(n):
        for j in range(m):
            b[i][j] = a[j][i]       #in this I defined that b[i][j]=a[j][i] which means that b is the transpose of a.
    return b



def matrix_sub(a, b):
    (m, n) = matrix_shape(a)                #first i create a len() of both a and b matrix.
    (o, p) = matrix_shape(b)
    assert m==o and n==p                    #in his step I assert that if both matrixs do not have the same size(row & columns) this function will not work.
    c = matrix_zeros(m, n)                  #create an empty matrix based on the size of matrix a.
    for i in range(m):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]     #matrix c is then used to hold the values of a-b
    return c

def matrix_mul(a, b):
    (m, n) = matrix_shape(a)
    (o, p) = matrix_shape(b)
    assert n == o                       # As with multiplication the columns of matrix a must be the same size as matrix b, otherwise this function will not work.
    c = matrix_zeros(m, p)
    for i in range(m):
        for j in range(p):
            Z = 0.0
            for k in range(n):
                Z = Z + a[i][k]*b[k][j] #this multiples each matrix row & column and then adds each interval
            c[i][j] = Z
    return c


def main():
    a = [[4,3,6],[2,4,0]]
    b= [[2,4,1],[0,3,12]]
    c=[[8,13,7],[21,2,11]]
    d=[[2,1],[4,7],[9,5]]
    h=[[0,0,0],[0,0,0],[0,0,0]]
    print('a',a)
    print('b',b)
    print('c',c)
    print('d',d)
    print('h',h)
    print('Matrix Shape of a',matrix_shape(a))
    print('Matrix Shape of d',matrix_shape(d))
    print('Matrix Zeros',matrix_zeros(3,3))
    print('Matrix Zeros',matrix_zeros(4,6))
    print('Matrix Sub of a & b',matrix_sub(a,b))
    print('Matrix Sub of c & b',matrix_sub(c,b))
    print('Matrix Transpose of a',matrix_transpose(a))
    print('Matrix Transpose of b',matrix_transpose(b))
    print('Matrix Transpose of c',matrix_transpose(c))
    print('Matrix Multi of a & d',matrix_mul(a,d))
    print('Matrix Multi of d & a',matrix_mul(d,a))
    print(matrix_lower(3))

if __name__ =="__main__":
    main()