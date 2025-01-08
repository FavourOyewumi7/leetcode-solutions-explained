"""
Thought process:
1. Create a mapping of digits to letters
2. Iterate through the digits
3. For each digit, get the corresponding letters
4. If the result is empty, set the result to the letters
5. Otherwise, append the letters to the result
6. Return the result
"""
class Solution:
    def letterCombinations(self, digits) :
        mapping = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
            }
        res = []

        for i in range(len(digits)):
            p = digits[i]
            val = mapping[int(p)]

            if not res:
                res = val
                print('val',val)
            else:
                res = [i+j for i in res for j in val]
                print('res',res)
        return res