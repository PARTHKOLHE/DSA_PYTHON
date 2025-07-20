from typing import List
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        max_num = 0
        sum_val = 0
        for i in range(len(grid)):
            grid[i].sort()
        
        for j in range(len(grid[0])):
            for a in range(len(grid)):
                max_num = max(grid[a][-1],max_num)
                grid.remove(grid[a][-1])
            sum_val = sum_val + max_num
            
        return sum_val    