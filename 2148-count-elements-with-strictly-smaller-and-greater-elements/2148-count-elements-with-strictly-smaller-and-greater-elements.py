class Solution:
    def countElements(self, nums: list[int]) -> int:
        return sum(min(nums) < x < max(nums) for x in nums)