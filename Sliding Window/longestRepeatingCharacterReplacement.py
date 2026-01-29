class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        l = 0   
        res = 0
        
        # Iterate through the string with right pointer
        for r in range(len(s)):
            # Add current character to frequency map
            freq[s[r]] = 1 + freq.get(s[r], 0)
            maxf = max(freq.values()) # Determine the max frequency in the current window

            # While the number of characters to change exceeds k, shrink the window from the left
            # Number of chars to change = window size - max frequency char count
            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            # Update the result with the maximum window size found
            res = max(res, r - l + 1)
        return res

