class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = [0,1,0,3,12]
        # nums = [1,3,12,0,0]
        # Want zeroes to drift towards the right, need to find next valid

        l = 0
        for r in range(1,len(nums)):
            if nums[l] == 0:
                if nums[r] != 0:
                    nums[l] = nums[r]
                    nums[r] = 0 
                    l += 1
            else:
                l += 1
        return None

