from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        max_count = 0
        for i in range(1 ,len(nums)):
            if nums[i -1] + 1 == nums[i]:
                count += 1
            else:
                count = 1
            if max_count < count:
                max_count = count
        
        if max_count < count:
            max_count = count
        return max_count       
                
                
        