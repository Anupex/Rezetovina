from unidecode import unidecode
import string
import random


def id_generator():

    seznam_id = []

    file_vstup = open("vstup.txt", "r")
    for vstup in file_vstup:
        jmeno = vstup.strip('\n').split()
        id_split = jmeno[1].lower() + '.' + jmeno[0][:2].lower()
        seznam_id.append(id_split)
    
    #print(seznam_id)
    file_vstup.close()
    return seznam_id

id_generator()