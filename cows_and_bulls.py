from random import randint

def list_of_numbers(num):
    return list(str(num))

def users_number(num):
    while (num > 9999) or (num < 1000):
        num = int(input("Give me a 4-digit number: "))
        if (num > 9999) or (num < 1000):
            print ("It's not 4-digit number. Please, try again.")
    return num

def count_cows (list1, list2):
    c = 0
    for i in range(4):
        if (list1[i] == list2[i]):
            c += 1
            list1[i] = 11
            list2[i] = 22
    return c

def count_bulls (list1, list2):
    b = 0
    for i in range(4):
        if list1[i] in list2:
            b += 1
    return b

if __name__=="__main__":
    number = randint(1000,9999)
    attempts = 0
    cows = 0
   # print (number)


    while cows != 4:
        user_num = 0
        user_num = users_number(user_num)
        list_of_user_num = list_of_numbers(user_num)
        list_of_num = list_of_numbers(number)
        cows = count_cows (list_of_num, list_of_user_num)
        bulls = count_bulls (list_of_num, list_of_user_num)
        print ('Cows:', cows)
        print (list_of_num, list_of_user_num)
        print ('Bulls:', bulls)
        attempts +=1

    print ("You've guessed the number! You had {} attempts".format(attempts))
