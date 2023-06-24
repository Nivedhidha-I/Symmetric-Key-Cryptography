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
    return [n,e,d]
key = RSA_key_generation(11, 13)
public_key = [key[0], key[1]]
private_key = [key[0], key[2]]

# functions for RSA and Digital Signature
import hashlib

def RSA_encryption(pu_key, data):
    # Encrypted_Data = (m^e)% n 
    enc = ""
    for m in data:
        enc += chr((ord(m)**pu_key[1]) % pu_key[0])
    return enc

def RSA_decryption(pr_key, data):
    # Decrypted_Data = (c^d)% n
    dec = ""
    for c in data:
        dec += chr((ord(c)**pr_key[1]) % pr_key[0])
    return dec

def Digital_Signature_Creation(dataSent):
    return [dataSent, RSA_encryption(public_key, hashlib.sha256(dataSent.encode()).hexdigest())]

def Digital_Signature_Verification(dataReceived):
    print(hashlib.sha256(dataReceived[0].encode()).hexdigest())
    print(RSA_decryption(private_key, dataReceived[1]))
    if hashlib.sha256(dataReceived[0].encode()).hexdigest() == RSA_decryption(private_key, dataReceived[1]):
        return True
    return False

# execution of RSA and Digital Signature process
dataToSend = "Harry"
dataAndDigitalSignature = Digital_Signature_Creation(dataToSend)
print(dataToSend)
print(dataAndDigitalSignature)
print(Digital_Signature_Verification(dataAndDigitalSignature))
