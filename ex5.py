# Exercise 5 

import random
import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

sizes = [1000, 2000, 4000, 8000, 16000, 32000]

def linear_model(n, a, b):
    return a * n + b

def log_model(n, a, b):
    return a * np.log2(n) + b

def linear_search(target, data):
    for x in data:
        if x == target:
            return True
    return False

def binary_search(target, data):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

def main():
    avg_lin_times = []

    for size in sizes:
        data = list(range(size))
        lin_times = []

        for _ in range(1000):       # Repeat 1000 times
            target = random.choice(data)
            t = timeit.timeit(lambda: linear_search(target, data), number=100)
             # get average of 100 iterations
            lin_times.append(t / 100)

        avg_lin_times.append(sum(lin_times) / len(lin_times))
        print(f"Linear search | n={size} | avg time={avg_lin_times[-1]:.10f}s")

    avg_bin_times = []

    for size in sizes:
        data = list(range(size))  # must stay sorted
        bin_times = []

        for _ in range(1000):
            target = random.choice(data)
            t = timeit.timeit(lambda: binary_search(target, data), number=100)
            bin_times.append(t / 100)

        avg_bin_times.append(sum(bin_times) / len(bin_times))
        print(f"Binary search   n={size}    avg time={avg_bin_times[-1]:.10f}s")

    sizes_np = np.array(sizes)
    lin_np = np.array(avg_lin_times)
    bin_np = np.array(avg_bin_times)

    params_lin, _ = curve_fit(linear_model, sizes_np, lin_np)
    a_lin, b_lin = params_lin

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes_np, lin_np, label="Measured times")
    plt.plot(
        sizes_np,
        linear_model(sizes_np, a_lin, b_lin),
        label=f"Fit: t(n) = {a_lin:.2e} n + {b_lin:.2e}",
        color="red"
    )
    plt.xlabel("List Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Linear Search Time Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()

    # binary search interpolation and plot
    params_bin, _ = curve_fit(log_model, sizes_np, bin_np)
    a_bin, b_bin = params_bin

    plt.figure(figsize=(10, 6))
    plt.scatter(sizes_np, bin_np, label="Measured times")
    plt.plot(
        sizes_np,
        log_model(sizes_np, a_bin, b_bin),
        label=f"Fit: t(n) = {a_bin:.2e} log2(n) + {b_bin:.2e}",
        color="red"
    )
    plt.xlabel("List Size (n)")
    plt.ylabel("Average Time (seconds)")
    plt.title("Binary Search Time Complexity")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()

"""
PART 4 Discuss the results. For each interpolating function, describe (1) the type of
function, and (2) the parameters of the function. Are the results what you
expected? Why?

Linear Search:
The interpolating function used for linear search is a linear function:
    t(n) = a*n + b
Here, n is the size of the list. The parameter a represents how much extra
time is added for each additional element in the list, and b represents
a constant amount of time that does not depend on the list size.

The measured running time increases roughly linearly as n increases, which
matches the expected O(n) time complexity. This makes sense because linear
search checks elements one by one until the target is found.

Binary Search:
The interpolating function used for binary search is a logarithmic function:
    t(n) = a*log2(n) + b
Binary search repeatedly divides the search space in half, so the number
of steps grows slowly as the list size increases.

The measured results show a much slower increase in running time compared
to linear search, which agrees with the theoretical O(log n) complexity.

Overall:
The experimental results match the theoretical time complexities for both
algorithms. Small differences are expected due to variations in Python and timing measurments. 
"""

