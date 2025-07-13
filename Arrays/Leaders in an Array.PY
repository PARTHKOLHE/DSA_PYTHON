class Solution:
    def leaders(self, nums):
        n = len(nums)
        result = [] 
        for i in range(1, n):
            if nums[i - 1] > nums[i]:
                for j in range(i ,n):
                    val = max(nums[i - 1],nums[j])
                if val == nums[i - 1]:
                    result.append(nums[i - 1])
                
        result.append(nums[-1])
        return result             
                    
            