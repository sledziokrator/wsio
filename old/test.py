#from wygenerujliste import alf, num, spec


import os, pandas as pd


current_path=os.getcwd()
path = '/home/sledz/sandbox/wsio/bety/'

pliktxt = path+'worklisty.txt'
plikcsv=path+'worklisty.csv'
plikjson=path+'worklisty.json'
#tekst=str(open(pliktxt).read())

cs=pd.read_csv(plikcsv, sep=',')

cs.to_csv(current_path+'/outputy/zapisanycsv.csv')