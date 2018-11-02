import random
alphabet_cap = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
alphabet_small = ['a', 'b', 'c', 'd', 'e']
symbols = ['?', '!', '@', '&']


def random_number ():
    pas = ""
    for i in range (4):
        pas += str(random.randint(0,9))
    return pas

def random_letters_cap():
    pas = ""
    for i in range (3):
        pas += str(random.choice(alphabet_cap))
    return pas

def random_letters_small():
    pas = ""
    for i in range (3):
        pas += str(random.choice(alphabet_small))
    return pas

def random_symbols ():
    pas = ""
    for i in range (1):
        pas += str(random.choice(symbols))
    return pas

def strong_password ():
    password = random_number() + random_letters_cap() + random_letters_small() +random_symbols()
    p = list(password)
    random.shuffle(p)
    p = ''.join(p)
    return p

def weak_password ():
    list_of_passwords = {
        "1": "god",
        "2": "sex",
        "3": "love"
    }
    for keys,values in list_of_passwords.items():
        print(keys, values)
    n = input ("Please, choose your password: ")
    print ("Your password is: ",list_of_passwords[str(n)])

flag = input ("Do you want strong or weak password? :")
if flag == 'strong':
    print ("Your password is: ", strong_password())
else:
    weak_password()
