class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        # Find correct row
        t, b = 0, len(matrix) - 1
        while t < b:
            mid = (t + b + 1) // 2
            if matrix[mid][0] <= target:
                t = mid
            else:
                b = mid - 1
        
        row = t
        
        # Binary search in row
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False