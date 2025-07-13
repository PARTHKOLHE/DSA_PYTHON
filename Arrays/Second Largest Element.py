#Input: nums = [8, 8, 7, 6, 5]
#              
#Output: 7
class Solution:
    def secondLargestElement(self, nums):
        if len(nums) < 1:
            return -1 
        L = float('-inf')
        l = float('-inf')
        
        for i in range (len(nums)):
            if nums[i] > L:
                l = L
                L = nums[i]
                
            elif nums[i] > l and nums[i] != L:
                l = nums[i]
                
        return l if l != float('-inf') else -1
            
            