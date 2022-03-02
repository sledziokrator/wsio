import requests
flagi_tekst= requests.get('https://zajecia-programowania-xd.pl/flagi').text
flagi_tekst=flagi_tekst.split('<p>-')
slownik={}
lista=[]
for f in flagi_tekst:
	f=f.replace('</p>','')
	f=f.replace('<h2><b>Zawisło 766 Flag.</b></h2><p>677 zawisło oficjalnie.<p>a 89 kolejnych bez rejestracji.<p>90 kolejnych nadal walczy.<p><b>Czy Twoja flaga zawisła? Wpisz ctrl+f</b><p>i poszukaj swojej flagi. Twoja flaga nie jest tu obecna wcale albo <b>nie jest</b> wymieniona od myślnika? Zgłoś ją oficjalnie.<p>Aby Twoja flaga pojawiła się oficjalnie <a href="https://zajecia-programowania-xd.pl/szturm_na_aws/caly_formularz">zarejestruj się.</a> a tym samym dołącz do Zajęć Programowania xD<p><b>A walczący? Wysyłaj im krzepiące wiadomości i pomagaj na <a href=\'https://discord.gg/BSpzQWUwk3\'>naszym discordzie</a>:</b><p>zulos#1437 , MagdaGrochoa#6151, jaspersmeadow#4571, Robert#2893, Trissabela#7833, alixIA (xe/xem)#8159, voxu#6002, Daniel7005#7265, Nerfi#3900, Magda19#6599, zalew#2311, python.py#5931, Nada#6483, Ni_Hu-Hu#2893 , szwung#8387, alcon#2432, sepo#2620, aleks.dab#6098, Kod#7516, AgentDkKabelek#4423, Felczer#3459, Aneta#1937, Hybris#6862, пициух#2755, michał#1899, Tomek Czernecki#7148, Istalri#5959, korczynskitomasz22#2539, //Kruz#4299, chrzanekz#1346, to nie rower smakówy#1993, Figus#6817, miss17moniczka#7050, Kari#4238, Ewelina_111#5624, jaqa#2305, Gdl21#8466, Ognomed#4419, sangadin#9370, Kasia#7046, mszuster#2299, obiektywny_wojtazz#4174, neex#7817, aluszka#8232, anulka2584#5395, wilczus#5486, kwawrzyniak#2996, Alpenfrq#4374, Addy#8963, XalCheRm #0364, NeQu#1585, ArkadiuszA #7961, Przemas#3897, Karutso#0388, wachluk#5295, shemaster#9409, jacekbalagane#5720, iktorn#2172, mocarz#4716<br></br><p><b>Flagi:</b>', '')
	f=f.replace('<br>','')
	f=f.replace('</br>','')
	f=f.replace('<b>','')
	f=f.replace('</b>','')
	f=f.replace('foxnox.pl<p>Flagi oczekujące na <a href="https://zajecia-programowania-xd.pl/szturm_na_aws/caly_formularz"> rejestrację</a>:<p>gregkozicki.pl<p>test.konradlapka.site<p>niebyt.pl<p>plusart.pro<p>test.wykrywaj.pl<p>pvtrk.pl<p>trzydwatrzy.pl<p>domibukowska.pl<p>tomekpython.online<p>hlwnv.com.pl<p>maczupikczu.online<p>dupa.twojadomena.pl<p>e-security.cloud<p>w-dziedzic.pl<p>runningwarrior.pl<p>localhost<p>pythontu.pl<p>progress-ab.pl<p>ab-solution.pl<p>zulos.pl<p>dt3.eu<p>pytonportfolio.pl<p>lubuskieklunkry.pl<p>projekty-patrycjaksmrz.pl<p>malinowapogoda.edu.pl<p>piotrekxd.pl<p>andysz.bieda.it<p>damianbialas.pl<p>przemekwrona.pl<p>pimpa.pl<p>wozyweselne.pl<p>kingvszka.pl<p>mikropatolog.pl<p>isp7.pl<p>kocilegat.pl<p>python-programming.marzec.eu<p>torododendron.pl<p>gosiatesterka.pl<p>dominisiaczkowo.pl<p>wyqp.pl<p>edukodu.pl<p>python-cave.pl<p>arek-pe.pl<p>lukasz-blechar.pl<p>jestemjonson.pl<p>yabol2137.pl<p>adavxcq.pl<p>cryptella.pl<p>danielekwafelek.pl<p>borovski.e-qov.pl<p>dt3.pl<p>wladek-py.pl<p>daco-python.pl<p>cyfrowydzik.pl<p>foremka.tk<p>despresso.pl<p>wetwater.pl<p>hadr.tk<p>youras.pl<p>inzpython.pl<p>em45.pl<p>flag.artbit.com.pl<p>mrmoose.com.pl<p>junioronly.com<p>pigalu.pl<p>puunina.szczecin.pl<p>masterofsnakes.pl<p>ribjata.pl<p>mojapierwszadomena.pl<p>kamilzeglen.pl<p>uczesieprogramowac.pl<p>urszkam.pl<p>bookreview.pl<p>szimilandia.pl<p>soczkowato.pl<p>ng-python.pl<p>agnieszkaf.pl<p>voxu.pl<p>tengel.pl<p>do-it-today.pl<p>hornowek.aqi.eco/pl<p>ehoze-developer.pl<p>rclimate.pl<p>python-learning.pl<p>emobox.pl<p>korneliusz-burian.pl<p>programatorek.pl<p>i-profil.pl<p>python.weselle.pl','')
	f=f.strip()
	lista.append(f)


lista.sort()


for i in lista:
	try:
		print(lista.index(i),i, requests.get('http://'+i+'/haslo').status_code)
	except:
		continue

