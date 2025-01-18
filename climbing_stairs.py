"""
thought process:
we use the same approach as fibonacci sequence, we know fibonnaci sequence is a sequence of numbers where each number is the sum of the two preceding ones,
starting from 0 and 1.
and the ways of climbing 2 stairs is the sum of the ways of climbing 1 stair and the ways of climbing 2 stairs., so also the
the ways of climbing n stairs is the sum of the ways of climbing n-1 stairs and the ways of climbing n-2 stairs.
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0,1

        while n > 0:
            a ,b = b, a+b
            n -= 1
        return b