# Initialisierung
text = 'Heute lernen wir fuer Krypto'
#text = 'Jetzt wird es Ernst'
text = text.upper()
code = input("Gebe deinen Schlüssel ein: ")
code = int(code)

# Verarbeitung
verschluesselter_text = ''
for zeichen in text:
    zahl = ord(zeichen)
    neue_zahl = zahl + code
    if neue_zahl > ord('Z'):
        neue_zahl = neue_zahl - 26
    neuesZeichen = chr(neue_zahl)
    verschluesselter_text = verschluesselter_text + neuesZeichen
# Ausgabe
print(verschluesselter_text)

# -- ENTSCHLÜSSELUNG --

# Initalisierung
text = ''
# Verarbeitung
for zeichen in verschluesselter_text:
    zahl = ord(zeichen)
    neue_zahl = zahl - code
    if neue_zahl < ord('A'):
        neue_zahl = neue_zahl + 26
    if neue_zahl == 58:
        neue_zahl = 32
    neuesZeichen = chr(neue_zahl)
    text = text + neuesZeichen
# Ausgabe
print(text)
