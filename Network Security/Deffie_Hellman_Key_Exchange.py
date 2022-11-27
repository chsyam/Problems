q = int(input())
alpha = int(input())

Xa = int(input())
Xb = int(input())

Ya = pow(alpha,Xa,q) # Ya = (alpha ** Xa) % q
Yb = pow(alpha, Xb, q)  # Yb = (alpha ** Xb) % q

K1 = pow(Yb, Xa, q) # K1 = (Yb ** Xa) % q
K2 = pow(Ya, Xb, q)  # K2 = (Ya ** Xb) % q

print(K1,K2)