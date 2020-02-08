"""
Fuel Injection Perfection
=========================

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly. 

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time. 

The fuel control mechanisms have three operations: 

1) Add one fuel pellet
2) Remove one fuel pellet
3) Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets)

Write a function called solution(n) which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example:
solution(4) returns 2: 4 -> 2 -> 1
solution(15) returns 5: 15 -> 16 -> 8 -> 4 -> 2 -> 1

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit Solution.java

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution('15')
Output:
    5

Input:
solution.solution('4')
Output:
    2

-- Java cases --
Input:
Solution.solution('4')
Output:
    2

Input:
Solution.solution('15')
Output:
    5
    """
from collections import defaultdict, deque, namedtuple
# import sys
# sys.setrecursionlimit(10000)
def process_fuel(fuel, step_n, HM):

    # Optimization: kill branches early if I've already been here, and no improvement was found
    #if fuel in HM and step_n >= HM[fuel]:
        #return float('inf')
    if fuel not in HM:
        HM[fuel] = min(step_n, HM.get(fuel,float('inf')))

    if fuel==1: 
        solution = step_n
    elif fuel % 2 == 1:
        solution = min(process_fuel(fuel+1, step_n+1, HM), process_fuel(fuel-1, step_n+1, HM))
    elif fuel % 2 == 0:
        solution = process_fuel(fuel//2, step_n+1, HM)
    else:
        raise RuntimeError("Unexpected behaviour in process_fuel")
    return solution

def process_fuel_DFS(fuel, step_n, HM, Q):
    # Optimization: kill branches early if I've already been here, and no improvement was found
    if fuel in HM and step_n >= HM[fuel]:
        return float('inf')

    if fuel==1: 
        solution = step_n
    elif fuel % 2 == 1:
        solution = min(process_fuel(fuel+1, step_n+1, HM), process_fuel(fuel-1, step_n+1, HM))
    elif fuel % 2 == 0:
        solution = process_fuel(fuel//2, step_n+1, HM)
    else:
        raise RuntimeError("Unexpected behaviour in process_fuel")
    return solution

def solution(n):
    # The general case we have the 3 options, we could explore a tree with "what if" I did that (+1/-1 //2) and assuming that +1+1 and -1-1 does not improve the result (should be able to prove it).
    
    # If number is odd, branch +1 and -1, repeat, add depth
    # If number is even, divide by 2, repeat, add depth.
    # Recursive solution should do it
    # To reduce branches and speedup solution, could keep a dict/hashtable of number/steps so far, and discard branch if we are not improving
    HM = {}
    Q = deque()
    state = namedtuple('state','n depth')
    Q.append(state(int(n), 0))
    candidate_depth = float('inf')
    counter = 0
    while Q:
        s = Q.pop()
        counter+=1
        # print(s.n)
        if counter%10000==0:
            lq = len(Q)
            print("{}".format(lq))

        if s.n in HM and s.depth >= HM[s.n]:
            continue
        
        if s.n not in HM:
            HM[s.n] = s.depth

        if s.n==0:
            continue
        
        if s.n==1:
            candidate_depth = min(candidate_depth, s.depth)
            #print("{}".format(candidate_depth))

        elif s.n % 2 == 1: # Odd
            Q.append(state(s.n-1, s.depth+1))
            Q.append(state(s.n+1, s.depth+1))
        
        elif s.n % 2 == 0: # Even
            Q.append(state(s.n//2, s.depth+1))
    
    return candidate_depth
    #
    # return process_fuel(int(n), 0, HM)

print(solution('3000000000000000000000000'))
# print(solution('4'))
# print(solution('17'))












