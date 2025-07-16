from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count_1 = 0
        count_2 = 0
        count_0 = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_0 += 1
            elif nums[i] == 1:
                count_1 += 1
            else:
                count_2 += 1

        i = 0
        while count_0 != 0:
            nums[i] = 0
            i += 1
            count_0 -= 1
        while count_1 != 0:
            nums[i] = 1
            i += 1
            count_1 -= 1

        while count_2 != 0:
            nums[i] = 2
            i += 1
            count_2 -= 1
