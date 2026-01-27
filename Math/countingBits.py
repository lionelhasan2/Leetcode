class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [-1] * (n+1)
        res_array = [0] * (n+1)
        for i in range(n+1):
            if dp[i-4] != -1:
                res_array[i] = 1 + dp[i-4]
            temp = i 
            while temp != 0:
                if temp & 1:
                    res_array[i] += 1
                temp = temp >> 1
            dp[i] = res_array[i]

        return res_array
    
    #3 011 