#This program will decipher a code in Caesar's cipher
#To do - plug main into a decryption function
#Fix bug when code has spaces
#Fix bug so that alphabet ordinals roll back after z

import random
import sys
import os
import matplotlib
import string

#returns code from user input
def getCode(prompt):
    code = input(prompt).strip()
    return code

#gets the character length of the code
def codeLength(code):
    length = len(code)
    return length


#Main
usercode = getCode("What is the code? ")
uclength = codeLength(usercode)
codeCharacters = usercode[0:uclength]
characterList = []


#while the shift number is within range, keep generating possible codes
for shift in range(-26, 26):
    #while the letter index hasn't exceeded the letter amount in the original code, keep going
    for letter in range(0, uclength):
        charValue = ord(usercode[letter])
        #break inner loop iteration if the character being tested isn't in the alphabet
        if (charValue + shift) not in range(65, 122):
            characterList.clear()
            break
        else:
            characterList.insert(letter, chr(charValue + shift))
            letter = letter+1
    #after finishing shifting the letters, print the word, clear it and then print a new line
    #if the characterList is empty, don't print
    if len(characterList) == 0:
        break
    else:
        print(''.join(characterList))
        characterList.clear()
        shift = shift+1
        print (" ")


