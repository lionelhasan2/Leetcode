class Solution:
    def countSubstrings(self, s: str) -> int:
        visited = set()
        
        def isPalindrome(substring):
            return substring == substring[::-1]
        
        def dfs(l, r):
            # Base case: if we've exhausted all possibilities
            if l > r or l >= len(s):
                return 0
            
            # Check if (l, r) is already visited
            if (l, r) in visited:
                return 0
            
            visited.add((l, r))
            count = 0
            
            # If current substring is palindrome, count it
            if isPalindrome(s[l:r+1]):
                count += 1
            
            # Explore: move right pointer forward (extend current left)
            if r + 1 < len(s):
                count += dfs(l, r + 1)
            
            # Explore: move left pointer forward (new starting position)
            if r + 1 == len(s):  # Only move left when we've exhausted right
                count += dfs(l + 1, l + 1)
            
            return count
        
        # Start with first character
        return dfs(0, 0)