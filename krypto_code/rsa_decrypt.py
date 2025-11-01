#!/usr/bin/python
import math

def rsa_decrypt(n,d,y):
    x =y**d % n
    return x


x = rsa_decrypt(n=971963, d=11963, y=616561)

print("x:", x)