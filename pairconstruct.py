'''
A program that returns the first and last values using Python closure.
@params pair: a function `cons(first_value, last_value)`
@returns: an object eg list, integer, tuple etc
'''

def cons(a, b):
    '''Closure that takes another function `f`'''
    def pair(f):
        return f(a, b)
    return pair

def pair_values(first, last):
    '''Callable function passed into `pair()` in `cons()` closure.'''
    return first, last

def car(pair):
    '''Returns first value of `cons()` closure.'''
    print(pair(pair_values)[0])

def cdr(pair):
    '''Returns last value of `cons()` closure.'''
    print(pair(pair_values)[1])

car(cons(3, 4))
car(cons('Backend', 'Dev'))
cdr(cons(3, 4))
cdr(cons([45], 'Twitter Handle'))
