class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to group duplicates together
        res = []
        
        def backtrack(i, path):
            if i == len(nums):
                res.append(path[:])  # Copy the path
                return
            
            # Include nums[i]
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()
            
            # Skip nums[i] and all duplicates of it
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            # Don't include nums[i]
            backtrack(i + 1, path)
        
        backtrack(0, [])
        return res