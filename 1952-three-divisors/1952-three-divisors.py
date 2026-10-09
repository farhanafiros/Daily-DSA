class Solution:
    def isThree(self, n: int) -> bool:
        count =0
        for i in range(1,1+n):
            if n % i==0:
                count += 1
        return count==3
