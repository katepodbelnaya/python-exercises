def guess(num):
    mynum = 6
    if num == mynum:
        return 0
    elif num < mynum:
        return 1
    else:
        return -1
        
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guessNumber(n):
    """
    :type n: int
    :rtype: int
    """
    if n == 1:
        return 1
    
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if guess(mid) == 0:
            return mid
        elif guess(mid) == 1:
            left = mid + 1
        else:
            right = mid - 1
            
