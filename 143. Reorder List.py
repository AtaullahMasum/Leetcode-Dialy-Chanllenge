# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        curr = slow.next
        slow.next = None  # Break the list into two halves
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Step 3: Merge the first half and the reversed second half of the linked list
        first_half = head
        second_half = prev
        while second_half:
            next_node_1 = first_half.next
            next_node_2 = second_half.next
            first_half.next = second_half
            second_half.next = next_node_1
            first_half = next_node_1
            second_half = next_node_2
        