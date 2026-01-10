class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = [-1]*len(nums)
        def dfs(i):
            if i>=len(nums):
                return 0 
            if cache[i]!= -1:
                return cache[i]
            # Rob house i (can only go to i+2) OR skip it (go to i+1)
            rob_current = nums[i] + dfs(i + 2)
            skip_current = dfs(i + 1)
            
            result = max(rob_current, skip_current)
            cache[i] = result
            return result
        return dfs(0)
        