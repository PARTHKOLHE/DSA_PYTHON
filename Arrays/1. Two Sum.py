from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
## Brute force 
        # for i in range(len(nums)):
        #     n = nums[i]
            
        #     for j in range(i+1, len(nums)):
        #         w = nums[j]
        #         if n + w == target:
        #             return [i,j]
                
## Optimal
        prevArr={}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in prevArr:
                return [prevArr[diff],i]
            prevArr[i] = n
        return 
            
            
            
        
        