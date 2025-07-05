from typing import List
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        leftsum = [0]
        righsum = [0]
        answer = []
        for i in range(len(nums) - 1):
            sum1 = nums[i] + leftsum[i]
            leftsum.append(sum1)
            
        for i in range(len(nums) -1,0,-1):
            sum2 = nums[i] + righsum[0]
            righsum.insert(0,sum2)
            
        for i in range (len(nums)):
            diff = abs(leftsum[i] - righsum[i])
            answer.append(diff)
        
        
        return answer
            

