""" Re-ID
=====

There's some unrest in the minion ranks: minions with ID numbers like "1", "42", and other "good" numbers have been lording it over the 
poor minions who are stuck with more boring IDs. To quell the unrest, Commander Lambda has tasked you with reassigning everyone new, random IDs based on her Completely 
Foolproof Scheme. 

She's concatenated the prime numbers in a single long string: "2357111317192329...". Now every minion must draw a number from a hat. That number is the 
starting index in that string of primes, and the minion's new ID number will be the next five digits in the string. So if a minion draws "3", their ID number 
will be "71113". 

Help the Commander assign these IDs by writing a function solution(n) which takes in the starting index n of Lambda's string of all primes, and returns the next five 
digits in the string. Commander Lambda has a lot of minions, so the value of n will always be between 0 and 10000.

Languages
=========

To provide a Java solution, edit Solution.java
To provide a Python solution, edit solution.py

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Java cases -- 
Input:
Solution.solution(0)
Output:
    23571

Input:
Solution.solution(3)
Output:
    71113
    
"""
import itertools
def solution(n):
    assert 0 <= n <= 10000
    ''' Solution is a 5 digit number of the prime numbers string starting from n '''
    gp = gen_primes()
    primes_string = ''
    # Generate the string on the go to have at least the necessary n+5 digits 
    # (there is no need to calculate extra values)
    while len(primes_string) < n+5:
        primes_string += str(gp.next())
    return primes_string[n:n+5]


# Sieve of Eratosthenes algorithm is used to generate prime numbers.
# Adapted from http://code.activestate.com/recipes/117119/
def gen_primes():
    '''Return a generators of prime numbers. 
    Call .next() to get the next prime number starting from 2'''
    yield 2
    D = {}
    # The running integer that's checked for primeness. 
    # Check odd numbers starting from 3.
    q = 3
    for q in itertools.islice(itertools.count(3), 0, None, 2):
        p = D.pop(q, None)
        if p:
            x = q + 2*p
            while x in D: x += 2*p
            D[x] = p
        else:
            D[q*q] = q
            yield q

if __name__ == "__main__":
    x = solution(3)
    print x == '71113'
    x = solution(0)
    print x == '23571'
