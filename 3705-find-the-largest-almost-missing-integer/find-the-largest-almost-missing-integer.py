class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        positions = {}
        for i in range(n):
            if nums[i] not in positions:
                positions[nums[i]] = []
            positions[nums[i]].append(i)
        answer = -1
        for num in positions:
            pos = positions[num]
            last_start = n - k
            count = 0
            start = max(0, pos[0] - k + 1)
            end = min(pos[0], last_start)
            for i in range(1, len(pos)):
                new_start = max(0, pos[i] - k + 1)
                new_end = min(pos[i], last_start)
                if new_start > end + 1:
                    count += end - start + 1
                    start = new_start
                    end = new_end
                else:
                    end = max(end, new_end)
            count += end - start + 1
            if count == 1:
                answer = max(answer, num)

        return answer