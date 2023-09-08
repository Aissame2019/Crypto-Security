# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 23:05:22 2023

@author: user
"""


def score_text(text):
    
    expected_frequencies = {
        'a': 0.08167, 'b': 0.01492, 'c': 0.02782, 'd': 0.04253, 'e': 0.12702,
        'f': 0.02228, 'g': 0.02015, 'h': 0.06094, 'i': 0.06966, 'j': 0.00153,
        'k': 0.00772, 'l': 0.04025, 'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
        'p': 0.01929, 'q': 0.00095, 'r': 0.05987, 's': 0.06327, 't': 0.09056,
        'u': 0.02758, 'v': 0.00978, 'w': 0.02361, 'x': 0.00150, 'y': 0.01974,
        'z': 0.00074, ' ': 0.19181
    }

    text = text.lower()
    score = sum(expected_frequencies.get(char, 0) for char in text)
    return score

def xor_decrypt(ciphertext, key):
    key_byte = ord(key)
    decrypted = bytearray()
    for byte in bytes.fromhex(ciphertext):
        decrypted.append(byte ^ key_byte)
    return decrypted.decode('utf-8', errors='ignore')

def find_best_decryption(ciphertext):
    best_score = 0
    best_decryption = ""
    best_key = ""

    for key in range(256):  
        decrypted_text = xor_decrypt(ciphertext, chr(key))
        score = score_text(decrypted_text)
        if score > best_score:
            best_score = score
            best_decryption = decrypted_text
            best_key = chr(key)

    return best_decryption, best_key, best_score


if __name__ == '__main__' :
    
    ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    best_decryption, best_key, best_score = find_best_decryption(ciphertext)
    print("Best decryption:", best_decryption)
    print("Key:", best_key)















