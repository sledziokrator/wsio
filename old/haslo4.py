import random
import string

lower = list(string.ascii_lowercase)
upper=list(string.ascii_uppercase)
num = list(string.digits)
specs=list(string.punctuation)

ilosclower= random.randrange(1,26)
iloscupper= random.randrange(1,26)
iloscnum= random.randrange(0,9)
iloscspecs= random.randrange(1,32)

def haslomocne(ilosclower,iloscupper,iloscnum,iloscspecs):
    haslomocne=''.join(random.sample(lower,ilosclower)+random.sample(upper,iloscupper)+random.sample(num,iloscnum)+random.sample(specs,iloscspecs))
    haslomocne=''.join(random.sample(haslomocne,len(haslomocne)))
    return haslomocne

final=haslomocne(ilosclower,iloscupper,iloscnum,iloscspecs)

