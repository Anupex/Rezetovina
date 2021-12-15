from unidecode import unidecode
import random
import string

def pwd_generator():

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits

    all = lower + upper + num
    temp = random.sample(all, 5)
    password = ''.join(temp)
    return password


def id_generator():

    seznam_id = []

    file_vstup = open("vstup.txt", "r+", encoding='utf-8')

    for vstup in file_vstup:
        jmeno = vstup.strip('\n').split()
        id_split = jmeno[1].lower() + '.' + jmeno[0][:2].lower()
        seznam_id.append(id_split)

    for i in range(len(seznam_id)):
       seznam_id[i] = unidecode(seznam_id[i])
    
    
    file_vstup.close()
    return seznam_id


def id_pwd_comb():
    file1 = open('data.txt', 'a+')

    for i in id_generator():
        print('id: ' + i + ' pwd: ' + pwd_generator() + '\n')
        file1.write('id: ' + i + ' pwd: ' + pwd_generator() + '\n')

    file1.close


id_pwd_comb()
