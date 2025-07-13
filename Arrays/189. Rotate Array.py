from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
# # brute force: 
#         for i in range(k):
#             last = nums[-1]
#             for j in range(len(nums) - 1, 0, -1):
#                 nums[j] = nums[j - 1]
#             nums[0] = last

# Optimal Solution:

        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])