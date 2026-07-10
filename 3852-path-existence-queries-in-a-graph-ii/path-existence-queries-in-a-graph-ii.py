class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        pairs = sorted((value, index) for index, value in enumerate(nums))

        LOG = 20
        jump = [[0] * LOG for _ in range(n)]

        r = n - 1

        for l in range(n - 1, -1, -1):

            while pairs[r][0] - pairs[l][0] > maxDiff:
                r -= 1

            original_index = pairs[l][1]
            farthest_index = pairs[r][1]

            jump[original_index][0] = farthest_index

            for k in range(1, LOG):
                jump[original_index][k] = jump[jump[original_index][k - 1]][k - 1]

        answer = []

        for u, v in queries:

            if nums[u] > nums[v]:
                u, v = v, u

            if u == v:
                answer.append(0)
                continue

            if nums[u] == nums[v]:
                answer.append(1)
                continue

            distance = 0

            for k in range(LOG - 1, -1, -1):
                if nums[jump[u][k]] < nums[v]:
                    distance += 1 << k
                    u = jump[u][k]

            if nums[jump[u][0]] < nums[v]:
                answer.append(-1)
            else:
                answer.append(distance + 1)

        return answer