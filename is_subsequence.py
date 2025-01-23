class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i, j = 0, 0
        while i <= len(s)-1 and j <= len(t)-1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j+= 1
        if i == len(s):
            return True
        else:
            return False
        