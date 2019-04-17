def mySqrt(x):
    if x == 0:
        return 0
    
    left, right = 0, x
    while left <= right:
        mid = (left + right) // 2
        if mid**2 == x:
            return mid
        elif mid**2 < x:
            left = mid + 1
        else:
            mid_last = mid
            right = mid - 1

    # End Condition: left > right
    return left-1
