def search1 (lis, num):
    if num in lis:
        print ('The number is in the list')
        
def binary_search (lis, num):
    newlist = []
    if num == lis[int(len(lis)/2)]:
        print ('The number is in the list')
    elif num > lis[int(len(lis)/2)]:
        for i in range (int(len(lis)/2), len(lis)):
            newlist.append(lis [i])
    else:
        for i in range (int(len(lis)/2)):
            newlist.append(lis[i])
    if len(newlist) > 0 and num < lis [len(lis) -1]:
        binary_search(newlist, num)
    else:
        print ('The number is not in the list')
    
list1 = [1, 5, 16, 20, 56, 100, 267, 300]
number = 2000

binary_search(list1, number)

#search1(list1, number)

