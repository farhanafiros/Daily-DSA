class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        result = []
        min_sum = float('inf')

        for i in range(len(list1)):
            if list1[i] in list2:
                total = i + list2.index(list1[i])

                if total < min_sum:
                    min_sum = total
                    result = [list1[i]]
                elif total == min_sum:
                    result.append(list1[i])

        return result
