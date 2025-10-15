import hashlib

#Aufruf zur Hashfunktion mit String zu Byte and hex

def hashing(password):
       return hashlib.sha512( password.encode()).hexdigest()

#Passwortvergleichs-Funktion    

def vergleich(hashed_password, user_password):
    password = hashed_password
    return password == hashlib.sha512(user_password.encode()).hexdigest()
 
My_PW = input ("Bitte ein neues Passwort eingeben: ")
# Aufruf der hashing Funktion mit dem eigenem Passwort
hashed_password = hashing(My_PW)
print('Dein Hash-Wert ist: ' , hashed_password)
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
     
    
