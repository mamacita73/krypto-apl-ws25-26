import hashlib
for i , out in enumerate (dir(hashlib)):
    print (i , out)     #Allgorithmen der Hashlib
    
#Text Hashing

# Ausgabe der verfügbaren Algorithmen
print ("\nVerfügbare Algorithmen: \n ", hashlib.algorithms_available)
# Garantierte lauffähige Algorithmen 
print ("\nVerfügbare Algorithmen: \n ", hashlib.algorithms_guaranteed)

# Einfaches Passwort- oder Text-Hashing

Mein_PW = hashlib.md5(b'Mein Text')
print ("\n Gehashdes PW für Mein Text = ", Mein_PW.hexdigest())

#Variable Text/Passworteingabe

Mein_PW = input ("Gib bitte ein Passwort ein: ")
Mein_Hash = hashlib.md5(Mein_PW.encode())
print ("\n Gehashdes PW = ", Mein_Hash.hexdigest())



