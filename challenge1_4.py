# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 16:10:03 2023

@author: user
"""
from challenge1_set3 import find_best_decryption

def read_lines_from_file(file_path):
    lines = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line) 
    return lines

def detect_single_xor_line(file_path):
    chunks = read_lines_from_file(file_path)
    best_score = 0
    for chunk in chunks:
        decrypted, key, curr_score = find_best_decryption(chunk)
        if curr_score > best_score:
                best_score = curr_score
                best_key = key
                plaintext = decrypted
    print(f"Decrypted text (key {best_key}): {plaintext}")       

if __name__ == '__main__' :

    detect_single_xor_line('cipher-hex-string.txt')

    



