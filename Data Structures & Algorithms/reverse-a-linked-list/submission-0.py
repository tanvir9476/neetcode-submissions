# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        curr = head
        while curr:
            stk.append(curr)
            curr = curr.next
            # print(curr.val)
        # print(stk)
        if not stk:
            return None
        newHead = stk.pop()
        curr = newHead

        while len(stk):
            top = stk.pop()
            curr.next = top
            curr = curr.next
        curr.next = None
        
        return newHead

        