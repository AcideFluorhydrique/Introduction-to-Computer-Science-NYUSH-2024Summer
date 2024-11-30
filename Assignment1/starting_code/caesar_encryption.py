#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 09:56:01 2021

@author: bing
"""

import random
import string
# import copy
def caesarEncrypt(message, codebook, shift):
    '''
    - you can compute the index of a character, or,
    - you can convert the codebook into a dictionary
    '''
    
    encrypted = ""
    ##put your code here

    # codebook_copy = copy.deepcopy(codebook)
    dictionary = {}
    for i in range(len(codebook)):
        if i < len(codebook) - shift:
            dictionary[codebook[i]] = codebook[i + shift]
        else:
            dictionary[codebook[i]] = codebook[i + shift - len(codebook)]
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

    # print(dictionary)
    for j in message:
        if j in dictionary:
            # print(dictionary)
            encrypted += dictionary[j]
        else:
            encrypted +=j
        # print(encrypted)
    # print(encrypted)

    return encrypted


def caesarDecrypt(message, codebook, shift):
    decrypted = ""
    ##put your code here

    dictionary = {}
    for i in range(len(codebook)):
        if i >= shift:
            dictionary[codebook[i]] = codebook[i - shift]
        else:
            dictionary[codebook[i]] = codebook[i - shift + len(codebook)]
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    # print(dictionary)
    for j in message:
        if j in dictionary:
            # print(dictionary)
            decrypted += dictionary[j]
        else:
            decrypted +=j
        # print(decrypted)

    
    return decrypted








if __name__ == "__main__":
    ##The following several lines generate the codebook
    ##Please don't change it
    random.seed("Caesar")
    
    codebook = []
    for e in string.ascii_letters:
        codebook.append(e)
        
    random.shuffle(codebook)
    print("Your codebook:")
    print(codebook)
    ## end of the codebook generation
    
    m = "Hello Kitty!"
    shift = 3
    encoded = caesarEncrypt(m, codebook, shift)
    decoded = caesarDecrypt(encoded, codebook, shift)
    print("Origin:", m)
    print("Encoded:", encoded)
    print("Decoded", decoded)