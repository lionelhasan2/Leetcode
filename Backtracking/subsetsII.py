class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i,path):
            if i == len(nums):
                copy = path.copy()
                res.append(list(copy))
                return
            else:
                if nums[i] not in path:
                    path.add(nums[i])
                    backtrack(i+1,path)
                    path.pop()

                backtrack(i+1,path)
        
        backtrack(0,set())
        return res 
