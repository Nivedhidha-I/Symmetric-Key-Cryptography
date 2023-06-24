# affine cipher code

key = [17,20]
text = input().upper()
arr = []
for i in text:
    if i.isalpha():
        c = chr(((key[0] * (ord(i)-65) + key[1]) % 26) + 65)
        arr.append(c)

print(arr)

text = []
for i in arr:
    a_1 = 0
    for x in range(26):
        if key[0] * x % 26 == 1:
            a_1 = x
            break
    p = chr(((a_1 * (ord(i) - 65 - key[1])) % 26) + 65)
    text.append(p)

print(text)
