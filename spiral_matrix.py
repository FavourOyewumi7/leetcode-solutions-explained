"""
Thought Process:

1. Use four pointers to represent the top, left, right, and bottom of the matrix
2. Traverse the matrix in a spiral order, appending the elements to the result list
3. Update the pointers after each traversal
4. Continue until all elements have been traversed
5. Return the result list
"""

class Solution:
    def spiralOrder(self, matrix):
        res = []
        m,n = len(matrix), len(matrix[0])

        t,l,r,b = 0,0,n-1, m-1

        while len(res) < m*n:
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t += 1

            for j in range(t, b+1):
                res.append(matrix[j][r])
            r -= 1
            if t <= b:
                for k in range(r, l-1, -1):
                    res.append(matrix[b][k])
                b -= 1
            if l <= r:
                for w in range(b, t-1, -1):
                    res.append(matrix[w][l])
                l += 1
        return res

