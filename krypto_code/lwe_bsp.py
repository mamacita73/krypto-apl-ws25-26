import numpy as np
import random
import math

# Definition Parameter

q = 97
s = 5

# Definition Klartext

message = 0

# Erzeugung öffentlicher Schlüssel

a = np.array([80,86,19,62,2,83,25,47,20,58])

e = np.array([3,3,4,1,3,3,4,4,1,4])

b = (a*s + e) % q

print("\n------Parameter and Schlüssel-------")
print("Primzahl:\t",q)
print("Klartext (m):\t",message)
print("Public Key (a):\t",a)
print("Public Key (b):\t",b)
print("Fehler (e):\t",e)
print("Privat key (s):\t",s)

# Ver- und Entschlüsselung

print("\n------Ver- und Entschlüsselung-------")

sample= np.array([3,4,5,8,7]) 
print("ausgewählter Index aus a und b:\t",sample)

u=0
v=0

print("Ausgabe ausgewählte Elemente aus a und b:\t")

for x in range(0,len(sample)):
	print("[",a[sample[x]],b[sample[x]],"]", end=' ')
	u= u+a[sample[x]]
	v= v+b[sample[x]]

v=v+math.floor(q//2)*message

v = v%q
u = u%q

print()
print("\n------Berechnung von u und v -----------------")
print("Wert u:\t\t",u)
print("Wert v:\t\t",v)

print()
print("\n------Berechnung Klartext -----------------")

res=(v-s*u) % q

print("Das Ergebnis der Entschlüsselung ist: \t",res)

if (res>q/2):
	print("Der Klartext m hat den Wert 1")
else:
	print("Der Klartext m hat den Wert 0")




