class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        group = [0] * n

        current_group = 0

        for i in range(1, n):

            if nums[i] - nums[i - 1] > maxDiff:
                current_group += 1

            group[i] = current_group

        answer = []

        for u, v in queries:

            if group[u] == group[v]:
                answer.append(True)
            else:
                answer.append(False)

        return answer