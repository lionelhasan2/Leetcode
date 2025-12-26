class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        max_len = 0
        c_set = set()
        while r < len(s):
            # Case 1 : r is already in char set therefore we need to shrink the sliding window and remove it from the set (to be replaced)
            while s[r] in c_set:
                c_set.remove(s[l])
                l += 1
            # Case 2: Not in set therefore add it to the set and expand the window 
            c_set.add(s[r])
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len
        
#abcabcbb
#bbbbbb