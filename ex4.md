Exercise 4

1. Describe the algorithm you will use to find the room. 
Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan.
    I will start by following the EY 100-130 sign to the left, checking every door number on the way until i get to EY128.

2. How many ”steps” it will take to find room EY128? And what is a “step” in this case?
    If we consider a step to be a door's number being checked, it will take 15 steps including EY128, since it is the 15th door when starting from the left.

3. Is this a best-case scenario, worst-case scenario, or neither?
    This is neither a best or worst case scenario, since we do not know exactly where EY128 is (best-case; 1 step), but we also did not have to check every room before finding EY128 (worst-case; 20 steps).

4. With this particular sign and floor layout, explain what a worst-case or best-case scenario would look like.
    Best-case scenario would be finding EY128 immediately (1 step).
    Worst-case would be checking every room on the floor before finding EY128 (20 steps).

5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient?
    Starting at the right end of the loop decreases walking time and leads us to EY128 quicker (Or, if we are assuming we still dont know exactly where EY128 is, starting at the right will take us less steps (only 6) to find it).