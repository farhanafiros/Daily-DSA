class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_value=[]
        small_value=min(nums)
        large_value=max(nums)
        for num in range(small_value,large_value + 1):
            if num not in nums:
                missing_value.append(num)
        return missing_value