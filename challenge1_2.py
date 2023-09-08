# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 21:41:56 2023

@author: user
"""



def xor_2_buffer(buffer1, buffer2):
    
    if len(buffer1) != len(buffer2):
        raise ValueError("the two buffers doesn't have the same lentgh")
        
    byte_buff1 = bytes.fromhex(buffer1)
    print("First Buffer : {}".format(byte_buff1))
    byte_buff2 = bytes.fromhex(buffer2)
    print("Second Buffer : {}".format(byte_buff2))

    xor_result = bytearray( x ^ y for x,y in zip(byte_buff1, byte_buff2) )
    print("XOR Buffers : {}".format(xor_result))

    hex_xor = ''.join(format(byte, '02x') for byte in xor_result )
    print("FINAL XOR RESULT = {}".format(hex_xor))



xor_2_buffer('1c0111001f010100061a024b53535009181c', '686974207468652062756c6c277320657965')
    
    

















