from math import sqrt

def jacobi(a,n):
 
    ans = 0
    residuo = 0
 
    if a == 0:
        if n == 1:
            ans = 1
        else:
            ans = 0
    elif a == 2:
        residuo = n%8
        if residuo == 7 or residuo == 1:
            ans = 1
        if residuo == 5 or residuo == 3:
            ans = -1
 
    elif a >= n:
        ans = jacobi(a%n, n)
    elif a%2 == 0:
        ans = jacobi(2,n)*jacobi(a/2,n)
    else:
        if a%4 == 3 and n%4 == 3:
            ans = -jacobi(n,a)
        else:
            ans = jacobi(n,a)
 
    return ans

n = 4230659086792057869605292356791
P = 1
Q = -3
delta =pow(P,2) - 4*Q
jac = jacobi(delta,n)

print(delta**2,jac)