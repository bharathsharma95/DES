# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:08:31 2019

@author: gorthy
"""

import time
import readFile
import encrypt
#import wFile
#import os

''' 
global variables here
'''
global key
global cipher


""" Function definitions """

def wFileBytToNorm(data):
    if data == key:
       f = open('keyBack.txt', 'w+b')
       keyByte = bytearray(data)
       f.write(keyByte)
       f.close()
    else:
        f = open('cipherBack.txt', 'w+b')
        keyByte = bytearray(data)
        f.write(keyByte)
        f.close()


if __name__ == "__main__":
    
    start_time = str(format(time.ctime()))
    print("Script Started at: " + start_time)
    print("")

    #fileSizeInBytes = os.path.getsize("key.txt")
    #print("keyFileSizeInBytes is: " + str(fileSizeInBytes))
    
    
    key = readFile.main("key.txt")
    #print("keyByt data: "+ str(key))
    #print("")

    #fileSizeInBytes = os.path.getsize("input.txt")
    #print("dataFileSizeInBytes is: " + str(fileSizeInBytes))
    
    inpDataByts = readFile.main("input.txt")
    print("inpDataByts: "+ str(inpDataByts))
    print("")
    
    cipher = []
    cipher = encrypt.DESencryption(inpDataByts, key)
    print("cipher: "+ str(cipher))
    #print(len(cipher))
    
    wFileBytToNorm(key)  #takes list and converts back to normal data
    wFileBytToNorm(cipher)