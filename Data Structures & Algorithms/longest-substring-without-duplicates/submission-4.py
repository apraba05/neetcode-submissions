class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxVal = 0
        res = set()

        for char in s:
            while char in res:
                res.remove(s[left])
                left += 1
            res.add(char)
            maxVal = max(maxVal, len(res))

        
        return maxVal
            


            

            
        