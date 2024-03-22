# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, prev=None):
        if not head:
            return prev
        next = head.next
        head.next = prev
        return self.reverse(next, head)
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the linked list
        second_half = self.reverse(slow)
        # Compare the first half with the reversed second half
        first_half = head
        while second_half:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next
        return True
        