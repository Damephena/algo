'''
A program that moves all 0s to the end of list.
Maintains the relative order of non-zero elements.

@param arr: a list of integers.
@returns: a list of initial array with 0's at the list's end.
'''

from collections import Counter

def move_zeroes(arr):
    '''Returns an array with all zeros at the list's end.'''
    result = [number for number in arr if number != 0]
    for _ in range(Counter(arr)[0]):
        result.append(0)
    return result

# returns [1, 3, 12, 0, 0]
MY_LIST = [0, 1, 0, 3, 12]

# returns [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]
ARR = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]

print(move_zeroes(ARR))
print(move_zeroes(MY_LIST))
