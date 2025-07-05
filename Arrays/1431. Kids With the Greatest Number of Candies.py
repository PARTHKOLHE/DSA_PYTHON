from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
       nums = []
       for i in range(len(candies)):
        more = max(candies)
        
        for j in range (len(candies)):
            if candies[j] + extraCandies >= more:
                nums.append(True)
            else:
                nums.append(False)
        return nums