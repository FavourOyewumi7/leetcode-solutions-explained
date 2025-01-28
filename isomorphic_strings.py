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