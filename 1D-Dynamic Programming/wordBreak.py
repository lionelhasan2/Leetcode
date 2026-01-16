class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #s = "Leetcode"  #dict = "Leet,code"
        dp = {}
        def dfs(i): 
            if i in dp:
                return dp[i]
            if i == len(s):
                return True
            if i > len(s):
                return False
            result = False
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    result = result or dfs(i+len(word))
            dp[i] = result
            return result
        
        return dfs(0)