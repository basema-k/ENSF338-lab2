# Exercise 5

import random
import timeit
import matplotlib.pyplot as plt
import numpy as np

sizes = [1000, 2000, 4000, 8000, 16000, 32000]

def findinlist(n, l):
    for i in range(len(l)):
        if l[i] == n:
            return True
    return False

avg_lin_times = []

for size in sizes:

    data = list(range(size))
    lin_times = []
    for i in range(1000):    # Repeat 1000 times
        random.shuffle(data)
        linear_time = timeit.timeit("findinlist(13, data)", setup="from __main__ import findinlist, data", number=100)
        # get average of 100 iterations
        lin_times.append(linear_time/100)

    avg = sum(lin_times) / len(lin_times)    # avg of 1000 repetitions
    print(f"Size: {size}, Average Linear Search Time: {avg:.10f} seconds")
    
    avg_lin_times.append(avg)

# plot linear search times
slope, intercept = np.polyfit(listlengths, avgtimes, 1)
plt.scatter(listlengths, avgtimes)
linevalues = [slope * x + intercept for x in listlengths]
plt.plot(listlengths, linevalues, 'r')

# print equation of the line
print("The linear model is: t = %.2e * n + %.2e" % (slope, intercept))

def binary_search(n, l):
    low = 0
    high = len(l) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if l[mid] == n:
            return True
        elif l[mid] < n:
            low = mid + 1
        else:
            high = mid - 1
    return False

avg_bin_times = []

for size in sizes:
    data = list(range(size))
    bin_times = []
    
    for i in range(1000):    # Repeat 1000 times
        # cant shuffle for binary search? 
        binary_time = timeit.timeit("binary_search(size//2, data)", 
                                     setup="from __main__ import binary_search, data, size", 
                                     number=100)
        # get average of 100 iterations
        bin_times.append(binary_time/100)

    avg = sum(bin_times) / len(bin_times)    # avg of 1000 repetitions
    print(f"Size: {size}, Average Binary Search Time: {avg:.10f} seconds")
    
    avg_bin_times.append(avg)

# plot binary search times
plt.figure(figsize=(10, 6))
slope, intercept = np.polyfit(sizes, avg_bin_times, 1)
plt.scatter(sizes, avg_bin_times)
linevalues = [slope * x + intercept for x in sizes]
plt.plot(sizes, linevalues, 'r')

# Add labels and title
plt.xlabel("List Size (n)")
plt.ylabel("Average Time (seconds)")
plt.title("Binary Search Time Complexity")
plt.grid(True)

# STILL NEED PARTS 3 & 4 --------------------
