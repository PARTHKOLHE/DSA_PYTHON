from typing import List
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        result = []
        neg_count = 0
        pos_count = 0
        for num in nums:
            if num < 0:
                neg.append(num)
                
            else:
                pos.append(num)
        for i in range(len(nums)):
            if i % 2 != 0:
                result.append(pos[pos_count])
                pos_count += 1
            else:
                result.append(neg[neg_count])
                neg_count += 1
        return result