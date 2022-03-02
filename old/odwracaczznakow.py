tekst=input('Jaki tekst ci odwrócić?: ')

ilosc=len(tekst)
ntekst=''
counter=1

for i in range(ilosc):
	ntekst=ntekst+tekst[ilosc-counter]
	counter+=1

print()
print('Tu masz odwrócony tekst:')
print()
print(ntekst)
print()
