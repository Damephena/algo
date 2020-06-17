'''
A program that returns any two numbers from a list which adds up to a target.

@params arr: a list
@params k: an integer
@returns: a boolean. True returns a tuple with result.
'''
from itertools import permutations
my_list = [10, 15, 3, 7]
k = 17

# using permutations to go through the list only once.
def find_sum(arr, k):
    result = [numbers for numbers in permutations(arr, 2) if sum(numbers) == k]
    return False if not result else (True, result)

# using range
def find_sum(arr, k):
    result = []
    for first_number in arr:
        for i in range(len(arr) - 1):
            if first_number + arr[i + 1] == k:
                result.append((first_number, arr[i + 1]))

    return False if not result else True

# using enumerate
def find_sum(arr, k):
    result = []
    for first_number in arr:
        for i, last_number in enumerate(arr, 1):
            if first_number + last_number == k:
                result.append((first_number, last_number))

    if not result:
        return False
    else:
        return True, result

print(find_sum(my_list, k))
