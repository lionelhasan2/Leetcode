class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(openN,closeN,path):
            if openN == closeN == n:
                res.append("".join(path[:]))
                return
            
            if openN < n:
                path.append("(")
                backtracking(openN+1,closeN,path)
                path.pop()
            if closeN < openN:
                path.append(")")
                backtracking(openN, closeN+1,path)
                path.pop()
            return
        backtracking(0,0,[])
        return res