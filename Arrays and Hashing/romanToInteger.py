class Solution:
    def romanToInt(self, s: str) -> int:
        # Add all chars and their values to a dictionary
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            # Check the character and the next
            if i + 1  < len(s) and roman_dict[s[i]] < roman_dict[s[i+1]]:
                total -= roman_dict[s[i]]
            else:
                total += roman_dict[s[i]]
        return total
