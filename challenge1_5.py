# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 21:37:52 2023

@author: user
"""

import math

def repeating_key_xor(plaintext, key):
    
    key = (key * math.ceil(len(plaintext)/len(key)))[0:(len(plaintext))]
    
    plaintext = plaintext.encode()
    print("Bytes plaintext : {}".format(plaintext))
    key = key.encode()
    print("Bytes key : {}".format(key))
    
    if len(plaintext)==len(key): 
        xor_result = bytearray(byte ^ k for byte,k in zip(plaintext,key))
        hex_xor = ''.join(format(byte, '02x') for byte in xor_result )
        print(hex_xor)
    

repeating_key_xor("abousalimaissame@gmail.com", "aA0102")
repeating_key_xor("Aissam.2019", "alo")
repeating_key_xor("meiner herz", "nein")
    
    
    