class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i,j):
            if i == len(nums):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            take = 0
            if nums[i] > j:
                take = 1 + dfs(i+1, nums[i])
            notTake = dfs(i+1, j)
            memo[(i,j)] = max(take, notTake)
            return memo[(i,j)]
        
        return dfs(0, float('-inf'))
