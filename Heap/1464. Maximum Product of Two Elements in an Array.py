from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return None
        largest = float('-inf')
        second_largest = float('-inf')
        
        for i in range(len(nums)):
            if nums[i] > largest:
                largest = nums[i]
                second_largest = largest
            
            elif nums[i] > second_largest:
                second_largest = nums[i]

        if second_largest != float('-inf'):
            return (largest - 1) * (second_largest - 1)
        else:
            return (largest - 1) 
        
        