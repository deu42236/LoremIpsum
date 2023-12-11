import random
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cons = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'x', 'c', 'v', 'b', 'n', 'm'] #cons... souhlasky
vowe = ['a', 'e', 'i', 'o', 'u', 'y'] #vowe... samohlasky
struktura = ["CV", "CVCV","CCV", "CVC", "CCVCC"]

start = "Lorem English"
word = ""
        ## C = souhlaska, V = samohlaska


struktura_now = random.choices(struktura)
#struktura_now = ["CV"]
def slabika():
    syll = ""
    if struktura_now == ["CV"]:
        syll = syll + random.choice(cons)
        syll = syll + random.choice(vowe)
        return syll
    
    elif struktura_now == ["CVCV"]:
        syll = syll + random.choice(cons)
        syll = syll + random.choice(vowe)
        syll = syll + random.choice(cons)
        syll = syll + random.choice(vowe)
        return syll

    elif struktura_now == ["CCV"]:
        syll = syll + random.choice(cons)
        syll = syll + random.choice(cons)
        syll = syll + random.choice(vowe)
        return syll
    
    elif struktura_now == ["CVC"]:
        syll = syll + random.choice(cons)
        syll = syll + random.choice(vowe)
        syll = syll + random.choice(cons)
        return syll
    
    elif struktura_now == ["CCVCC"]:
        syll = syll + random.choice(cons)
        syll = syll + random.choice(cons)
        syll = syll + random.choice(vowe)
        syll = syll + random.choice(cons)
        syll = syll + random.choice(cons)
        return syll




print(slabika())