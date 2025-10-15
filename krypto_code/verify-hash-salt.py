import hashlib
import uuid

#Aufruf zur Hashfunktion mit String zu Byte and hex und zufälligen Salt mit Doppelpunkt als Trennzeichen

def hashing(password):
    salt=uuid.uuid4().hex
    return hashlib.sha512(salt.encode() + password.encode()).hexdigest() + ":" + salt , salt

#Passwortvergleichs-Funktion    

def vergleich(hashed_password, user_password):
    password , salt = hashed_password.split(":")
    return password == hashlib.sha512(salt.encode() + user_password.encode()).hexdigest()
 
My_PW = input ("Bitte ein neues Passwort eingeben: ")

# Aufruf der hashing Funktion mit dem eigenem Passwort

hashed_password , salt = hashing(My_PW)

print('Dein Hash-Wert ist: ' , hashed_password , "\nSalt separat: " , salt)
i = 1
# Passwortkontrolle 3 x
while i <= 3 :   
      vergleich_pw = input("Zum Vergleich Ihr Passwort erneut eingeben: ")
      i =i + 1
      if vergleich(hashed_password, vergleich_pw):
           print("Passwort war korrekt! ")
           i = 5
      else:
           print("Leider stimmen die Passwörter nicht überein! ")

if i==4:
   print ("\nSorry! Leider dreimal falsch! ")
     
    
