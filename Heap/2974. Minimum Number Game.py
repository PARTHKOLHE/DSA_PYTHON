from typing import List
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr = []
        for i in range(1,len(nums),2):
            arr.append(nums[i - 1])
            arr.append(nums[i])
        return arr