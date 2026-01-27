class Solution:
    def maxArea(self, height: List[int]) -> int:
        #[1,8,6,8,7]
        l,r = 0, len(height) -1
        res = 0 
        while l<r:
            curr_h = min(height[l],height[r])
            curr_w = r-l
            res = max(res,curr_h*curr_w)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res 



        