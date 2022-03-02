from kombinuj import tekscior
counterpl=0
countercom=0
tekstczysty=tekscior('https://zajecia-programowania-xd.pl/flagi')
for i in tekstczysty:
    if '.pl' in i[-3:]:
      counterpl+=1
    if '.com' in i[-4:]:
      countercom+=1  
print('wszystkich stron: ',len(tekstczysty))
print('zakończonych pl: ',counterpl)
print('zakończonych com: ',countercom)