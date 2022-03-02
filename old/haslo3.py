import random
import string

lower = string.ascii_lowercase
upper=string.ascii_uppercase
num = string.digits
specs=string.punctuation

ilosc=''

while not isinstance(ilosc,int):
    try:
        ilosc=int(input('Ile znaków w haśle? (8-20): '))
    except:
        print('E, no panie, ale długość hasła tylko w cyferkach!')

if ilosc < 8:
    print('Za mało znaków! Ustawiam na 8 gościu, bo cię okradną')
    ilosc=8
elif ilosc > 20:
    print('Za dużo znaków! Panie, kto ci to zapamięta?')
    ilosc=20

typyname=['małych liter','dużych liter','cyferek','znaków specjalnych']
typy=[0,0,0,0]


iloscpozostala=ilosc

def nowytyp(index,ilezostalo):
    global iloscpozostala
    print()
    print('zostało ', iloscpozostala, ' znaków.')
    print('Ile ',typyname[index],'?')
    typy[index]=int(input())
    iloscpozostala=iloscpozostala-typy[index]
    if iloscpozostala==0:
        print('Koniec znaków!')
        typy[index+1:]=[0]*ilezostalo
    elif iloscpozostala<0:
        print('Ło gościu, przeholowałeś! Daję maksimum i nara')
        typy[index]=iloscpozostala+typy[index]
        typy[index+1:]=[0]*ilezostalo
    if iloscpozostala<=0:
        haslo=''.join(random.sample(lower,typy[0])+random.sample(upper,typy[1])+random.sample(num,typy[2])+random.sample(specs,typy[3]))
        haslo=''.join(random.sample(haslo,len(haslo)))
        print()
        print('No i proszę, twoje przekombinowane hasło to:',haslo)
        print()
        quit()
    if typy[2]>10:
        print('Panie, więcej jak 10 cyferek to my nie mamy! Daję maks i elo!')
        typy[2]=10

nowytyp(0,3)
nowytyp(1,2)
nowytyp(2,1)

typy[3]=iloscpozostala

haslo=''.join(random.sample(lower,typy[0])+random.sample(upper,typy[1])+random.sample(num,typy[2])+random.sample(specs,typy[3]))
haslo=''.join(random.sample(haslo,len(haslo)))
print()
print('No i proszę, twoje przekombinowane hasło to:',haslo)
print()
