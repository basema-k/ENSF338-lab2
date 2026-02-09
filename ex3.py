# 1. What is a profiler, and what does it do?
""" 
A profiler describes and anlyzes how a program uses its exection time, providing a deterministic profiling of the program.
In Python, the cProfile module runs a program or function and produces a report of where the execution time is allocated.
The output of the module includes the total number of functions calls, how many of the calls are non-recursive and how execution time is distributed.
"""
# 2. How does profiling differ from benchmarking?
"""
 Benchmarking is about determining the speed and overall peformance of a program compared with other programs or to a standard for a certain application/task.
Profiling, on the other hand focuses on constraints within a program and gives exact information of how a program spends its time.
"""

# 3. Use a profiler to measure the execution time of the program (skip function definitions)
import timeit
import cProfile

def sub_function(n):
#sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data
def third_function():
    # third function that calculates the square of the numbers from 0 to 999
    return [i**2 for i in range(100000000)]

cProfile.run("test_function()")
cProfile.run("third_function()")

# 4. Discuss a sample output. Where does execution time go?
""" 
test_function(): 69 function calls with 24 being primitive calls in 0.000 seconds.
The table tells us sub_function() is called multiple times because of recursion (55 times total, 10 of those being primitive) and append() is called 10 times
test_function is only called once
Despite the multiple instances of function calls, totime and cumtime are 0.000 and so the total execution time is also 0 seconds.

third_function(): 4 function calls in 8.885 seconds
third_function() was called only once but it resulted in most of the execution time (7.796 seconds)
The remaining time (1.089 seconds) is spent on running the module and profiler maintenance
"""

