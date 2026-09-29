class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            if s.count(char) == 1:
                return s.index(char)
        return -1