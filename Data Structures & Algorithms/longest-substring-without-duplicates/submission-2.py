class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        substring = set()
        n = len(s)


        for sub in range(n):
            while s[sub] in substring:
                substring.remove(s[start])
                start += 1
            substring.add(s[sub])
            window = (sub - start) + 1
            longest = max(longest, window)
            

        return longest

        

