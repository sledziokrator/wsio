import random
import string

lower = string.ascii_lowercase
upper=string.ascii_uppercase
num = string.digits
specs=string.punctuation

ilosc=int(input('Ile znaków w haśle? (8-20): '))
if ilosc < 8:
    print('Za mało znaków! Ustawiam na 8 gościu, bo cię okradną')
    ilosc=8
elif ilosc > 20:
    print('Za dużo znaków! Panie, kto ci to zapamięta?')
    ilosc=20

typy=[0,0,0,0]
iloscpozostala=ilosc
###############
print('Zostało ', iloscpozostala, ' znaków.')
typy[0]=int(input('Ile małych liter?: '))
iloscpozostala=iloscpozostala-typy[0]
if iloscpozostala==0:
    print('Koniec znaków!')
    typy[1:3]=[0]*2
elif iloscpozostala<0:
    print('Ło gościu, przeholowałeś! Daję maksimum i nara')
    typy[0]=ilosc
    typy[1:3]=[0]*2

if iloscpozostala<=0:
    haslo=''.join(random.sample(lower,typy[0])+random.sample(upper,typy[1])+random.sample(num,typy[2])+random.sample(specs,typy[3]))
    haslo=''.join(random.sample(haslo,len(haslo)))
    print()
    print('No i proszę, twoje poebane hasło:',haslo)
    quit()

########################    
print('Zostało ', iloscpozostala, ' znaków.')
typy[1]=int(input('Ile dużych liter?: '))
iloscpozostala=iloscpozostala-typy[1]

if iloscpozostala==0:
    print('Koniec znaków!')
    typy[2:3]=[0]*1
elif iloscpozostala<0:
    print('Ło gościu, przeholowałeś! Daję maksimum i nara')
    typy[1]=iloscpozostala+typy[1]
    typy[2:3]=[0]*1
    

if iloscpozostala<=0:
    haslo=''.join(random.sample(lower,typy[0])+random.sample(upper,typy[1])+random.sample(num,typy[2])+random.sample(specs,typy[3]))
    haslo=''.join(random.sample(haslo,len(haslo)))
    print()
    print('No i proszę, twoje poebane hasło:',haslo)
    quit()
####################### 
print('Zostało ', iloscpozostala, ' znaków.')
typy[2]=int(input('Ile cyferek?: '))
if typy[2]>10:
    print('Panie, więcej jak 10 cyferek to my nie mamy! Daję maks i elo!')
    typy[2]=10
    

iloscpozostala=iloscpozostala-typy[2]
if iloscpozostala==0:
    print('Koniec znaków!')
    typy[3]=0
elif iloscpozostala<0:
    print('Ło gościu, przeholowałeś! Daję maksimum i nara')
    typy[2]=iloscpozostala+typy[2]
    typy[3]=0


if iloscpozostala<=0:
    haslo=''.join(random.sample(lower,typy[0])+random.sample(upper,typy[1])+random.sample(num,typy[2])+random.sample(specs,typy[3]))
    haslo=''.join(random.sample(haslo,len(haslo)))
    print()
    print('No i proszę, twoje poebane hasło:',haslo)
    quit()


typy[3]=iloscpozostala



haslo=''.join(random.sample(lower,typy[0])+random.sample(upper,typy[1])+random.sample(num,typy[2])+random.sample(specs,typy[3]))
haslo=''.join(random.sample(haslo,len(haslo)))
print()
print('No i proszę, twoje poebane hasło:',haslo)