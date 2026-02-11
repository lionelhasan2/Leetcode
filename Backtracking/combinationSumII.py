class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Backtracking Algorithm
        res = []
        candidates.sort()
        def backtrack(i,path,total):
            # Base Cases
            if total == target:
                res.append(path[:])
                return
            if total > target or i > len(candidates)-1:
                return
            
            # i 
            for j in range(i,len(candidates)):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                path.append(candidates[j])
                backtrack(j+1,path,total + candidates[j])
                path.pop()
            
        backtrack(0,[],0)
        return res 

