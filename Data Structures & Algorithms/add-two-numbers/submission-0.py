# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        curr = result
        c = 0
        while l1 or l2 or c:
            sum = c
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            c = sum//10
            s = sum % 10
            sum_node=ListNode(val=s)
            curr.next = sum_node
            curr = curr.next

        curr.next = None
        return result.next