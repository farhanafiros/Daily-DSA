class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
         c = len(set(candyType))
         half = len(candyType) // 2

         if c < half:
            return c
         else:
            return half







