class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
       result =[] 
       for i in range(len(nums)):
            left = sum(nums[:i])
            right = sum(nums[i+1:])
            result.append(abs(left - right))

       return result
