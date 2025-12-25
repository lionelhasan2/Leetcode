class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r  = 0, 1
        max = 0
        while r<len(prices):
            if prices[r] - prices[l] > max:
                max = prices[r] - prices[l]
            if prices[l] > prices[r]:
                l = r
            r += 1
        return max

            
            
            


            
