class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        candidates.sort()

        def backtrack(i,currList, currTotal):
            # Base case: We passed target or past list
            if currTotal > target or i >= len(candidates):
                return
            # Found target, add to results and return
            if currTotal == target:
                results.append(currList.copy())
                return
            else:
                # Add the current value to the current list because values can be repeated
                currList.append(candidates[i])
                backtrack(i,currList,currTotal + candidates[i])
                # Remove the last value and now check the other paths 
                currList.pop()
                backtrack(i+1,currList,currTotal)

        backtrack(0,[],0)
        return results

            

