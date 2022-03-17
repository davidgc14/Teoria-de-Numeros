# Valores a introducir por el usuario:
n = 34539388448652514879742656254743
P = 1
Q = -1

# Datos de las iteraciones:
k = 0
U1 = 0
U2 = 1
binary = bin(n+1)[2:]

m = 0
print("m", "k", "U1", "U2")
print(m, k, U1, U2)

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
    print(m, k, U1, U2)


