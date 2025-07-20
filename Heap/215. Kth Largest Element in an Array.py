from typing import List
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        for i in range(len(nums) - 1, - 1, -1):
            if k > 0:
                k_value = nums[i]
                k -= 1
            else:
                return k_value