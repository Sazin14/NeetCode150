# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        temp = dummy
        carry = 0

        while l1 or l2 or carry!= 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + carry
            
            temp.next = ListNode(sum % 10)
            temp = temp.next
            carry = sum//10
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next


# Create l1 = 2 -> 4 -> 3
l1 = ListNode(2, ListNode(4, ListNode(3)))

# Create l2 = 5 -> 6 -> 4
l2 = ListNode(5, ListNode(6, ListNode(4)))



l3 = Solution()
sum_list = l3.addTwoNumbers(l1,l2)
print(sum_list.val)

