# forming matrix from the plaintext
text = input().upper()
arr = []
for i in text:
    if i.isalpha():
        c = ord(i)-65
        arr.append(c)
while len(arr)%3!=0:
    arr.append(ord("X")-65)
newarr = []
for i in range(len(arr)):
    if i%3==0:
        newarr.append([])
    newarr[-1].append(arr[i])

# encryption process matrix multiplication with key
result = []
key = [[6,24,1], [13,16,10], [20,17,15]]
for i in range(len(newarr)):
    result.append([])
    for j in range(len(newarr[0])):
        val = 0
        for k in range(len(newarr[0])):
            val += (key[k][j] * newarr[i][k])
        result[-1].append(val % 26)
        print(chr((val%26) + 65))

# key matrix inverse process
det = 0
for i in range(3):
    det += key[0][i] * (key[1][(i+1)%3]*key[2][(i-1)%3] - key[1][(i-1)%3]*key[2][(i+1)%3])
det %= 26
for x in range(26):
        if det * x % 26 == 1:
            det = x
            break
keyIN = []
for i in range(3):
    keyIN.append([])
    for j in range(3):
        val = (key[(j+1)%3][(i+1)%3]*key[(j-1)%3][(i-1)%3] - key[(j+1)%3][(i-1)%3]*key[(j-1)%3][(i+1)%3])
        keyIN[-1].append((val * det)%26)

# decryption process matrix multiplication with key inverse
newresult = []
for i in range(len(result)):
    newresult.append([])
    for j in range(len(result[0])):
        val = 0
        for k in range(len(result[0])):
            val += (keyIN[k][j] * result[i][k])
        newresult[-1].append(chr((val%26) + 65))
print(newresult)
