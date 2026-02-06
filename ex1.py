# Exercise 1

def original_func(n):
    if n <= 1:
        return n
    else:
        return original_func(n-1) + original_func(n-2)

'''
1. What does this code do?
    This code computes the nth Fibonacci number using recursion.

2. Is this an example of a divide-and-conquer algorithm?
    Yes, this is an example of a divide-and-conquer algorithm 
    because it breaks the problem into smaller subproblems 
    (using recursion to calculate the Fibonacci numbers 
    of n-1 and n-2 seperately and combining the results).

3. Give an expression for the time complexity of this code.
    The time complexity of this code is O(2^n) since each call to func(n)
    results in two more calls (func(n-1) and func(n-2)), 
    This means there is exponential growth in the number of calls as n increases.

4. Implement a version of this code which uses memoization to improve performance.
'''

def optimized_func(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = optimized_func(n-1, memo) + optimized_func(n-2, memo)
    return memo[n]

'''
5. Give an expression for the time complexity of the optimized algorithm.
    The time complexity of the optimized algorithm is O(n) 
    because each Fibonacci number is computed only once and 
    stored in memo, therefore there are at most n unique subproblems.

6. Time the original code and your improved version for all integers 
    between 0 and 35, and plot the results.
'''

import time
import matplotlib.pyplot as plt
import numpy as np

original_times = []
optimized_times = []
memo = {}

for i in range(36):

    # original code
    start_time = time.time()
    original_func(i)
    original_times.append(time.time() - start_time)

    # optimized code
    start_time = time.time()
    optimized_func(i, memo)
    optimized_times.append(time.time() - start_time)

# plot original_func
plt.figure()
plt.plot(range(36), original_times, marker='o', color='purple')
plt.title('Original Function Times for increasing n')
plt.xlabel('n')
plt.ylabel('Time (sec)')
plt.savefig('ex1.6.1.jpg')
y_min, y_max = plt.ylim()    # ***
plt.close()

# plot optimized_func
# optimized graph y axis is set to match original graph to more easily see differences
# remove lines commented with *** to have optimized graph auto-scale y axis
plt.figure()
plt.plot(range(36), optimized_times, marker='o', color='red')
plt.title('Memoized Function Times for increasing n')
plt.xlabel('n')
plt.ylabel('Time (sec)')
plt.ylim(y_min, y_max)    # ***
plt.savefig('ex1.6.2.jpg')
plt.close()