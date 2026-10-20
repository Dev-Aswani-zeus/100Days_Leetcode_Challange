class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        prefix_max = [0] * (n + 1)

        for i in range(n):
            prefix_max[i + 1] = max(prefix_max[i], nums[i])
        prefix_min = [10**9] * (n + 1)

        for i in range(n - 1, -1, -1):
            prefix_min[i] = min(nums[i], prefix_min[i + 1])
        drops = [0] * n
        for i in range(1, n):
            drops[i] = drops[i - 1]

            if nums[i - 1] > nums[i]:
                drops[i] += 1

        def check(k):
            for start in range(0, n, k):
                end = start + k - 1
                count = drops[end] - drops[start]

                if nums[end] > nums[start]:
                    count += 1
                if count > 1:
                    return False
                if prefix_max[start] > prefix_min[start]:
                    return False

            return True

        answer = 0
        i = 1
        while i * i <= n:
            if n % i == 0:
                if check(i):
                    answer += i
                other = n // i

                if other != i:
                    if check(other):
                        answer += other
            i += 1
        return answer