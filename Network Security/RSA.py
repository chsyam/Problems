def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)

p = int(input()) # 3
q = int(input()) # 5
message = int(input()) # 7

n = p * q

phi_n = (p-1)*(q-1)

# Calculate e
e = 2
for e in range(2,phi_n):
    if gcd(e,phi_n) == 1:
        break

# Calculate d
d = 0
for i in range(1,phi_n):
    x = 1 + i * phi_n
    if x % e == 0:
        d = int(x / e)
        break

cipher_text = message**e % n

print(cipher_text)

decrypted_text = cipher_text ** d % n

print(decrypted_text)

# Decrypted text and encrypted text are must and should same ... !!! 