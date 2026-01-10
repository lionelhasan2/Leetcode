class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }
        for char in s:
            if char in map.keys():
                stack.append(char)
            elif len(stack) <=0:
                return False
            elif char != map[stack.pop()]:
                return False
        return len(stack) == 0