# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Given any singley linked list re order them using [0, n-1, 1, n-2,3,n-3...] 
        # split list in half using fast and slow pointers > reverse the second list > merge first and second 
        if not head or not head.next:
            return
        slow = head
        fast = head.next
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
            ## when fast is EMPTY and while loop breaks, slow is at the last of the first half. 
        second = slow.next
        slow.next = None    
        first = head
        # Now lists are cut, revser the second then merge
        cur = second
        prev = None
        while cur: 
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        ## second is reversed so merge
        second = prev
        while first and second: 
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next



        


            