"""
Thought process:
Using the inbuilt heap, heapify nums and find the kth largest value, since the py heap implementation is a min heap,
I used the length of my list - k to find the kth largest value.
to solve the min heap and turn it to max heap you can multiply all values in the list with -1.
"""
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heapq.heapify(nums)
        ac = len(nums) - k +1
        while ac > 0:
            x = heapq.heappop(nums)
            ac -= 1
        return x
