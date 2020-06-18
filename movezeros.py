'''
A program that moves all 0s to the end of list.
Maintains the relative order of non-zero elements.

@param arr: a list of integers.
@returns: a list of initial array with 0's at the list's end.
'''

from collections import Counter

def move_zeroes(arr):
    '''Returns a new array with all zeros at the list's end.'''
    result = [number for number in arr if number != 0]
    for _ in range(Counter(arr)[0]):
        result.append(0)
    return result

def zero(arr):
    '''Returns same array using in-place swap.'''
    count = 0
    for i, value in enumerate(arr):
        if value != 0:
            arr[i], arr[count] = arr[count], value
            count += 1
    return arr

# returns [1, 3, 12, 0, 0]
MY_LIST = [0, 1, 0, 3, 12]

# returns [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
ARR = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

print(zero(ARR))
print(MY_LIST)
print(move_zeroes(ARR))
