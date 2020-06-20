'''
A program that finds the first missing positive integer in linear time and constant space.

@param arr: a list of integers.
@returns: the smallest positive integer that does not exist in the list.
'''
# returns 2
MY_LIST = [3, 4, -1, 1]

# returns 3
ARR = [1, 2, 0]

def lowest_positive(arr):
    '''Set() to remove duplicate and reduce memory usage.'''
    a_set = sorted(set(arr))
    new_arr = [index for index, _ in enumerate(a_set, 1) if index not in a_set][0]
    
    return print(new_arr)

lowest_positive(MY_LIST)
lowest_positive(ARR)
lowest_positive([0, -1, -3, -3, -3, -1])
