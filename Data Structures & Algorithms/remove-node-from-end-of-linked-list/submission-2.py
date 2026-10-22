# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        next_node = head
        length = 0

        while next_node:
            length += 1
            next_node = next_node.next
        
        del_node = length - n

        if del_node == 0:
            # print("hit")
            if length == 1:
                return None
            else:
                head = head.next
            return head

        next_node = head
        i = 0
        while next_node:
            if i == del_node - 1:
                next_node.next = next_node.next.next
            next_node = next_node.next
            i += 1
            
        return head