class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        other_index = [0] * n
        for i in range(n):
            other_index[(i+k)% n] = nums[i]
        
        nums[:] = other_index
