class Solution:
    def dominantIndex(self, nums):
        largest = max(nums)
        second = sorted(nums)[-2]

        if largest >= second * 2:
            return nums.index(largest)
        else:
            return -1