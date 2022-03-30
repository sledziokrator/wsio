
'''tekst=input('Jaki tekst ci odwrócić?: ')
tekst=''.join(tekst[::-1])
print('Tu masz odwrócony tekst:', tekst)
'''
tekst=input('Jaki tekst ci odwrócić?: ')
tekst=[i for -i in tekst]
print(tekst)

'''
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
'''