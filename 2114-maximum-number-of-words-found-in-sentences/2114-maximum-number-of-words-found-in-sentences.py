class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maximum=0 
        for sentences in sentences:
            words = sentences.split()
            count =len(words)
            if count > maximum:
                maximum = count
        return maximum