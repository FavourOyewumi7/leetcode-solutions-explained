"""
thought process:

1. check if the length of the strings are the same, if not return false
2. create two dictionaries, one to keep track of the mapping from s to t, and one to keep track of the mapping from t to s
3. iterate through the strings, and for each character, check if it is in the dictionary, if not, add it to the dictionary
4. if it is in the dictionary, check if the mapping is correct, if not return false
5. if the mapping is correct, return true

"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        keep = {}
        keep_inv = {}

        if len(s) > len(t) or len(t) > len(s):
            return False

        for x,y in zip(s,t):
            if x not in keep and y not in keep_inv:
                keep[x] = y
                keep_inv[y] = x
            elif keep.get(x) != y or keep_inv.get(y) != x:
                return False
        return True