class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
        answer = prefix[n - 1]
        for i in range(n - 2, 0, -1):
            answer = max(answer, prefix[i] - answer)
        return answer