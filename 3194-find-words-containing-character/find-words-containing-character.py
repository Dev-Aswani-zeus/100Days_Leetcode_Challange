class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        arr = []
        for i in range(len(words)):
            for ch in words[i]:
                if ch == x:
                    arr.append(i)
                    break
        
        return arr
        