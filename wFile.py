# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 18:08:31 2019

@author: gorthy
"""


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

if '__name__' == '__main__':
    wFileBytToNorm()