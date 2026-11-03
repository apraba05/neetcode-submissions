from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each of the strs
        # and then check if they match and if they do 
        # add the index of that to a hashmap
        # return the values of the hashmap

        if strs == [""]:
            return [[""]]
        hashMap = defaultdict(list)

        
        

        for i, char in enumerate (strs):
            newChar = "".join(sorted(char))
            hashMap[newChar].append(char)
        
        return list(hashMap.values())