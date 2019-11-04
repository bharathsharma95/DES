# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 16:36:44 2019

@author: gorthy
"""

def DESdecryption(dataByts, keyByts):
    print("Decrypting file ...")
    print("")
    
    print("keyByt data: " + str(keyByts))
    print("")
    
    print("ciphDataByts: " + str(dataByts))
    print("")
    
    outData = dataByts
    for rounds in range(8):
        for i in range(len(dataByts)):
            if (i%2==0):
                dataBytes = [dataByts[i]] + [dataByts[i+1]]
                keyByte = keyByts[7-rounds]
                outData[i:i+2] = iteration(dataBytes, keyByte)
        #print("outDataByts: "+ str(outData))
    dataByts = outData
    return outData
    
    

def iteration(dataBytes,keyByte):
    #Takes 2bytes of data and 1 byte of key
    #does an iteration and outputs it as a list
    #Eg: dataBytes = [data1, data2]
    #    keyByte = [key1]
    
    dataL = dataBytes[0]
    dataR = dataBytes[1]
    dataLdash = dataR ^ keyByte
    dataRdash = dataL
    outData = [dataLdash] + [dataRdash]
    return outData