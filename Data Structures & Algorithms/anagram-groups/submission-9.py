from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # G: arr of strings -> strs
        # R: all the anagrams -> sublists
        # A: "act" -> "act" -> "act" -> "cat"
        # Brute Force: iterate through chars
        # subarrays -> O(n^2)
        
        
        strsNew = sorted(strs)
        arr = []
        
        if strs == [""]:
            return [[""]]
        
        hashMap = defaultdict(list)
        

        for i, char in enumerate (strs):
            newChar = "".join(sorted(char))
            hashMap[newChar].append(char)
        

        return list(hashMap.values())