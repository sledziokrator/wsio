import os
os.system('clear')
lista=[]
zakup=input('Co dodac do listy? Aby zamknac wpisz koniec: ')
lista.append(zakup)
print('Teraz lista zawiera: ' + str(lista))

def robliste():
 zakup=input('\nCo dodac do listy? Aby zamknac wpisz koniec: ')
 lista.append(zakup)
 if(zakup!='koniec'):
  print('Teraz lista zawiera: ' + str(lista)+'\n')

while(lista[-1]!='koniec'):
 robliste()



print('Twoja lista zawiera '+ str(len(lista)-1) +' elementow')

print(str(lista[0:-1]))




