# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #nov 16 recursion
        def add(l1, l2, carry):
            if not l1 and not l2 and not carry:
                return

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            carry, s = divmod(v1 + v2 + carry, 10)

            next_node = add(l1.next if l1 else None,
                            l2.next if l2 else None,
                            carry
                            )
            return ListNode(val=s, next=next_node)

        return add(l1, l2, 0)