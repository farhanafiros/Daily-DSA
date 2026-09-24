class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = max(nums)
        index = nums.index(largest)

        for num in nums:
            if num != largest and largest < 2 * num:
                return -1

        return index