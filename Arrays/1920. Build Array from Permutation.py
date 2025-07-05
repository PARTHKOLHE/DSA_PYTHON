from typing import List
class Solution:  
    def buildArray(self, nums: List[int]) -> List[int]:
        start = []
        for i in range(len(nums)):
            numb = nums[nums[i]]
            start.append(numb)
        return start
 # optimal
#   return [nums[num] for num in nums]
    

        