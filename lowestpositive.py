'''
A program that finds the first missing positive integer in linear time and constant space.

@param arr: a list of integers.
@returns: the smallest positive integer that does not exist in the list.
'''
# returns 2
MY_LIST = [3, 4, -1, 1]

# returns 3
ARR = [1, 2, 0]

def low(arr):
    '''Using a counter to loop. '''
    a_set, count = sorted(set(arr)), 1
    new_arr = list()

    for _ in a_set:
        if count not in a_set:
            new_arr.append(count)
        count += 1
    return print(new_arr[0])

low(MY_LIST)
low(ARR)
low([0, -1, -3, -3, -3, -1])
