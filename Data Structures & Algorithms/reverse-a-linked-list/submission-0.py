class ListNode:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = head

        prev = None

        # 0 -> 1 -> 2 -> 3 -> None
        
        # I need to update the current state 

        # None <- 0 -> 1

        cur = tmp
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur 
            cur = next
        return prev

        