'''
A program that returns the product of list elements.

@param arr: a list of integers.
@returns: a new list such that each element at the index `i` of the new
list is the product of all the numbers in the original array except
the one at `i`.
'''
from math import prod
# returns [120, 60, 40, 30, 24]
ARR = [1, 2, 3, 4, 5]
#returns [2, 3, 6]
MY_LIST = [3, 2, 1]

def product_list(arr):
    '''Using slice and math.prod function.'''
    if len(arr) == 1:
        return print([arr[0]])
    if not arr:
        return print([])

    result = [prod(arr[:i] + arr[i+1:]) for i, _ in enumerate(arr)]
    return print(result)

def pro(arr):
    '''Creating a new copy of initial list to make changes.'''
    result = []
    if len(arr) == 1:
        return print([arr[0]])

    if not arr:
        return print([])

    for index, value in enumerate(arr):
        new_list = arr
        new_list[index] = 1

        multiplier = 1
        for number in new_list:
            multiplier *= number

        result.append(multiplier)
        # update the list to its inital value
        new_list[index] = value
    return print(result)

def product1(arr):
    '''Using division.'''
    if len(arr) == 1:
        return print([arr[0]])
    if not arr:
        return print([])

    result = [int(prod(arr) / number) for number in arr]
    return print(result)

product_list(MY_LIST)
product_list(ARR)
product_list([])
pro(MY_LIST)
pro(ARR)
pro([0])
product1(MY_LIST)
