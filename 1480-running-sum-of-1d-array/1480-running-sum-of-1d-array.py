class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        result=[]
        total =0
        for num in nums:
            total += num
            result.append(total)

        return result