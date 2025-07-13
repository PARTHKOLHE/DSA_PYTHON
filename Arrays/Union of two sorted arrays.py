class Solution:
    def unionArray(self, nums1, nums2):
        arr1 = []
        arr2 = []
        for i in range(len(nums1)):
            for j in range(i + 1 , len(nums1)):
                if nums1[i] != nums1[j]:
                    arr2[i] = nums1[i]    
                