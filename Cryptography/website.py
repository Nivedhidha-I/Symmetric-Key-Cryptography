# IMPORT REQUIRED MODULES
import numpy as np
import random as r 
import streamlit as st 



# CRYPTOGRAPHIC ALGORITHMS
def caesar_cipher (text):
    cipher_text = ''
    for t in text:
        c = chr(((ord(t) - 97 + 3) % 26) + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        p = chr(((ord(c) - 65 - 3) % 26) + 97)
        plain_text += p
    
    return ['3', cipher_text, plain_text]


def shift_cipher (text, key):
    cipher_text = ''
    for t in text:
        c = chr(((ord(t) - 97 + key) % 26) + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        p = chr(((ord(c) - 65 - key) % 26) + 97)
        plain_text += p
    
    return [str(key), cipher_text, plain_text]


def substitution_cipher(text, key):
    cipher_text = ''
    for t in text:
        val = key[ord(t) - 97]
        c = chr(val + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        pos = int(np.where(key == (ord(c) - 65))[0])
        p = chr(pos + 97)
        plain_text += p
    
    return [str(key), cipher_text, plain_text]


def vigenere_cipher (text, block_size, key):
    cipher_text = ''
    for t in range(0, len(text), block_size):
        c_block = text[t : (t + block_size)]
        for cb in range(len(c_block)):
            c = chr(((ord(c_block[cb]) - 97 + key[cb]) % 26) + 65)
            cipher_text += c
    
    plain_text = ''
    for c in range(0, len(cipher_text), block_size):
        p_block = cipher_text[c : (c + block_size)]
        for pb in range(len(p_block)):
            p = chr(((ord(p_block[pb]) - 65 - key[pb]) % 26) + 97)
            plain_text += p
    
    return [str(key), cipher_text, plain_text]


def one_time_pad_cipher (text, key) :
    cipher_text = ''
    for t in range(len(text)) :
        c = chr(((ord(text[t]) - 97 + key[t]) % 26) + 65)
        cipher_text += c

    plain_text = ''
    for c in range(len(cipher_text)) :
        p = chr(((ord(cipher_text[c]) - 65 - key[c]) % 26) + 97)
        plain_text += p
    
    return [str(key), cipher_text, plain_text]


def rail_fence_cipher (text_arr, key):
    cipher_arr = np.transpose(text_arr)
    cipher_text = ""
    for c in range(len(cipher_arr)):
        cipher_text += "".join(cipher_arr[c])
        
    plain_arr = np.transpose(cipher_arr)
    plain_text = ""
    for p in range(len(plain_arr)):
        plain_text += "".join(plain_arr[p])
        
    return [str(key), cipher_text, plain_text]


def permutation_cipher (text_arr, block_size, key):
    cipher_text = ''
    for t in range(0, len(text_arr), block_size):
        c_block = text_arr[t: (t + block_size)]
        for cb in range(len(c_block)):
            cipher_text += c_block[key[cb]]
    
    plain_text = ''
    for c in range(0, len(cipher_text), block_size):
        p_block = cipher_text[c: (c + block_size)]
        for pb in range(len(p_block)):
            for k in range(len(key)):
                if pb == key[k]:
                    plain_text += p_block[k]
    
    return [str(key), cipher_text, plain_text]
    

def playfair_cipher (text_arr, key):
    cipher_text = ''
    for t in range(0, len(text_arr), 2):
        t1 = text_arr[t]
        res1 = np.where(key == t1)
        pos1 = list(list(zip(res1[0], res1[1]))[0])
        t2 = text_arr[t+1]
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
        cipher_text += t1 + t2
    
    plain_text = ''
    for t in range(0, len(cipher_text), 2):
        c1 = cipher_text[t]
        c2 = cipher_text[t+1]
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
        plain_text += c1 + c2
       
    return [str(key), cipher_text, plain_text]



# WEBSITE CODE
with st.sidebar:
    option = st.selectbox(
        'Cryptographic Algorithms',
        (
            'Caesar Cipher',
            'Shift Cipher',
            'Substitution Cipher',
            'Vigenere Cipher',
            'One Time Pad Cipher',
            'Rail Fence Cipher',
            'Permutation Cipher',
            'Playfair Cipher'
        )
    )


st.title(option.upper())
st.subheader('Live Demo')


inputText = st.text_input('Input the text to process: ').lower()
text = np.array([])
for iT in inputText:
    if iT.isalpha():
        text = np.append(text, iT)


if len(text) != 0 :
    obj = None
    if option == 'Caesar Cipher':
        code = '''def caesar_cipher (text):
    cipher_text = ''
    for t in text:
        c = chr(((ord(t) - 97 + 3) % 26) + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        p = chr(((ord(c) - 65 - 3) % 26) + 97)
        plain_text += p
    
    return ['3', cipher_text, plain_text]'''
    
        obj = caesar_cipher(text)
        
    elif option == 'Shift Cipher':
        code = '''def shift_cipher (text, key):
    cipher_text = ''
    for t in text:
        c = chr(((ord(t) - 97 + key) % 26) + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        p = chr(((ord(c) - 65 - key) % 26) + 97)
        plain_text += p
    
    return [str(key), cipher_text, plain_text]'''
        
        key = int(st.number_input('Input the key: ', min_value=1, max_value=25))
        obj = shift_cipher(text, key)

    elif option == 'Substitution Cipher':
        code = '''def substitution_cipher(text, key):
    cipher_text = ''
    for t in text:
        val = key[ord(t) - 97]
        c = chr(val + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        pos = int(np.where(key == (ord(c) - 65))[0])
        p = chr(pos + 97)
        plain_text += p
    
    return [str(key), cipher_text, plain_text]'''
        
        key = np.arange(start = 0, stop = 26)
        r.shuffle(key)
        obj = substitution_cipher(text, key)
        
    elif option == 'Vigenere Cipher':
        code = '''def vigenere_cipher (text, block_size, key):
    cipher_text = ''
    for t in range(0, len(text), block_size):
        c_block = text[t : (t + block_size)]
        for cb in range(len(c_block)):
            c = chr(((ord(c_block[cb]) - 97 + key[cb]) % 26) + 65)
            cipher_text += c
    
    plain_text = ''
    for c in range(0, len(cipher_text), block_size):
        p_block = cipher_text[c : (c + block_size)]
        for pb in range(len(p_block)):
            p = chr(((ord(p_block[pb]) - 65 - key[pb]) % 26) + 97)
            plain_text += p
    
    return [str(key), cipher_text, plain_text]'''
        
        block_size = int(st.number_input('Input number of characters: ', min_value=2))
        key_text = st.text_input('Input a string of alphabets: ').lower()
        if not (key_text.isalpha() and len(key_text) == block_size) :
            st.error('Input string must only contain ' + str(block_size) + ' alphabets.')
        else:
            key = np.array([]).astype(int)
            for kt in key_text:
                key = np.append(key, (ord(kt) - 97))
            obj = vigenere_cipher(text, block_size, key)
    
    elif option == 'One Time Pad Cipher':
        code = '''def one_time_pad_cipher (text, key) :
    cipher_text = ''
    for t in range(len(text)) :
        c = chr(((ord(text[t]) - 97 + key[t]) % 26) + 65)
        cipher_text += c
    
    plain_text = ''
    for c in range(len(cipher_text)) :
        p = chr(((ord(cipher_text[c]) - 65 - key[c]) % 26) + 97)
        plain_text += p
    
    return [str(key), cipher_text, plain_text]'''
        
        key = np.array([]).astype(int)
        for i in range(len(text)):
            key = np.append(key, r.randrange(26))
        obj = one_time_pad_cipher(text, key)
    
    elif option == 'Rail Fence Cipher':
        code = '''def rail_fence_cipher (text_arr, key):
    cipher_arr = np.transpose(text_arr)
    cipher_text = ""
    for c in range(len(cipher_arr)):
        cipher_text += "".join(cipher_arr[c])
        
    plain_arr = np.transpose(cipher_arr)
    plain_text = ""
    for p in range(len(plain_arr)):
        plain_text += "".join(plain_arr[p])
        
    return [str(key), cipher_text, plain_text]'''
        
        key = int(st.number_input('Input depth level: ', min_value=2, max_value=int(len(text)/2)))
        text_arr = np.append(text, np.repeat(" ", (key - (len(text) % key)))).reshape(key, -1)
        obj = rail_fence_cipher(text_arr, key)
    
    elif option == 'Permutation Cipher':
        code = '''def permutation_cipher (text_arr, block_size, key):
    cipher_text = ''
    for t in range(0, len(text_arr), block_size):
        c_block = text_arr[t: (t + block_size)]
        for cb in range(len(c_block)):
            cipher_text += c_block[key[cb]]
    
    plain_text = ''
    for c in range(0, len(cipher_text), block_size):
        p_block = cipher_text[c: (c + block_size)]
        for pb in range(len(p_block)):
            for k in range(len(key)):
                if pb == key[k]:
                    plain_text += p_block[k]
    
    return [str(key), cipher_text, plain_text]'''
        
        block_size = int(st.number_input('Input block size: ', min_value=2, max_value=len(text)))     
        key = np.array(range(block_size))
        r.shuffle(key)
        text_arr = np.append(text, np.repeat(" ", (block_size - (len(text) % block_size))))
        obj = permutation_cipher(text_arr, block_size, key)
    
    elif option == 'Playfair Cipher':
        code = '''def playfair_cipher (text_arr, key):
    cipher_text = ''
    for t in range(0, len(text_arr), 2):
        t1 = text_arr[t]
        res1 = np.where(key == t1)
        pos1 = list(list(zip(res1[0], res1[1]))[0])
        t2 = text_arr[t+1]
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
        cipher_text += t1 + t2
    
    plain_text = ''
    for t in range(0, len(cipher_text), 2):
        c1 = cipher_text[t]
        c2 = cipher_text[t+1]
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
        plain_text += c1 + c2
       
    return [str(key), cipher_text, plain_text]'''
        
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
                    continue
                textArr = np.append(textArr, text[t])
                if t != (len(text) - 1) and text[t] == text[t+1] :
                    textArr = np.append(textArr, 'x')
            if len(textArr) % 2 != 0 :
                textArr = np.append(textArr, 'x')
            obj = playfair_cipher(textArr, key)
    
    
    if obj != None:
        st.markdown('**Output**')
        st.text('Key: ' + obj[0])
        st.text('Cipher Text: ' + obj[1])
        st.text('Plain Text: ' + obj[2])
    
    agree = st.checkbox('View function code')

    if agree:
        st.subheader('Function Code')
        st.code(code)