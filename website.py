# IMPORT REQUIRED MODULES
import numpy as np
import random as r 
import streamlit as st 


# CRYPTOGRAPHIC ALGORITHMS
def caesar_cipher (text, method):
    result = ''
    if method == "Encrypt":
        for p in text:
            c = chr(((ord(p) - 97 + 3) % 26) + 97)
            result += c
    
    else: 
        for c in text:
            p = chr(((ord(c) - 97 - 3) % 26) + 97)
            result += p
    
    return ['3', result]

def shift_cipher (text, method, key):
    result = ''
    if method == "Encrypt":
        for t in text:
            c = chr(((ord(t) - 97 + key) % 26) + 97)
            result += c
    else:
        for c in text:
            p = chr(((ord(c) - 97 - key) % 26) + 97)
            result += p
    
    return [str(key), result]

def vigenere_cipher (text, method, block_size, key):
    result = ''
    if method == "Encrypt":
        for t in range(0, len(text), block_size):
            c_block = text[t : (t + block_size)]
            for cb in range(len(c_block)):
                c = chr(((ord(c_block[cb]) - 97 + key[cb]) % 26) + 97)
                result += c
    else:
        for c in range(0, len(text), block_size):
            p_block = text[c : (c + block_size)]
            for pb in range(len(p_block)):
                p = chr(((ord(p_block[pb]) - 97 - key[pb]) % 26) + 97)
                result += p
    
    return [str(key), result]

def rail_fence_cipher (text, method, key):
    if method == "Encrypt":
        result = ''
        for i in range(1, key+1):
            if i == key or i == 1:
                for j in range(i-1, len(text), ((key*2)-2)):
                    result += text[j]
            else:
                j = i-1
                c = 1
                while (j < len(text)):
                    result += text[j]
                    if c % 2 == 1:
                        j += (key-i)*2
                    else:
                        j += (i-1)*2
                    c += 1
    else:
        result = np.empty(len(text), dtype='U1')
        k = 0
        for i in range(1, key+1):
            if i == key or i == 1:
                for j in range(i-1, len(text), ((key*2)-2)):
                    result[j] = text[k]
                    k += 1
            else:
                j = i-1
                c = 1
                while (j < len(text)):
                    result[j] += text[k]
                    k += 1
                    if c % 2 == 1:
                        j += (key-i)*2
                    else:
                        j += (i-1)*2
                    c += 1
        result = ''.join(result)

    return [str(key), result]

def permutation_cipher (text, method, block_size, key):
    result = ''
    if method == "Encrypt":
        for t in range(0, len(text), block_size):
            c_block = text[t: (t + block_size)]
            for cb in range(len(c_block)):
                result += c_block[key[cb]]
    else:
        for c in range(0, len(text), block_size):
            p_block = text[c: (c + block_size)]
            for pb in range(len(p_block)):
                for k in range(len(key)):
                    if pb == key[k]:
                        result += p_block[k]
    
    return [str(key), result]

def playfair_cipher (text, method, key):
    result = ''
    if method == "Encrypt":
        for t in range(0, len(text), 2):
            t1 = text[t]
            res1 = np.where(key == t1)
            pos1 = list(list(zip(res1[0], res1[1]))[0])
            t2 = text[t+1]
            res2 = np.where(key == t2)
            pos2 = list(list(zip(res2[0], res2[1]))[0])
            if pos1[0] == pos2[0]:
                pos1[1] = 0 if (pos1[1] == 4) else pos1[1]+1 
                pos2[1] = 0 if (pos2[1] == 4) else pos2[1]+1
            elif pos1[1] == pos2[1]:
                pos1[0] = 0 if (pos1[0] == 4) else pos1[0]+1 
                pos2[0] = 0 if (pos2[0] == 4) else pos2[0]+1
            else:
                pos1[1], pos2[1] = pos2[1], pos1[1]
            t1 = key[pos1[0]][pos1[1]]
            t2 = key[pos2[0]][pos2[1]]
            result += t1 + t2
    
    else:
        for t in range(0, len(text), 2):
            c1 = text[t]
            c2 = text[t+1]
            res1 = np.where(key == c1)
            pos1 = list(list(zip(res1[0], res1[1]))[0])
            res2 = np.where(key == c2)
            pos2 = list(list(zip(res2[0], res2[1]))[0])
            if pos1[0] == pos2[0]:
                pos1[1] = 4 if (pos1[1] == 0) else pos1[1]-1 
                pos2[1] = 4 if (pos2[1] == 0) else pos2[1]-1
            elif pos1[1] == pos2[1]:
                pos1[0] = 4 if (pos1[0] == 0) else pos1[0]-1 
                pos2[0] = 4 if (pos2[0] == 0) else pos2[0]-1
            else:
                pos1[1], pos2[1] = pos2[1], pos1[1]    
            c1 = key[pos1[0]][pos1[1]]
            c2 = key[pos2[0]][pos2[1]]
            result += c1 + c2
       
    return [str(key), result]

# STATIC CONTENT
Data = {
    "Caesar Cipher": {
        "Code": """def caesar_cipher (text, method):
    result = ''
    if method == "Encrypt":
        for p in text:
            c = chr(((ord(p) - 97 + 3) % 26) + 97)
            result += c
    
    else: 
        for c in text:
            p = chr(((ord(c) - 97 - 3) % 26) + 97)
            result += p
    
    return ['3', result]""", 
        "Description" : "Historically used by Julius Caesar, this method secures messages by shifting each letter three positions through the alphabet. It stands as a classic demonstration of confidentiality achieved through fixed character rotation."
    },
    'Shift Cipher': {
        "Code": """def shift_cipher (text, method, key):
    result = ''
    if method == "Encrypt":
        for t in text:
            c = chr(((ord(t) - 97 + key) % 26) + 97)
            result += c
    else:
        for c in text:
            p = chr(((ord(c) - 97 - key) % 26) + 97)
            result += p
    
    return [str(key), result]""", 
        "Description" : "A generalized Caesar Cipher where the user defines the shift value (Key). It illustrates the fundamental principle of Symmetric Encryption—where the same secret is used to lock and unlock data—and highlights the risks of small key spaces vulnerable to brute-force attacks."
    },
    'Vigenere Cipher': {
        "Code": """def vigenere_cipher (text, method, block_size, key):
    result = ''
    if method == 'Encrypt':
        for t in range(0, len(text), block_size):
            c_block = text[t : (t + block_size)]
            for cb in range(len(c_block)):
                c = chr(((ord(c_block[cb]) - 97 + key[cb]) % 26) + 97)
                result += c
    else:
        for c in range(0, len(text), block_size):
            p_block = text[c : (c + block_size)]
            for pb in range(len(p_block)):
                p = chr(((ord(p_block[pb]) - 97 - key[pb]) % 26) + 97)
                result += p
    
    return [str(key), result]""", 
        "Description" : "A landmark in cryptography, this polyalphabetic substitution cipher uses a keyword to apply different shifts to each letter. By breaking the simple frequency patterns of a single-shift cipher, it introduces the concept of masking data patterns to resist basic cryptanalysis."
    },
    'Rail Fence Cipher': {
        "Code": """def rail_fence_cipher (text, method, key):
    if method == "Encrypt":
        result = ''
        for i in range(1, key+1):
            if i == key or i == 1:
                for j in range(i-1, len(text), ((key*2)-2)):
                    result += text[j]
            else:
                j = i-1
                c = 1
                while (j < len(text)):
                    result += text[j]
                    if c % 2 == 1:
                        j += (key-i)*2
                    else:
                        j += (i-1)*2
                    c += 1
    else:
        result = np.empty(len(text), dtype='U1')
        k = 0
        for i in range(1, key+1):
            if i == key or i == 1:
                for j in range(i-1, len(text), ((key*2)-2)):
                    result[j] = text[k]
                    k += 1
            else:
                j = i-1
                c = 1
                while (j < len(text)):
                    result[j] += text[k]
                    k += 1
                    if c % 2 == 1:
                        j += (key-i)*2
                    else:
                        j += (i-1)*2
                    c += 1
        result = ''.join(result)

    return [str(key), result]""", 
        "Description" : "Unlike substitution, this cipher scrambles the message by writing it in a zig-zag pattern across multiple 'rails' and reading it off row by row. It serves as a visual introduction to Transposition—the art of securing information by rearranging its structure rather than changing the characters themselves."
    },
    'Permutation Cipher': {
        "Code": """def permutation_cipher (text, method, block_size, key):
    result = ''
    if method == "Encrypt":
        for t in range(0, len(text), block_size):
            c_block = text[t: (t + block_size)]
            for cb in range(len(c_block)):
                result += c_block[key[cb]]
    else:
        for c in range(0, len(text), block_size):
            p_block = text[c: (c + block_size)]
            for pb in range(len(p_block)):
                for k in range(len(key)):
                    if pb == key[k]:
                        result += p_block[k]
    
    return [str(key), result]""", 
        "Description" : "A mathematical approach to transposition where the message is divided into fixed-size blocks and the characters within each block are reordered based on a specific key. This demonstrates the 'diffusion' principle, a core component of modern encryption like DES and AES."
    },
    'Playfair Cipher': {
        "Code": """def playfair_cipher (text, method, key):
    result = ''
    if method == "Encrypt":
        for t in range(0, len(text), 2):
            t1 = text[t]
            res1 = np.where(key == t1)
            pos1 = list(list(zip(res1[0], res1[1]))[0])
            t2 = text[t+1]
            res2 = np.where(key == t2)
            pos2 = list(list(zip(res2[0], res2[1]))[0])
            if pos1[0] == pos2[0]:
                pos1[1] = 0 if (pos1[1] == 4) else pos1[1]+1 
                pos2[1] = 0 if (pos2[1] == 4) else pos2[1]+1
            elif pos1[1] == pos2[1]:
                pos1[0] = 0 if (pos1[0] == 4) else pos1[0]+1 
                pos2[0] = 0 if (pos2[0] == 4) else pos2[0]+1
            else:
                pos1[1], pos2[1] = pos2[1], pos1[1]
            t1 = key[pos1[0]][pos1[1]]
            t2 = key[pos2[0]][pos2[1]]
            result += t1 + t2
    
    else:
        for t in range(0, len(text), 2):
            c1 = text[t]
            c2 = text[t+1]
            res1 = np.where(key == c1)
            pos1 = list(list(zip(res1[0], res1[1]))[0])
            res2 = np.where(key == c2)
            pos2 = list(list(zip(res2[0], res2[1]))[0])
            if pos1[0] == pos2[0]:
                pos1[1] = 4 if (pos1[1] == 0) else pos1[1]-1 
                pos2[1] = 4 if (pos2[1] == 0) else pos2[1]-1
            elif pos1[1] == pos2[1]:
                pos1[0] = 4 if (pos1[0] == 0) else pos1[0]-1 
                pos2[0] = 4 if (pos2[0] == 0) else pos2[0]-1
            else:
                pos1[1], pos2[1] = pos2[1], pos1[1]    
            c1 = key[pos1[0]][pos1[1]]
            c2 = key[pos2[0]][pos2[1]]
            result += c1 + c2
       
    return [str(key), result]""", 
        "Description" : "The first literal digram substitution cipher, it encrypts pairs of letters using a $5$ x $5$ grid. By encrypting two letters at once, it significantly complicates frequency analysis and represents an early leap toward more complex block-based encryption."
    }
}

# WEBSITE CODE
st.title("Cryptography Demonstrator")
st.html("<i>— An interactive tool to learn and explore symmetric key cryptography.</i>")
with st.sidebar:
    option = st.selectbox(
        'Algorithms',
        (
            'Caesar Cipher',
            'Shift Cipher',
            'Vigenere Cipher',
            'Rail Fence Cipher',
            'Permutation Cipher',
            'Playfair Cipher'
        )
    )

st.header(option)
st.subheader("Description")
st.write(Data[option]["Description"])
st.subheader("Live Demonstration")

method = st.selectbox("Method", ("Encrypt", "Decrypt"))
if method == "Encrypt":
    inputText = st.text_input('Input Plaintext: ')
else:
    inputText = st.text_input('Input Ciphertext: ')
if len(inputText) != 0 :
    text = np.array([])
    if option not in ['Rail Fence Cipher', 'Permutation Cipher']:
        if not (inputText.isalpha()) :
            st.error('Input string must only contain alphabets.')
        else:
            inputText = inputText.lower()
        for iT in inputText:
            text = np.append(text, iT)
    else: 
        for iT in inputText:
            text = np.append(text, iT)

    obj = None
    if option == 'Caesar Cipher':
        obj = caesar_cipher(text, method)
    elif option == 'Shift Cipher':
        key = int(st.number_input('Input the key: ', min_value=1, max_value=25))
        obj = shift_cipher(text, method, key)
    elif option == 'Vigenere Cipher':
        block_size = int(st.number_input('Input number of characters: ', min_value=2))
        key_text = st.text_input('Input a string of alphabets: ').lower()
        if not (key_text.isalpha() and len(key_text) == block_size) :
            st.error('Number of characters in Input String must be equal to number of Blocks.')
        else:
            key = np.array([]).astype(int)
            for kt in key_text:
                key = np.append(key, (ord(kt) - 97))
            obj = vigenere_cipher(text, method, block_size, key)
    elif option == 'Rail Fence Cipher':
        key = int(st.number_input('Input depth level: ', min_value=2, max_value=max(2, len(text) - 1)))
        if not (len(inputText) >= 3) :
            st.error('Input string must have minimum 3 characters.')
        else:
            obj = rail_fence_cipher(text, method, key)
    elif option == 'Permutation Cipher':
        block_size = int(st.number_input('Input block size: ', min_value=3, max_value=9)) 
        text_arr = np.append(text, np.repeat(" ", (block_size - (len(text) % block_size))))
        st.text(f"Assign a unique rank (1 to {block_size}) to each column position:")
        cols = st.columns(block_size)
        key = []

        available_ranks = list(range(1, block_size + 1))
        for i in range(block_size):
            with cols[i]:
                choice = st.selectbox(
                    f"Position {i+1}",
                    options=available_ranks,
                    index=i, 
                    key=f"perm_pos_{i}"
                )
                key.append(choice-1)

        if len(set(key)) != block_size:
            st.error("Invalid Key: Each number must be used exactly once. Please resolve duplicate selections.")
        else:
            st.success("Valid Permutation Key!")
            
            obj = permutation_cipher(text_arr, method, block_size, key)
    else:
        key_text = st.text_input('Input a string: ').lower()
        if not (key_text.isalpha() and key_text != '') :
            st.error('Input string must only contain alphabets.')
        else:
            key = np.array([])
            for kt in key_text:
                if (kt != 'j') and (kt not in key) :
                    key = np.append(key, kt)
            for i in range(97, 123):
                if chr(i) not in key and chr(i) != 'j':
                    key = np.append(key, chr(i))
            key = np.reshape(key, (5,5))
            
            textArr = np.array([])
            for t in range(len(text)):
                if text[t] == 'j' :
                    text[t] = 'i'
                textArr = np.append(textArr, text[t])
                if t != (len(text) - 1) and text[t] == text[t+1] :
                    textArr = np.append(textArr, 'x')
            if len(textArr) % 2 != 0 :
                textArr = np.append(textArr, 'x')
            obj = playfair_cipher(textArr, method, key)
    
    if obj != None:
        st.markdown('Output')
        st.text('Key: ' + obj[0])
        if method == "Decrypt":
            st.text('Plain Text: ' + obj[1])
        else:
            st.text('Cipher Text: ' + obj[1])

agree = st.checkbox('View Function Code')

if agree:
    st.subheader('Demo Code')
    st.code(Data[option]["Code"])