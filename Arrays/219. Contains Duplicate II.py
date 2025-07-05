from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range (len(nums)):
            end = min(i + k,len(nums) - 1)
            for j in range (i + 1, end + 1):
                if nums[i] == nums[j]:
                    return True
            return False
                
        