class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        # Keep original index
        arr = []
        for i, interval in enumerate(intervals):
            l, r, w = interval
            arr.append((l, r, w, i))

        # Sort by ending position
        arr.sort(key=lambda x: x[1])

        # previous[i] = first interval we can use before arr[i]
        previous = [0] * n

        for i in range(n):
            l = arr[i][0]

            left = 0
            right = i - 1
            pos = -1

            while left <= right:
                mid = (left + right) // 2

                if arr[mid][1] < l:
                    pos = mid
                    left = mid + 1
                else:
                    right = mid - 1

            previous[i] = pos + 1

        # dp[i][k] = (maximum score, indices)
        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            l, r, w, original_index = arr[i - 1]

            for k in range(1, 5):

                # Option 1: don't take this interval
                best = dp[i - 1][k]

                # Option 2: take this interval
                old_score, old_indices = dp[previous[i - 1]][k - 1]

                new_score = old_score + w
                new_indices = tuple(sorted(old_indices + (original_index,)))

                if new_score > best[0]:
                    best = (new_score, new_indices)

                elif new_score == best[0] and new_indices < best[1]:
                    best = (new_score, new_indices)

                dp[i][k] = best

        return list(dp[n][4][1])