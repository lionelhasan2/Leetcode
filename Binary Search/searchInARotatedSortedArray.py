class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Determine which half is sorted, so we can check if target is within that half
            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target is in sorted left half
                else:
                    l = m + 1  # Target is in right half
            else:  # Right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target is in sorted right half
                else:
                    r = m - 1  # Target is in left half
        
        return -1

