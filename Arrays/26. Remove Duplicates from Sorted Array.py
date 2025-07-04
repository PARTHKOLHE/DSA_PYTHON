from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 1
        for i in range(len(nums)):
            if nums[i] != nums[i -1]:
                nums[write] = nums[i]
                write += 1
            
        return write
                    
            

            
                
        
        
        
        