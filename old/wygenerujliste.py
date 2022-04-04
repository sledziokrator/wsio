import string

alf=list(string.ascii_uppercase)
num=[pozycja for pozycja,litera in enumerate(alf,1)]
spec=[i for i in string.punctuation[:len(alf)]]

l1=[list(i) for i in zip(num,alf,spec)]
#print(l1)