class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0

        map = {} 
        def dfs(i):
            if i == len(s):
                return 1 
            if s[i] == '0':
                return 0
            if i in map:
                return map[i]
            res = dfs(i + 1)
            if i + 1 < len(s) and int(s[i:i + 2]) <= 26:
                res += dfs(i + 2)
            map[i] = res
            return res
        return dfs(0)
    
    