class Solution:
    def maxProduct(self, n: int) -> int:
          digits = list(map(int, str(n)))
          digits.sort()
          return digits[-1] * digits[-2]