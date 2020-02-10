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
    if fuel in HM and step_n >= HM[fuel]:
        return float('inf')

    if fuel not in HM:
        HM[fuel] = min(step_n, HM.get(fuel,float('inf')))
    
    if fuel in HM and step_n < HM[fuel]:
        HM[fuel] = step_n

    if fuel==1: 
        solution = step_n
    elif fuel % 2 == 1:
        solution = min(process_fuel(fuel+1, step_n+1, HM), process_fuel(fuel-1, step_n+1, HM))
    elif fuel % 2 == 0:
        solution = process_fuel(fuel//2, step_n+1, HM)
    else:
        raise RuntimeError("Unexpected behaviour in process_fuel")
    return solution


def go_down(n):

    i1, i2 = 1, 0
    while i1<n:
        i2 = i1
        i1 *= 2
    return i1-n+1 >= n-i2

    if n%2==0:
        n = n//2

def iteration_mike(n):

    if n%2==0:
        return n//2
    if go_down(n):
        return n-1
    else:
        return n+1

def solution_mike(n):
    i = 0
    n = int(n)
    while n>1:
        n = iteration_mike(n)
        i+=1
    return i

def answer_random_dude(n):
  n = int(n)
  steps = 0
  
  while n > 1:
    # if n is even, divide by 2 using bit manipulation
    if n & 1 == 0:
      n >>= 1
    else:
      # Use bit manipulation to create as many 0 from LSB as possible
        if (n == 3 or n % 4 == 1):
            n = n - 1
        else:
            n = n + 1

      #n = (n - 1) if (n == 3 or n % 4 == 1) else (n + 1)

    steps += 1
  return steps

def solution(n):
    HM = {}
    
    # DFS solution begin
    Q = deque()
    state = namedtuple('state','n depth')
    Q.append(state(int(n), 0))
    candidate_depth = float('inf')
    counter = 0
    while Q:
        s = Q.pop()

        # Kill branch early if there is no improvement
        if s.n in HM and s.depth >= HM[s.n]:
            continue
        
        # First time seen this number, update hash table
        if s.n not in HM:
            HM[s.n] = s.depth

        # We found a better number of steps to reach this number
        if s.n in HM and s.depth < HM[s.n]:
            HM[s.n] = s.depth
        
        # 0 Edge case
        if s.n==0:
            continue
        
        if s.n==1:
            candidate_depth = min(candidate_depth, s.depth)

        elif s.n % 2 == 1: # Odd
            Q.append(state(s.n-1, s.depth+1))
            Q.append(state(s.n+1, s.depth+1))
        
        elif s.n % 2 == 0: # Even
            Q.append(state(s.n//2, s.depth+1))
    
    return candidate_depth
    # DFS solution end

    return process_fuel(int(n), 0, HM) # Recursive solution

print(solution('4'))
print(solution('17'))
print(solution('300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000'))

print(solution_mike('4'))
print(solution_mike('17'))
print(solution_mike('300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000'))

#for i in range(1,100):
i = 300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000300000000000000000000000000000
print("{}: {} - {} - {}".format(i, solution(str(i)), solution_mike(str(i)), answer_random_dude(str(i))))












