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

# pwd_generator()
def id_generator():

    jmeno_prijmeni = str(unidecode(input('zadej jmeno a prijmeni: '))).lower()
    rozdeleno = jmeno_prijmeni.split()
    id = rozdeleno[1] + '.' + rozdeleno[0][:2]
    return id

# id_generator()

def id_pwd():

    file1 = open('data.txt', 'a+')
    file1.write('id: ' + id_generator() + ' pwd: ' + pwd_generator() + '\n')
    file1.close()
    
    
while str(input('zadat jmeno? (a/n): ')).lower() == 'a':
    id_pwd()
