class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Store the positions where each number appears
        positions = {}

        for i in range(n):
            if nums[i] not in positions:
                positions[nums[i]] = []

            positions[nums[i]].append(i)

        answer = -1

        # Check every different number
        for num in positions:
            pos = positions[num]

            # Number of possible subarrays of size k
            last_start = n - k

            count = 0

            # Find the ranges of starting positions
            # of subarrays that contain this number
            start = max(0, pos[0] - k + 1)
            end = min(pos[0], last_start)

            for i in range(1, len(pos)):
                new_start = max(0, pos[i] - k + 1)
                new_end = min(pos[i], last_start)

                # If the new range is separate
                if new_start > end + 1:
                    count += end - start + 1
                    start = new_start
                    end = new_end
                else:
                    # Merge the ranges
                    end = max(end, new_end)

            # Add the final range
            count += end - start + 1

            # Appears in exactly one subarray
            if count == 1:
                answer = max(answer, num)

        return answer