"""
thought process:
1. iterate through the array
2. if the current value is less than 0, reset the current value to the current value
3. if the current value is greater than 0, add the current value to the current value
4. update the result with the maximum of the current value and the result
5. return the result

(kadane's algorithm)
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        val = nums[0]
        for i in range(1, len(nums)):
            if val < 0:
                val = nums[i]
            else:
                val += nums[i]
            res = max(val, res)
        return res
        