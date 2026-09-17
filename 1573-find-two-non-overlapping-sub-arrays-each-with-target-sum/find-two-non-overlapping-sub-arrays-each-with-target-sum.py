class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        INF = float('inf')
        best = [INF] * (n + 1)
        left = 0
        total = 0
        answer = INF
        for right in range(n):
            total += arr[right]
            while total > target:
                total -= arr[left]
                left += 1
            if total == target:
                length = right - left + 1
                if best[left] != INF:
                    answer = min(answer, length + best[left])
                best[right + 1] = min(best[right], length)
            else:
                best[right + 1] = best[right]
        if answer == INF:
            return -1
        return answer