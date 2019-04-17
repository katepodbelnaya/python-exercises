def binary_search (lis, num):
    
    st = 'The number is not in the list'
    
    if len(lis) == 0:
        print (st)

    left, right = 0, len(lis) - 1
    while left <= right:
        mid = (left + right) // 2
        if lis[mid] == num:
            st = 'The number is in the list'
            break
        elif lis[mid] < num:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    print (st)
    

    

list1 = [1, 5, 16, 20, 56, 100, 267, 300]

number = 9
