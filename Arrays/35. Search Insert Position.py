from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
# # Brute force 
#         if nums[len(nums) - 1] < target:
#             return len(nums)
#         for i in range(len(nums)):
#             if target <= nums[i]:
#                 return i
# optimal O(logn)
     left = 0
     right = len(nums) - 1
     
     while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
     return left
        
        
        
             
  