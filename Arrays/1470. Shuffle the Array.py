from typing import List
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        p = nums[n]
        new = []
        
        for i in range(n):
            new.append(nums[i])
            new.append(nums[p])
            p += 1
            
        return new