class Solution:
    def linearSearch(self, nums, target):
        val = -1
        for i in range (len(nums)):
            if nums [i] == target:
                val = i
                break
        return val