# 2.1

***1 - Mention at least two aspects that make interpolation search better than binary search.*** 

- Binary search is very rigid, always checking the middle element, whereas interpolation search is more dynamic with its ability to go to different locations according to the values at certains positions.
- When the data is uniformly distributed, interpolation search has a better average time complexity than binary search

These reasons contribute to  making interpolation search more efficient then binary search.

***2 - Interpolation search assumes that data is uniformly distributed. What happens this data follows a different distribution? Will the performance be affected? Why?***

Interpolation search assumes that values are uniformly distributes so it can accurately predict where a certain value may be located. If the data follows a different distribution, like being concentrated in one area, the search's estimated position will be further from than the actual location compared to if the values were uniformly distributed. This leads to less accurate subsections, more iterations and worse performance.


***3 - If we wanted to modify interpolation search to follow a different distribution, which part of the code would be affected?***

The line:
pos = low + int(((float(high - low) / (arr[high] - arr[low])) * (x - arr[low])))
will be affected when modifying for a different distrbution.

This line estimates where x should be located, based on the assumption that the values are uniformly distributed. If the distribution is different, the formula is no longer accurate.


# 2.2

*When comparing linear, binary and interpolation search:*

***4 - When is linear search your only option for searching data as binary and interpolation search may fail?***

When data is unsorted, linear search is your only option. Binary and interpolation search both require the data to be sorted but linear search does not. 

***5 - In which case will linear search outperform both binary and interpolation search, and why>***

Linear search will outperform binary and interpolation search if the set of data is very small, or if the element the search is working to find -- which we can call x --  is near the beginning of the list. This can be explained by looking at the steps of the linear search algorithm: begin at index 0, compare the element to x, stop if it matches otherwise move to the next index. If x is near the beginning of the list, linear search can iterate through and find it quickly, and if the list itself is small, the algorithm can cycle through its entirety quickly, both options without the complexity of binary or interpolation search. Of course, as we mentioned before, linear search will also outperform the other two options when the data is unsorted.

***6 - Is there a way to improve binary and interpolation search to solve this issue?***

Yes, optimizations to binary and interpolation search can be applied to improve them in these scenarios. A lower-limit on size can be applied, meaning binary or interpolation search will only be used on arrays of sizes large enough to justify it.




