from random import randint

def list_of_numbers(num):
    return list(str(num))

def users_number(num):
    while (num > 9999) or (num < 1000):
        num = int(input("Give me a 4-digit number: "))
        if (num > 9999) or (num < 1000):
            print ("It's not 4-digit number. Please, try again.")
    return num

def count_cows_bulls (list1, list2):
    c = 0
    b = 0
    for i in range(4):
        if (list1[i] == list2[i]):
            c += 1
        elif (list1[i] != list2[i]) and (list2[i] in list1):
            b += 1
    return c, b

if __name__=="__main__":
    number = randint(1000,9999)
    list_of_num = list_of_numbers(number)
    attempts = 0
    cows = 0
    print (number)
    
    
    while cows != 4:
        user_num = 0
        user_num = users_number(user_num)  
        list_of_user_num = list_of_numbers(user_num)
        cows, bulls = count_cows_bulls (list_of_num, list_of_user_num)
        print ('Cows:', cows)
        print ('Bulls:', bulls)
        attempts +=1
        
    print ("You've guessed the number! You had {} attempts".format(attempts))
    
    
