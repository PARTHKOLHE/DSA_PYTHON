class Solution:
    def largestElement(self, nums):
        numb = nums[0]
        for i in range(1,len(nums)):
            if nums[i - 1] < nums[i]:
                numb = nums[i]
        return numb

        