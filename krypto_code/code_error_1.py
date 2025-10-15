#import math
import numpy as np

# Erzeugung Informationswort

i  = np.random.randint(2,size=2); # Informationswort

print ('Informationswort', i)

GM = np.array([[1,0,1,1,0],[0,1,1,0,1]]) # Generatormatrix
H  = np.array([[1,1,1,0,0],[1,0,0,1,0],[0,1,0,0,1]]) # Prüfmatrix

# Erzeugung Codewort

c = np.dot(i,GM) % 2

print ('Codeowrt', c)

# Erzeugung Fehlerwort

f = np.zeros(5) 

fehlerposition = np.random.randint(5,size=1);

f[fehlerposition] = 1;

# Erzeugung Empfangswort

y = np.add(c,f) % 2 # Empfangswort

print('Empfangswort', y)

# Dekodierung Empfangswort

s = np.dot(H,y) % 2

print('Syndrom', s)

weight = np.count_nonzero(f)

h0 = np.ones(5)

s0 = s.reshape(s.shape[0], 1)
h1 = s0*h0

#h1  = np.array([[s[0],s[0],s[0],s[0],s[0]],[s[1],s[1],s[1],s[1],s[1]],
#                    [s[2],s[2],s[2],s[2],s[2]]])

h2 = np.add(H,-h1) % 2

h3 = np.sum(np.abs(h2),axis = 0)

h4 = np.nonzero(h3<1)

print('Geschätzte Fehlerposition', h4[0]+1)

# geschätztes Fehlermuster

h5 = np.zeros(5) 
h5[h4[0]] = 1 

print('geschätzes Fehlerwort', h5)

# geschätztes Codewort

c1 =np.add(y,h5) % 2

print('geschätzes Codewort', c1)

# Klartext

i1 = [c1[0],c1[1]]

print('Klartext', i1)
