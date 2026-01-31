class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Write algo to determine time taken for some eating speed n
        def timeToEatBanana(n):  
            t = 0 
            for pile in piles:
                t+= (pile+n-1) // n
            return t 

        l,r = 1,max(piles)

        res = 0
        while r>=l:
            m = ((r-l) // 2) + l
            time = timeToEatBanana(m)
            if time <= h:
                r = m - 1
                res = m
            else:
                l = m + 1
        return res 
        
