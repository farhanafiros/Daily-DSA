class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            lower_word = word.lower()

            for row in rows:
                if all(char in row for char in lower_word):
                    result.append(word)
                    break

        return result