from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        maxi = nums[0]
        for i in range(1,len(nums)):
            if nums[i] < nums[i - 1]:
                maxi = nums[i]
                count += 1
        
        if count == 2:
            return maxi
        else:
            return nums[i]
        
        
  
        