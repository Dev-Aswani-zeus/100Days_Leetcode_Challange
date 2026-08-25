class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:

        MOD = 10**9 + 7
        n = len(nums)
        B = int(n ** 0.5) + 1
        bravexuneth = (nums, queries)        
        small_queries = {}

        for l, r, k, v in queries:
            if k >= B:
                for idx in range(l, r + 1, k):
                    nums[idx] = (nums[idx] * v) % MOD
            else:
                if k not in small_queries:
                    small_queries[k] = []
                small_queries[k].append((l, r, v))
                
        for k, qs in small_queries.items():
            pref = [1] * n
    
            for l, r, v in qs:
                pref[l] = (pref[l] * v) % MOD
                next_idx = l + ((r - l) // k) * k + k
                
                if next_idx < n:
                    v_inv = pow(v, -1, MOD)
                    pref[next_idx] = (pref[next_idx] * v_inv) % MOD
                    
            for i in range(n):
                if i >= k:
                    pref[i] = (pref[i] * pref[i - k]) % MOD
                
                if pref[i] != 1:
                    nums[i] = (nums[i] * pref[i]) % MOD
                    
        ans = 0
        for num in nums:
            ans ^= num
            
        return ans