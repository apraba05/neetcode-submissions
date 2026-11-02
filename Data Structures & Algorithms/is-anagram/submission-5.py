class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # r a c e c a r
        # c a r r a c e

        if len(s) != len(t):
            return False
        
        newS = sorted(s)
        newT = sorted(t)
        
        return newS == newT

        