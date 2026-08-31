class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_value= []
        maximum =max(nums)
        minimum =min(nums)
        for num in range(minimum,maximum+1):
            if num not in nums:
                missing_value.append(num)
        return missing_value