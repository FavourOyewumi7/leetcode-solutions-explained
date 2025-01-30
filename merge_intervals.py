"""
thought process:
1. sort the intervals by the start time
2. initialize the result list and the initial and final variables
3. iterate through the intervals
4. if the current interval's start time is greater than the final time, add the current interval to the result list and update the initial and final variables
5. otherwise, update the final variable to the maximum of the current final time and the current interval's end time
6. add the last interval to the result list
7. return the result list
"""

class Solution:
    def merge(self, intervals):

        intervals.sort(key = lambda x:x[0])
        res = []
        init, final = intervals[0][0], intervals[0][1]
        
        for i in range(1, len(intervals)):

            if intervals[i][0] > final:
                res.append([init, final])
                init = intervals[i][0]
                final = intervals[i][1]
            else:
                final = max(final, intervals[i][1])
            
            
        res.append([init, final])
                
        return res
