class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        zero = nums.index(0)
        def check(step):
            for i in range(1, n):
                previous = (zero + (i - 1) * step) % n
                current = (zero + i * step) % n
                if nums[previous] > nums[current]:
                    return False
            return True
        answer = float('inf')
        if check(1):
            answer = min(answer, zero)
            answer = min(answer, n - zero + 2)
        if check(-1):
            answer = min(answer, zero + 2)
            answer = min(answer, n - zero)
        if answer == float('inf'):
            return -1
        return answer