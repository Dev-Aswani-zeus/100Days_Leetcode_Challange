class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            values = set()
            for j in range(i, len(nums)):
                values.add(nums[j])
                distinct_count = len(values)
                answer += distinct_count * distinct_count
        return answer