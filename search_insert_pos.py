"""
Thought Process:
1. Use binary search to find the target in the array
2. If the target is not found, return the index where it should be inserted which is the left side
3. If the target is found, return the index of the target
"""

class Solution:
    def searchInsert(self, nums, target):

        j = len(nums)-1
        i = 0
        while i <= j:
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                j = mid-1
            else:
                i = mid + 1
        return i
        
        
        