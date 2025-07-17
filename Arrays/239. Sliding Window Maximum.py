from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        d = 3
        p = 0
        for i in range(0,len(nums) - 2):
            arr = nums[p:d]
            arr.sort()
            d += 1
            p += 1
            result.append(arr[-1])
        return result
            
        
        

        