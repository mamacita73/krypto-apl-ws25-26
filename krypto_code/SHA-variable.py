import hashlib

Mein_PW = input ("Gib bitte ein Passwort ein: ")

x=['md5','sha1','sha256', 'sha384', 'sha512']

for x in x:
   Mein_Hash = hashlib.new(x)
   Mein_Hash.update(Mein_PW.encode())
   print ("Gehashdes PW nach" , x, " = ", Mein_Hash.hexdigest())
   print ("Gehashdes PW nach" , x," hat = ", Mein_Hash.digest_size * 8 , "Bit Länge \n")
   
