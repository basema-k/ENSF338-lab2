# 2.1

***1 - Mention at least two aspects that make interpolation search better than binary search.*** 

- Binary search is very rigid, always checking the middle element, whereas interpolation search is more dynamic with its ability to go to different locations according to the values at certains positions.
- Binary search is constrained to checking one at a time, while interpolation search can perform multiple checks.

These reasons an contribute to  making interpolation search more efficient and faster then binary search.

***2 - Interpolation search assumes that data is uniformly distributed. What happens this data follows a different distribution? Will the performance be affected? Why?***

Interpolation search works by narrowing the search space of an array to increasingly small subsets, until the position is found. 
For example, in an array with arr[0] = 0 and arr[9] = 20, if we're searching for x = 2, it makes sense to try arr[1] over a position at the end of the array. 
This entire concept is predicated on the assumption that arr[0] is the smallest number and arr[9] is the largest. If this assumption does not hold up, the process of narrowing down a potential location fails, or at least, slows down significantly.

If the dataset follows a different distribution

***3 - If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?***



# 2.2

*When comparing linear, binary and interpolation search:*

***4 - When is linear search your only option for searching data as binary and interpolation search may fail?***

