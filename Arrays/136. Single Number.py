from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
# Brute force:
#         nums.sort()
#         if len(nums) == 1:
#             return nums[0]
#         i = 0
#         while i < len(nums) - 1:
#             if nums[i] != nums[i + 1]:
#                 return nums[i]
#             i += 2

#         return nums[-1]

# optimal:
        result = 0
        for num in nums:
            result ^= num
        return result