from typing import List

class Solution:
    def rotateArrayByOne(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums 
        first = nums[0]
        for i in range (1, len(nums)):
            nums[i - 1] = nums[i]
            
        nums[len(nums) - 1] = first
        return nums
