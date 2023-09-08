# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:51:08 2023

@author: user
"""

import codecs
import base64

string_hex = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

bytes_hex = bytes.fromhex(string_hex)
#print(bytes_hex)
b64 = codecs.encode(bytes_hex, 'base64').decode()
"""
or
"""

autherB64 = base64.b64encode(bytes_hex).decode()

print(b64)
print(autherB64)



