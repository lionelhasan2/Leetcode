class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = [-1]*len(nums)
        def dfs(i,length):
            if i>=length:
                return 0 
            if cache[i] != -1:
                return cache[i]
            max_jump1 = dfs(i+1,length)
            max_jump2 = nums[i]+dfs(i+2,length)
            node_max = max(max_jump1,max_jump2)
            cache[i] = node_max
            return node_max
        
        first_max = dfs(0,len(nums)-1)
        cache = [-1]*len(nums)

        second_max = dfs(1,len(nums))
        return max(first_max,second_max)