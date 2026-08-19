# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        left = dummy_node
        right = head
        
        # second pointer should be n ahead of first pointer to increment pointers.
        for _ in range(n):
            right = right.next
        while right:
            left = left.next
            right = right.next
        # now left is at the node 1 before the nth node, so cut and move around
        tmp = left.next.next
        left.next = tmp
        return dummy_node.next    

