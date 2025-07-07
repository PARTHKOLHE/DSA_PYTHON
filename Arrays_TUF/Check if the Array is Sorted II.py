class Solution:
    def isSorted(self, nums):
        for i in range (1,len(nums)):
            if nums[i - 1] > nums[i]:
                return False
        return True
                
                