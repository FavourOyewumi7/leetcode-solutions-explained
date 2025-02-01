"""
Thought process:
1. Create a dummy node to store the result
2. Iterate through both lists and compare the values
3. Append the smaller value to the result list
4. Append the remaining elements of the non-empty list to the result list
5. Return the result list
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        res = ListNode()
        head = res

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                temp = list1
                list1 = list1.next
                temp.next = None
                res.next = temp
            else:
                temp = list2
                list2 = list2.next
                temp.next = None
                res.next = temp
            res = res.next
                
        if list1 != None:
            res.next = list1
        if list2 != None:
            res.next = list2
        return(head.next)

        