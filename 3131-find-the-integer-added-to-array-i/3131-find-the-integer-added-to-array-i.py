class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(len(nums1)):
            for j in range(len(nums1) - i - 1):
                if nums1[j] > nums1[j + 1]:
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]

                if nums2[j] > nums2[j + 1]:
                    nums2[j], nums2[j + 1] = nums2[j + 1], nums2[j]

        return nums2[0] - nums1[0]
