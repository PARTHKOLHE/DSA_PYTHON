from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
# not interview meathod:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return nums[i]
# interview meathod:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if fast == slow:
                break
        
            slow = nums[0]
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
                
            return slow        