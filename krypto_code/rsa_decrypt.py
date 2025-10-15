#!/usr/bin/python
import math

def rsa_decrypt(n,d,y):
    x =y**d % n
    return x 
