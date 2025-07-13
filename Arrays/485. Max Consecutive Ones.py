from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        final = 0
        count = 0
        for i in range(len(nums)):
            if nums[0] == 1:
                count += 1
                
            else:
                final = count
                count = 0
        return count