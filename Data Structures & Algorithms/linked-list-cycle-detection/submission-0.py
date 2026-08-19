# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # one solution would be to loop through the list and keep a seen Set and for every node, check if seen, if so loop and exit with True. O(N) space
        # O(1) space would be 2 pointer, slow (node.next) and fast node.next.next and exit false when slow == fast
        slow = head
        fast = head
        while fast and fast.next: # avoid NoneType - fast is always first
            fast = fast.next.next
            if fast == slow :
                return True
            slow = slow.next
        return False    