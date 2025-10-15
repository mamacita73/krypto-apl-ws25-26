import math
import decimal

def ggt_v01(x, y):
    while x > 0 and y > 0:
        if x >= y:
            x = x - y
        else:
            y = y - x
    return x+y

def ggt_v02(x, y):
    rest = 1
    while rest != 0: 
        if x >= y:
            rest = x % y
            x = y
            y = rest
            ggt = x
        else:
            rest = y % x
            y = x
            x = rest
            ggt=y
    return ggt


p = int (decimal.Decimal (input ("Zahl 1 eingeben p = ")))
q = int (decimal.Decimal (input ("Zahl 2 eingeben q = ")))


print(" Größter gemeinsamer Teiler Ansatz 1:",ggt_v01(p,q),"\n")
print(" Größter gemeinsamer Teiler Ansatz 2:",ggt_v02(p,q),"\n")
