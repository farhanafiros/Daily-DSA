class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        # Convert each list to a set to remove duplicates
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        
        # Find numbers that appear in at least two sets
        result = (s1 & s2) | (s2 & s3) | (s1 & s3)
        
        return list(result)
