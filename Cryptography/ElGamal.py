# key generation process for ElGamal algorithm
def ELGAMAL_key_generation(p):
    g = 2
    while g < p:
        arr = []
        for i in range(p):
            arr.append(g**i%p)
        if len(set(arr)) == p-1:
            break
        g += 1
    d = g+1
    e = g**d%p
    return [p,g,e,d]
key = ELGAMAL_key_generation(11)
public_key = [key[0], key[1], key[2]]
private_key = [key[0], key[3]]
print("Key: " + str(key))

# Encryption process for ElGamal
def ELGAMAL_encryption(pu_key, data):
    k = 3
    c = []
    c.append(pu_key[1]**k%pu_key[0])
    c.append(data * pu_key[2]**k % pu_key[0])
    return c

# Decryption process for ElGamal
def ELGAMAL_decryption(pr_key, data):
    val = data[0]**pr_key[1]
    for x in range(pr_key[0]):
        if val * x % pr_key[0] == 1:
            val = x
            break
    d = data[1] * val % pr_key[0]
    return d

data = 4
en = ELGAMAL_encryption(public_key, data)
print("Cipher Text: " + str(en))
de = ELGAMAL_decryption(private_key, en)
print("Plain Text: " + str(de))
