# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:08:31 2019

@author: gorthy
"""

import time
import readFile
import encrypt
import decrypt
import os
#import wFile

''' 
global variables here
'''
global key
global cipher


""" Function definitions """

def wFileBytToNorm(data):
    if data == keyByts:
       f = open('keyBack.txt', 'w+b')
       keyByte = bytearray(data)
       f.write(keyByte)
       f.close()
    elif data == cipher:
        f = open('cipher.txt', 'w+b')
        keyByte = bytearray(data)
        f.write(keyByte)
        f.close()
    elif data == decypher:
        f = open('decypher.txt', 'w+b')
        keyByte = bytearray(data)
        f.write(keyByte)
        f.close()
    else:
        print("unknown identifier, debugging code needed")
        print(str(time.ctime()))
        print("Exiting ...")


if __name__ == "__main__":
    
    start_time = str(format(time.ctime()))
    print("Script Started at: " + start_time)
    print("")

    #fileSizeInBytes = os.path.getsize("key.txt")
    #print("keyFileSizeInBytes is: " + str(fileSizeInBytes))
      
    keyByts = readFile.main("key.txt")
    print("keyByt data: "+ str(keyByts))
    print("")

    fileSizeInBytes = os.path.getsize("input.txt")
    print("dataFileSizeInBytes is: " + str(fileSizeInBytes))
    
    inpDataByts = readFile.main("input.txt")
    print("inpDataByts: "+ str(inpDataByts))
    print("")
    
    cipher = encrypt.DESencryption(inpDataByts, keyByts)
    print("cipher: "+ str(cipher))
    #print(len(cipher))
    
    #wFileBytToNorm(key)  #takes list and converts back to normal data
    wFileBytToNorm(cipher)
    
    cipherByts = readFile.main("cipher.txt")
    decypher = decrypt.DESdecryption(cipherByts, keyByts)
    wFileBytToNorm(decypher)