from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        new_nums = []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
               
                if start == nums[i - 1]:
                    new_nums.append(str(start))
                else:
                    new_nums.append(f"{start}->{nums[i - 1]}")
                start = nums[i]  

        
        if start == nums[-1]:
            new_nums.append(str(start))
        else:
            new_nums.append(f"{start}->{nums[-1]}")

        return new_nums
