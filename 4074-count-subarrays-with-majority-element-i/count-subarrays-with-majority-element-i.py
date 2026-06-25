class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # answer = 0
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         target_count = 0
        #         length = j - i + 1
        #         for k in range(i, j + 1):
        #             if nums[k] == target:
        #                 target_count += 1
        #         if target_count > length // 2:
        #             answer += 1
        # return answer


        answer = 0

        for i in range(len(nums)):

            target_count = 0

            for j in range(i, len(nums)):

                if nums[j] == target:
                    target_count += 1

                length = j - i + 1

                if target_count > length // 2:
                    answer += 1

        return answer