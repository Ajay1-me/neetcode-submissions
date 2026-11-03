# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Use two pointers to track which node has been visited

        # one pointer stays at one node and other pointer iterates until they find the same node  
        seen, curr = head, head
        while curr and curr.next:
            seen = seen.next
            curr = curr.next.next
            if seen == curr:
                return True
        return False