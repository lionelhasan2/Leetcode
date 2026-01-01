class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-1):
            target = -nums[i]
            l = i + 1
            r = (len(nums)-1)
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip this i, we already processed this value
            while l < r:
                # Check whether current val + val at i + val at r equal 0
                sum = nums[l] + nums[r]
                if sum > target:
                    # Decrease by moving right pointer backward
                    r -=1
                elif sum < target:
                    # Increase by moving the left pointer forward
                    l +=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                # Progress l and r towards each other

        return res