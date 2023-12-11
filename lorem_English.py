#https://www.sttmedia.com/characterfrequency-english

import random
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cons = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'x', 'c', 'v', 'b', 'n', 'm', 'th', 'he', 'an'] #cons... souhlasky
cons_w = [9, 234, 568, 937, 166, 611, 414, 203, 192, 611, 23, 87, 424, 20, 273, 106, 154, 680, 253, 30, 30, 15]
vowe = ['a', 'e', 'i', 'o', 'u', 'y'] #vowe... samohlasky
vowe_w = [834, 1260, 671, 770, 285, 204]
struktura = ["CV", "CVCV","CCV", "CVC", "CCVCC"]

start = "Lorem English"
word = ""
        ## C = souhlaska, V = samohlaska


struktura_now = random.choices(struktura)
#struktura_now = ["CV"]
def slabika():
    syll = ""
    if struktura_now == ["CV"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choice(vowe)
        return syll
    
    elif struktura_now == ["CVCV"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choice(vowe)
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choice(vowe)
        return syll

    elif struktura_now == ["CCV"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choice(vowe)
        return syll
    
    elif struktura_now == ["CVC"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choice(vowe)
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        return syll
    
    elif struktura_now == ["CCVCC"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choice(vowe)
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        return syll




print(slabika())