ile=int(input ('Jak bardzo chuj?: '))
import os
import time
t0=time.time()
i=1
for i in range(ile):
 print ("chuj "+str(i+1))
 t1=time.time()
print('i juz nie chuj. Przeliczylem wszystkie te chuje w ' + str(round(t1-t0, 2)) + ' sekund')
if input('Czyscic?: ').upper()=='T':
 os.system('clear')
else:
 print('no ok')
