from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  
        intervals.sort()
        final = []
        result = intervals[0]
        i = 1
        while i < len(intervals):
            if result[1] >= intervals[i][0]:
                result[1] = max(intervals[i][1], result[1]) 
            else:
                final.append(result)
                result = intervals[i]
            i += 1
        final.append(result)
        return result
             
        
                
                
        