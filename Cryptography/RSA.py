# key generation process for RSA algorithm
def RSA_key_generation(p,q):
    n = p*q
    phi = (p-1) * (q-1)
    e = 2
    while e < phi:
        if phi%e !=0:
            break
        e+=1
    d = 0
    k = 1
    while d == 0:
        if (k*phi + 1) % e == 0:
            d = int((k*phi + 1) / e)
            break
        k += 1
    return [n, e, d]

key = RSA_key_generation(11, 13)
public_key = [key[0], key[1]]
private_key = [key[0], key[2]]
print(private_key)

# Encrypted_Data = (m^e)% n
def RSA_encryption(pu_key, data):
    enc = ""
    for m in data:
        enc += chr((ord(m)**pu_key[1]) % pu_key[0])
    return enc

# Decrypted_Data = (c^d)% n
def RSA_decryption(pr_key, data):
    dec = ""
    for c in data:
        dec += chr((ord(c)**pr_key[1]) % pr_key[0])
    return dec

data = "abc"
en = RSA_encryption(public_key, data)
de = RSA_decryption(private_key, en)
print(en)
print(de)
