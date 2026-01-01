class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r= 0, len(nums)- 1 
        minval = nums[0] 
        while l <= r:
            m = (l + r) // 2 
            if nums[l] < nums[r]:
                minval = min(minval, nums[l])
                break
            minval = min(minval, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1 

        return minval