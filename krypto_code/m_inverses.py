import math
import decimal


def m_inverses(a,n):
    while math.gcd(a,n)>1:
         print("Die Zahlen a und n sind nicht teilerfremd")
         b = 0
         return(n,a,b)
    b = 0
    h = 2
    while h!=1:
          b = b + 1
          h = a * b % n
    return (n,a,b)


a = int (decimal.Decimal (input ("Eingabe Zahl a = ")))
n = int (decimal.Decimal (input ("Eingabe Modul n = ")))

(n,a,b) = m_inverses(a,n)

if b != 0:
    print ("\nZahl a:", a,"\nZahl b:",b,"\nModul n:",n)
    print ("\nÜberprüfung  a * b (mod n):", a * b % n)
