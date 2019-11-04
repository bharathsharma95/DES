# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:08:31 2019

@author: gorthy
"""

def DESencryption(data,key):
    outData = data
    for rounds in range(8):
        for i in range(len(data)):
            if (i%2==0):
                dataBytes = [data[i]] + [data[i+1]]
                keyByte = key[rounds]
                outData[i:i+2] = iteration(dataBytes, keyByte)
        #print("outDataByts: "+ str(outData))
    data = outData
    return outData
    
def iteration(dataBytes,keyByte):
    #Takes 2bytes of data and 1 byte of key
    #does an iteration and outputs it as a list
    #Eg: dataBytes = [data1, data2]
    #    keyByte = [key1]
    
    dataL = dataBytes[0]
    dataR = dataBytes[1]
    dataLdash = dataR
    dataRdash = dataL ^ keyByte
    outData = [dataLdash] + [dataRdash]
    return outData

