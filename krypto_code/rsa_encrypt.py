#!/usr/bin/python
import math

def rsa_encrypt(n,e,x):
    y =x**e % n
    return y 

y = rsa_encrypt(n=47921, e=17, x=40601)

print("y:", y)