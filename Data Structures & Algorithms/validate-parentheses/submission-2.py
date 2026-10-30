class Solution:
    def isValid(self, s: str) -> bool:
        # O(n)
        # hashmap and stack
        hashMap = {"}":"{",")":"(","]":"["}
        stack = []

        if s is None:
            return True
        
        for char in s:
            if char in hashMap:
                    if stack and stack[-1] == hashMap[char]:
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(char)
        
        return True if not stack else False

        