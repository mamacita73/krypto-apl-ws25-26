import math
import decimal

def rsa_encrypt(n,e,x):                         #RSA Verschlüsselung
      y=x**e % n
      return y

def rsa_decrypt ( n , d , y ) :                 #RSA Entschlüsselung
      x = y** d % n
      return x
      
def rsa_key ( p , q, e ) :                      #RSA Key-Generierung
      n= p * q
      phi_n = (p-1)*(q-1)
      
      while math.gcd (e, phi_n) > 1:
           e = e+1
          
      d = 0
      h = 2
      while h !=1 :
           d = d + 1
           h = e * d % phi_n
           
      return (n , e , d , phi_n )


def verschlüsseln() :  
    
    print ("\n######### Verschlüsselung Ziffer #########")
           
    klar     = int(input("Klartexteingabe (Ziffer) bitte: "))
    x       = rsa_encrypt(keys[0],keys[1],klar)
    
    print ("Deine geheime Ziffer : ", x,"\n")
    return()

def entschlüsseln() :
    
    print ("\n####### Entschlüsselung Ziffern  #########")
           
    geheim = int(decimal.Decimal (input("Geheim-dezimal: ")))
    print ("Decrypt:", rsa_decrypt (keys[0], keys[2], geheim),"\n")
    return()

#Key-Bildung
def keybilden():
    global keys
    print("Erzeugung RSA-schlüssel")
    p = int (decimal.Decimal (input ("Bitte Primzahlen eingeben p = ")))
    q = int (decimal.Decimal (input ("Bitte Primzahlen eingeben q = ")))
    e = int (decimal.Decimal (input ("Bitte öffentliches e bzw. Startpunkt e = ")))

#Primzahltest sollte folgen
    
    keys = rsa_key (p,q,e)
    print ("Die Keys lauten n, e, d, phi_n " , keys )
    return()


def auswahl_fkt():
    
    auswahl = int (input ("Stop 0 \nKeybilden 1 \nVerschlüsseln 2 \nEntschlüssel 3 \nEingabe :"))
    test=1
    if auswahl == 1:
        keybilden()
    if auswahl == 2:
        verschlüsseln()
    if auswahl == 3:
        entschlüsseln()
    if auswahl == 0:
        test = 0
        return(test)
    return(test)



#Hauptprogramm
test=1
keybilden()
while test:
    test = auswahl_fkt()
  

print('\n Programm Ende')
