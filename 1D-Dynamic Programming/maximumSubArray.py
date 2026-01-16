class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):  # Start from index 1, not 0
            currMax = max(nums[i], currMax + nums[i])
            result = max(result, currMax)
        
        return result