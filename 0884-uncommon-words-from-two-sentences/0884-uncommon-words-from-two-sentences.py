class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        words=s1.split() + s2.split()
        result = []
        for word in words:
            if words.count(word)==1:
                result.append(word)
        return result
