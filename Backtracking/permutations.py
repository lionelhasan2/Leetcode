class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(path,take):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if not take[i]:
                    path.append(nums[i])
                    take[i] = True
                    backtrack(path,take)

                    path.pop()
                    take[i] = False
        
        backtrack([], [False] * len(nums))
        return res
                    
