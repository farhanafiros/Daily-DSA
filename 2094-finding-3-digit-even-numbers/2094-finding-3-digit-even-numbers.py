class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        
        result = []

        for i in range(100, 1000):
            if i % 2 == 0:
                nums = list(map(int, str(i)))
                temp = digits.copy()

                for n in nums:
                    if n in temp:
                        temp.remove(n)
                    else:
                        break
                else:
                    result.append(i)

        return result
