from typing import List
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_val = 0
        for i in range(k):
            for j in range(k):
                if nums[j] < nums[min_val]:
                    min_val = j
                    nums[j] = nums[j] * multiplier
                    break
        return nums       