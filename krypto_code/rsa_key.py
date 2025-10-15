#!/usr/bin/python
import math

def rsa_key(p,q):
    n = p*q
    phi_n = (p-1)*(q-1)
    e = 6157
    while math.gcd(e,phi_n)>1:
         e = e+1        
    d = 0
    h = 2
    while h!=1:
          d = d + 1
          h = e * d % phi_n
    return (n,e,d,phi_n) 
