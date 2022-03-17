
n = 34539388448652514879742656254743
P = 1
Q = -1

k = 1
U1 = [k, 1]
U2 = [k+1, P]
binary = bin(n)[2:]

m = 0

for i in binary: 
    if i == '0':
        k *= 2
        aux = [2 * U1[1] * U2[1] - P * U1[1]^2, U2[1]^2 - Q * U1[1]^2]
    else:
        k = 2*k + 1
        aux = [U2[1]^2 - Q * U1[1]^2, P * U2[1]^2 - 2 * Q * U1[1] * U2[1]]

    U1 = [k, aux[0] % n]
    U2 = [k+1, aux[1] % n]

    m += 1
    print(m)
    print(U1)


