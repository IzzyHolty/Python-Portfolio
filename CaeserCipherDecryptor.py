# Used this tutorial to help create this program https://www.youtube.com/watch?v=0wdRh7QVzbw
# Made global variables local inside functions so that functions are optimised and only decrypt needs to be called

import random
import sys
import os
import matplotlib
import collections
import string

#returns code from user input
def getCode(prompt):
    code = input(prompt).lower().strip()
    return code


#creates alphabet of shifted letters
def shiftThatAlphabet(shiftNumber):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    shiftedAlphabet = {}
    for i in range(0, 26):
        letter = alphabet[i]
        shiftedAlphabet[letter] = alphabet[(i+shiftNumber) % 26]
    return shiftedAlphabet

#uses alphabet of shifted letters to decrypt the word
def decrypt(code, shiftNumber):
    decryptedCode = ' '
    shiftedAlphabet = shiftThatAlphabet(shiftNumber)
    for letter in code:
        if letter in shiftedAlphabet:
            letter = shiftedAlphabet[letter]
            decryptedCode = decryptedCode + letter
        else:
            decryptedCode = decryptedCode + ' '
    return decryptedCode


#Main
userCode = getCode("What is the code? ")

for i in range(0, 26):
    message = decrypt(userCode, i)
    print(message)




