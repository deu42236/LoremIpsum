#bican_kvant-anal-slab-v-ces-lex.pdf
#3 slabiky na slovo

#program dává počet slabik do jednoho slova

import random
abc = "abcdefghijklmnopqrstuvyz"
souhlasky = "hkrdtnňžščjďťňbflmpsvz"
m_souhl =  "žšcčřjďťň"
m_samoh = "aeiou"
t_souhl = "hkrdtn"
t_samoh = "aeyou"
o_souhl = "bflmpsvz"
o_samoh = "aeiouy"
hacek_samoh = "ňžščďť"
hacek_souhlasky = "aou"
slabika_typy = ["CV", "CVC","CCV", "CCVC"] 
slabika = ""
CC = ["l", "r", "s", "k"] #kdyz jsou 2 samohlasky, ta druha je jedna z techto
choice = [m_samoh, t_samoh, o_samoh]
characters = 10
slovo_slabik = random.choices([1,2,3,4,5,], weights=(3, 20, 40, 30, 25))
## C = souhlaska
## V = samohlaska
slabika_now = random.choices(slabika_typy, weights=(48, 18, 17, 5))         #pravděpodobnost slabik
print(slabika_now)

for _ in range(slovo_slabik[0]):
    if slabika_now == ["CV"]:                               
        slabika = slabika + random.choice(souhlasky)
        if  slabika in hacek_souhlasky:
            slabika = slabika + random.choice(hacek_samoh)      
        elif slabika in m_souhl:
            slabika = slabika + random.choice(m_samoh)
        elif slabika in t_souhl:
            slabika = slabika + random.choice(t_samoh)
        elif slabika in o_souhl:
            slabika = slabika + random.choice(o_samoh)


    elif slabika_now == ["CVC"]:
        slabika = slabika + random.choice(souhlasky)        
        if  slabika in hacek_souhlasky:
            slabika = slabika + random.choice(hacek_samoh)      
        elif slabika in m_souhl:
            slabika = slabika + random.choice(m_samoh)
        elif slabika in t_souhl:
            slabika = slabika + random.choice(t_samoh)
        elif slabika in o_souhl:
            slabika = slabika + random.choice(o_samoh)
        slabika = slabika + random.choice(souhlasky)        

    elif slabika_now == ["CCV"]:
        slabika = slabika + random.choice(souhlasky)
        slabika = slabika + random.choice(CC)
        if  slabika in hacek_souhlasky:
            slabika = slabika + random.choice(hacek_samoh)      
        elif slabika[-1] in m_souhl:
            slabika = slabika + random.choice(m_samoh)
        elif slabika[-1] in t_souhl:
            slabika = slabika + random.choice(t_samoh)
        elif slabika[-1] in o_souhl:
            slabika = slabika + random.choice(o_samoh)


    elif slabika_now == ["CCVC"]:    
        slabika = slabika + random.choice(souhlasky)
        slabika = slabika + random.choice(CC)
        if  slabika in hacek_souhlasky:
            slabika = slabika + random.choice(hacek_samoh)
        elif slabika[-1] in m_souhl:
            slabika = slabika + random.choice(m_samoh)
        elif slabika[-1] in t_souhl:
            slabika = slabika + random.choice(t_samoh)
        elif slabika[-1] in o_souhl:
            slabika = slabika + random.choice(o_samoh)
        slabika = slabika + random.choice(souhlasky)
    
print(slabika)


