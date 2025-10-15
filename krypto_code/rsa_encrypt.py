#!/usr/bin/python
import math

def rsa_encrypt(n,e,x):
    y =x**e % n
    return y 
