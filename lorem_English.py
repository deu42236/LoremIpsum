#https://www.sttmedia.com/characterfrequency-english

import random
#abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cons = ['q', 'w', 'r', 't', 'p', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'x', 'c', 'v', 'b', 'n', 'm', 'th', 'he', 'an', 'th', 'nd', 'ng', 'tt', 'll', 'rr'] #cons... souhlasky
cons_w = [9, 234, 568, 937, 166, 611, 414, 203, 192, 611, 23, 87, 424, 20, 273, 106, 154, 680, 253, 30, 30, 60, 399, 162, 99, 30, 43, 32]
vowe = ['a', 'e', 'i', 'o', 'u', 'y']                                                                                                                        #vowe... samohlasky
vowe_w = [834, 1260, 671, 770, 285, 304]
structure = ["CV", "CVCV","CCV", "CVC", "CCVCC"]        ## C = souhlaska, V = samohlaska
words_count = int(input("počet slov: "))
output = "Lorem english "
premade_words = ["yo", "wadup", "always", "bai", "kuk", "sakrss", "america can be described in 1 word: "]


structure_now = random.choices(structure)


def slabika():
    syll = ""
    if random.randint(0, 60) == 5:
        syll = random.choice(premade_words)
        return syll
    if structure_now == ["CV"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(vowe, weights = vowe_w, k=1)[0]
        return syll
    
    elif structure_now == ["CVCV"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(vowe, weights = vowe_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(vowe, weights = vowe_w, k=1)[0]
        return syll

    elif structure_now == ["CCV"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(vowe, weights = vowe_w, k=1)[0]
        return syll
    
    elif structure_now == ["CVC"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(vowe, weights = vowe_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        return syll
    
    elif structure_now == ["CCVCC"]:
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(vowe, weights = vowe_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        syll = syll + random.choices(cons, weights = cons_w, k=1)[0]
        return syll

for _ in range(words_count):                                                          #počet slov
    for i in range(random.randint(1, 3)):
        output = output + slabika()
    output = output + " "
print(output)