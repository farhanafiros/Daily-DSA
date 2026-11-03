class Solution:
    def reverseWords(self, s: str) -> str:
        
        result = ""
        start = 0

        for i in range(len(s)):
            if s[i] == " ":
                result += s[start:i][::-1] + " "
                start = i + 1

        result += s[start:][::-1]

        return result