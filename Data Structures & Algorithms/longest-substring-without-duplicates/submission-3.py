class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        left = 0
        longestSubstring = 0

        for sub in range(len(s)):
            while s[sub] in store:
                store.remove(s[left])
                left += 1
            store.add(s[sub])
            long = (sub - left) + 1
            longestSubstring = max(long, longestSubstring)


        return longestSubstring                
        