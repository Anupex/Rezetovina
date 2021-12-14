from unidecode import unidecode
import random
import string


def id_generator():

    jmeno_prijmeni = str(unidecode(input('zadej jmeno a prijmeni: '))).lower()
    rozdeleno = jmeno_prijmeni.split()
    id = rozdeleno[1] + '.' + rozdeleno[0][:2]
    
    repeat = []
    if id not in repeat:
        repeat += id
        print(repeat)
        return id
    else:
        id = rozdeleno[1] + '.' + rozdeleno[0][:3]
        print(repeat)
        return id

id_generator()
