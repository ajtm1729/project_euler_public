'''pe.py module contains functions for solving Project Euler problems

This module contains functions I have written for solving some of the first 100
Project Euler problems.
'''

def digit_sum(n):
    '''
    Calculate the digit sum of n.
    '''

    answer = 0

    while n>0:
        answer += n%10
        n = n//10

    return(answer)

def divisors(n):
    '''
    Returns a list of the divisors of n.
    '''

    # I am loathe to write this function, as I think I already wrote one that
    # does exactly this and I will surely be able to find by looking on my old
    # laptop.

    # I think I will see if there is a standard function to use here, and come
    # back and fill this in later if I fancy it.

    # The next six lines were from an AI:

    divisors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return list(sorted(divisors))

def proper_divisor_sum(n):
    '''
    Returns the sum of the proper divisors of n.
    '''
    return sum(divisors(n))-n