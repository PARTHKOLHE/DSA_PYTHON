from  typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        max_count = 1
        store = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1  

            if count > max_count and count > len(nums) / 2:
                max_count = count
                store = nums[i]
        
        return store
