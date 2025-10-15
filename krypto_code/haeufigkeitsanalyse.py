import numpy as np


filename = input ("Filename bitte:")       # unsere Files Klartext und encrypted aus Wireshark
infile   = open(filename, "r")
s0       = infile.read()                   # die Datei ist in der Zeichenkette s0 gespeichert
s        = s0.lower()                      # alle die Grossbuchstaben werden klein geschrieben
infile.close()

a_ASCII = ord('a')
absolute_haeufigkeit = [0]*26
anz_buchstaben = 0
for x in s:
    if x.isalpha():                 # x ist ein Charakter
        absolute_haeufigkeit[ord(x) - a_ASCII] += 1
        anz_buchstaben                         += 1
        

print("\nHäufigkeitsanalyse:\n")

for i in range(26):
    if absolute_haeufigkeit[i] == 0:
        print(chr(a_ASCII + i) + " taucht nicht auf!\t\t" + 
              "{0: >6.3f}".format(absolute_haeufigkeit[i]/anz_buchstaben) + "%")
    elif absolute_haeufigkeit[i] == 1:
        print(chr(a_ASCII + i) + " taucht 1 Mal auf:\t" + 
              "{0: >6.3f}".format(absolute_haeufigkeit[i]/anz_buchstaben) + "%")
    else:
        print(chr(a_ASCII + i) + " taucht " + str(absolute_haeufigkeit[i]) + " Mal:\t" + 
              "{0: >6.3f}".format(100*absolute_haeufigkeit[i]/anz_buchstaben) + "%")
    
print("\nGesamtzahl der Buchstaben:", anz_buchstaben)

print ("\nBuchstabe:", np.argmax(absolute_haeufigkeit)+1, " mit einer Häufigkeit von : ",np.max(absolute_haeufigkeit))


