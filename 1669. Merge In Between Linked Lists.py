# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Initialize pointers
        head1 = list1
        head2 = list2
        
        # Move head1 to the node at position a - 1
        for _ in range(a - 1):
            head1 = head1.next
        
        # Move head2 to the last node of list2
        while head2.next:
            head2 = head2.next
        
        # Connect the node at position a - 1 to the head of list2
        connect_start = head1
        head1 = head1.next
        connect_start.next = list2
        
        # Connect the last node of list2 to the node following the node at position b
        for _ in range(b - a + 1):
            head1 = head1.next
        head2.next = head1
        
        return list1
        
        
