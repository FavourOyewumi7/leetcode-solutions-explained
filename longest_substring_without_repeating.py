class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val = 0
        seen = dict()
        cur_val = 0
        start = 0
        for i,val in enumerate(s):
            if val in seen and seen[val] >= start:
                start = seen[val]+1
            seen[val] = i  
            cur_val = i - start+1              
            max_val = max(cur_val, max_val)
        return max_val

            

