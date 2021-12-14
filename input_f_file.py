from unidecode import unidecode
import string
import random


def id_generator():

    seznam_jmen = []

    file_vstup = open("vstup.txt", "r")
    for vstup in file_vstup:
        jmeno = vstup.strip('\n')
        seznam_jmen.append(jmeno)

    for jmeno in seznam_jmen:
        pass


    print(seznam_jmen)
    file_vstup.close()
    #jmeno_prijmeni = str(unidecode(input('zadej jmeno a prijmeni: '))).lower()
    #rozdeleno = jmeno_prijmeni.split()
    #id = rozdeleno[1] + '.' + rozdeleno[0][:2]
    #return id

id_generator()