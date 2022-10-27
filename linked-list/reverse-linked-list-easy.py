# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        first, second, third = None, None, head
        while third is not None:
            first = second
            second = third
            third = third.next
            second.next = first

        return second 