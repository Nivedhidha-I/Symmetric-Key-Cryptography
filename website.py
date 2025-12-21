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
    pass

def substitution_cipher(text, key):
    pass

def vigenere_cipher (text, block_size, key):
    pass

def one_time_pad_cipher (text, key) :
    pass

def rail_fence_cipher (text_arr, key):
    pass

def permutation_cipher (text_arr, block_size, key):
    pass

def playfair_cipher (text_arr, key):
    pass

# STATIC CONTENT
Data = {
    "Caesar Cipher": {
        "Code": """def caesar_cipher (text):
    cipher_text = ''
    for t in text:
        c = chr(((ord(t) - 97 + 3) % 26) + 65)
        cipher_text += c
    
    plain_text = ''
    for c in cipher_text:
        p = chr(((ord(c) - 65 - 3) % 26) + 97)
        plain_text += p
    
    return ['3', cipher_text, plain_text]""", 
        "Description" : "Historically used by Julius Caesar, this method secures messages by shifting each letter three positions through the alphabet. It stands as a classic demonstration of confidentiality achieved through character rotation."
    },
    'Shift Cipher': {
        "Code": """""", 
        "Description" : ""
    },
    'Substitution Cipher': {
        "Code": """""", 
        "Description" : ""
    },
    'Vigenere Cipher': {
        "Code": """""", 
        "Description" : ""
    },
    'One Time Pad Cipher': {
        "Code": """""", 
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
            'Substitution Cipher',
            'Vigenere Cipher',
            'One Time Pad Cipher',
            'Rail Fence Cipher',
            'Permutation Cipher',
            'Playfair Cipher'
        )
    )

st.header(option)
st.subheader("Description")
st.write(Data[option]["Description"])
st.subheader("Live Demonstration")

inputText = st.text_input('Input Plaintext: ')
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

agree = st.checkbox('View function code')

if agree:
    st.subheader('Demo Code')
    st.code(Data[option]["Code"])