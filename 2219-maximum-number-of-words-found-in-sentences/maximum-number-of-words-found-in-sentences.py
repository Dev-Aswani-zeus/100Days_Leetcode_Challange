class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max = 0
        for i in range(len(sentences)):
            count = len(sentences[i].split())
            if count > max:
                max = count
        return max
        