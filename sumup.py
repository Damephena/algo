'''
A program that returns any two numbers from a list which adds up to a target.

@params arr: a list
@params target_value: an integer
@returns: a boolean. True returns a tuple with result.
'''
from itertools import permutations

def find_sum(arr, target_value):
    '''Using permutations. Loops through the list only once'''
    result = [numbers for numbers in permutations(arr, 2) if sum(numbers) == target_value]
    return False if not result else (True, result)

def find_sum2(arr, target_value):
    '''Using range. Loops through list twice. Returns unique value if True.'''
    result = []
    for first_number in arr:
        for i in range(len(arr) - 1):
            if first_number + arr[i + 1] == target_value:
                result.append((first_number, arr[i + 1]))
    return False if not result else (True, result)

def find_sum3(arr, target_value):
    '''Using enumerate. Loops through list twice.'''
    result = []
    for first_number in arr:
        for _, last_number in enumerate(arr):
            if first_number + last_number == target_value:
                result.append((first_number, last_number))
    if not result:
        return False
    return True, result

print(find_sum([10, 15, 3, 7], 17))
