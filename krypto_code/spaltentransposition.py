# Entschlüsselung einer Spaltentransposition
# gibt alle Varianten der Matrix aus (aussser fuer 1 und Gesamtzahl)
 
import numpy as np

text = input('Eingabe Geheimtext: ')
# leere Liste für Geheimtext
t = []*len(text)
# wandle Geheimtext in Liste um
for i in text:
	t.append(i)

# ermittle die Teiler der Buchstabenanzahl
def get_factors(x):
	# leere Liste fuer Faktoren
	f = []
	# durchlaufe Anzahl Buchstaben
	for i in range(1, x + 1):
		# wenn teilbar
		if x % i == 0:
			# erweitere Liste um Teiler
			f.append(i)
	return f

# erstelle Matrix
def get_matrix(t, f):
	# entferne Wert 1 und Wert der Buchstabenanzahl
	# 1 Spalte und 1 Zeile wird nicht dargestellt
	f = f[1:]
	f = f[:-1]
	# fuer Anzahl Spalten
	for col in f:
		# leerer String fuer Darstellung
		s = ""
		# Zeilen = Anzahl / Spalten
		row = int(len(t) / col)
		print('\nSpalten:', col,', Zeilen:',row)
		# erstelle Matrix aus Liste
		m = np.asarray(t).reshape(col, row).T
		print('Matrix:')
		# durchlaufe Anzahl der Zeilen
		for r in range(row):
			# Ausgabe der Spalteninhalte
			for c in range(col):
				print(m[r][c], end = " ")
				s = s + m[r][c]
			print()
		# Ausgabe des moeglichen Klartextes
		print('\nString:\n'+s)
		print('\n-----')

get_matrix(t, get_factors(len(text)))
