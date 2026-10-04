class Solution:
    def checkValidString(self, s: str) -> bool:
        low = high = 0

        for ch in s:
            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1      # treat '*' as ')'
                high += 1     # treat '*' as '('

            # Minimum unmatched '(' can't be negative
            low = max(low, 0)

            # Even the best case has too many ')'
            if high < 0:
                return False

        return low == 0