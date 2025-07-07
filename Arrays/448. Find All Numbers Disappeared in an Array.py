# Input: nums = [1,2,2,3,3,4.,7,8]
# Output: [5,6]

from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []

        for i in range(1, n + 1):  # loop from 1 to n
            found = False
            for j in range(n):  # check each number in the list
                if nums[j] == i:
                    found = True
                    break
            if  found == False:
                result.append(i)
        
        return result
                