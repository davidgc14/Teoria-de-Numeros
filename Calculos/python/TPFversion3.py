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

###########################################################
###########################################################
###########################################################
# Valores a introducir por el usuario:
n = 2647849547930825548751933021224632491399
P = 1
Q = 58
# delta = (P + sqrt(P**2 - 4*Q))/2
delta = P**2 - 4*Q
# jac = jacobi(delta,n)
jac = -1
# Datos de las iteraciones: 2 3 5 7 11 125263161782269243 457538832345169229
r = (n - jac) 
k = 0
U1 = 0
U2 = 1
binary = bin(r)[2:]

# inicialización de la impresión:
m = 0
#print("m", "k", "U1", "U2")
#print(m, k, U1, U2)

# Ciclo de iteraciones:
for i in binary: 
    if i == '0':
        k *= 2
        aux = [2 * U1 * U2 - P * (U1**2), (U2**2) - Q * (U1**2)]
    else:
        k = 2*k + 1
        aux = [(U2**2) - Q *(U1**2), P * (U2**2) - 2 * Q * U1 * U2]

    U1 = aux[0] % n
    U2 = aux[1] % n

    m += 1
    # print(m,"&", k,"&", U1,"&", U2,"\\")


# Certificación de primalidad:
V = 2 * U2 - P * U1
# print("V = ",V)

print("Uk = ", U1)

x = V % n
if x > n/2:
    x = x - n

if U1 == 0:
    if 2*Q == x and jac == -1:
        print("PRIMO")
    elif 2*Q == x and jac == 1:
        print("PRIMO")
    else: 
        print("COMPUESTO")