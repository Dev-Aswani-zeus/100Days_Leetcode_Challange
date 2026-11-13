from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()
        cost = 0
        answer = 0
        right = n - 1
        for left in range(n - 1, -1, -1):
            while dq and nums[dq[-1]] < nums[left]:
                index = dq.pop()
                if dq:
                    previous = dq[-1]
                else:
                    previous = right + 1

                cost += (previous - index) * (nums[left] - nums[index])
            dq.append(left)
            while cost > k:
                cost -= nums[dq[0]] - nums[right]
                if dq[0] == right:
                    dq.popleft()
                right -= 1
            answer += right - left + 1

        return answer