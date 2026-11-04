import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

        words = re.findall(r'[a-zA-Z0-9]+', s)
        clean_text = "".join(words).lower()
        
        left = 0
        right = len(clean_text) - 1
        
        while left < right:
            if clean_text[left] == clean_text[right]:
                print(clean_text[left])
                print(clean_text[right])
                left += 1
                right -= 1
                continue
            else:
                return False
        
        return True

        
        