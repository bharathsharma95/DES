""" import statements """
from __future__ import with_statement
import time
import os


""" Function definitions """
def encryption(data,key):
    outData = []
    #for rounds in range(8):
    for i in range(len(data)):
            if (i%2==0):
                dataBytes = [data[i]] + [data[i+1]]
                keyByte = key[0]
                outData = outData + [iteration(dataBytes, keyByte)]
    print(outData)
    return outData
    
def iteration(dataBytes,keyByte):
    dataL = dataBytes[0]
    dataR = dataBytes[1]
    dataLdash = dataR
    dataRdash = dataL ^ keyByte
    #print(dataLdash, dataRdash)
    outData = dataLdash + dataRdash 
    return outData    
    

def openFile(file):
    print(file + " opened in 'rb' mode")
    with open(file, 'rb') as fid:
      byte = fid.read(1)
      fileInBytes = list(byte)
      while byte:
          byte = fid.read(1)
          fileInBytes = fileInBytes + list(byte)
    fid.close()
    return fileInBytes

if __name__ == "__main__":
    
    start_time = str(format(time.ctime()))
    print("Script Started at: " + start_time)
    print("")

    fileSizeInBytes = os.path.getsize("key.txt")
    print("keyFileSizeInBytes is: " + str(fileSizeInBytes))
    
    key = openFile("key.txt")
    print("keyByt data: "+ str(key))
    print("")

    fileSizeInBytes = os.path.getsize("input.txt")
    print("dataFileSizeInBytes is: " + str(fileSizeInBytes))
    
    inpDataByts = openFile("input.txt")
    print("inpDataBin: "+ str(inpDataByts))
    print("")
    
    cipher = []
    cipher = encryption(inpDataByts, key)
    