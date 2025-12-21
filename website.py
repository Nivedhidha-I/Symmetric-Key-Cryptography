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
    
    return [str(key), result]

def rail_fence_cipher (text_arr, key):
    pass

def permutation_cipher (text_arr, block_size, key):
    pass

def playfair_cipher (text_arr, key):
    pass

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
        "Description" : "Historically used by Julius Caesar, this method secures messages by shifting each letter three positions through the alphabet. It stands as a classic demonstration of confidentiality achieved through character rotation."
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
        "Description" : "A generalized Caesar Cipher where the user defines the shift value (Key). It illustrates the fundamental principle of Symmetric Encryption and the risks of small key spaces."
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
        "Description" : ""
    },
    'Rail Fence Cipher': {
        "Code": """""", 
        "Description" : ""
    },
    'Permutation Cipher': {
        "Code": """""", 
        "Description" : ""
    },
    'Playfair Cipher': {
        "Code": """""", 
        "Description" : ""
    }
}

# WEBSITE CODE
st.title("Cryptography Demonstrator")
st.info("An interactive tool to learn and explore symmetric key cryptography.")
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
    if option not in ['Rail Fence Cipher', 'Permutation Cipher']:
        if not (inputText.isalpha()) :
            st.error('Input string must only contain alphabets.')
        else:
            inputText = inputText.lower()
        text = np.array([])
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