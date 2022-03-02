import requests

def tekscior(adres):
   tekst=requests.get(adres).text
   tekst=tekst[1668:]
   tekst=tekst.replace('</p>','')
   tekst=tekst.replace('<br>','')
   tekst=tekst.replace('</br>','')
   tekst=tekst.split('<p>')
   tekst=tekst[1:]
   tekstczysty=[]
   for i in tekst:
      i=i.replace('-','')
      i=i.strip()
      if 'oczekujące' in i:
         continue 
      tekstczysty.append(i)
   tekstczysty.sort()
   return tekstczysty


#https://zajecia-programowania-xd.pl/flagi
#for i in tekstczysty:
#   print(i)