class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictniory = {}
        for num in nums:
            if num in dictniory:
                dictniory[num] += 1
            else:
                 dictniory[num] = 1 
        keys = list(dictniory.keys())
        keys.sort(
            key=dictniory.get,
            reverse=True
        )
        return keys[:k]

        