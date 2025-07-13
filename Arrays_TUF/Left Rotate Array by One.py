from typing import List
class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range (1, len(nums)):
            if nums[i] > nums[i - 1]:
                pass
            
            else :
                break
        for j in range(i + 1, len(nums)):
            if (nums[j] - nums[j - 1]) > 1 :
                return False
        return True
        
        