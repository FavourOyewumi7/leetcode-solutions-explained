class Solution:
    def removeElement(self, nums, val):
        i, j = 0, len(nums)-1
        count = 0
        while i <= j:
            if (nums[i] == val and nums[j] != val):
                nums[i], nums[j] =nums[j], nums[i]
                i += 1
                j -= 1
            elif nums[i] == val and nums[j] == val:
                j -= 1
            elif nums[i] != val and nums[j] != val:
                i +=1
            else:
                i += 1
                j -= 1
        for x in nums:
            if x != val:
                count += 1
        return count
        