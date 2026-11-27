class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        for i in range(len(nums1)):
            for j in range(i + 1, len(nums1)):
                if nums1[i] > nums1[j]:
                    nums1[i], nums1[j] = nums1[j], nums1[i]

                if nums2[i] > nums2[j]:
                    nums2[i], nums2[j] = nums2[j], nums2[i]

        return nums2[0] - nums1[0]
