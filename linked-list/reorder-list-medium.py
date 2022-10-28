# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #find middle
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            #break needed for even length lists
            if not fast:
                break
            slow = slow.next
            
        
        #reverse second half
        first = None
        second = None
        third = slow.next
        slow.next = None #this is the new end of the list
        
        while third:
            first = second
            second = third
            third = third.next
            second.next = first
        
        #merge two lists
        list1 = head
        list2 = second
        while list2:
            tmp1 = list1.next
            list1.next = list2
            tmp2 = list2.next
            list2.next = tmp1
            list1 = tmp1 
            list2 = tmp2
        return head
