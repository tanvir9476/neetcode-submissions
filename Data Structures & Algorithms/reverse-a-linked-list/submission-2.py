# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # october 16 2026
        # I traverse each node from head, 
        # While its not None
        # I remember the next node
        # change the pointer to the prev node
        # change the current to the old next node
        prev = None
        curr = head
        while curr:
            old_nxt = curr.next
            curr.next = prev
            prev = curr
            curr = old_nxt
        return prev #return prev because curr is now None