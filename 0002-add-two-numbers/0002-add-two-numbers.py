# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        hap = 0  # 다음거에 더해줄 올림수
        x = ListNode()  # 맨 처음 값
        first = x  # 맨 첫번째 값을 return 해야함
        
        while l1 or l2 or hap:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            newNode = ListNode()
            newNode.val = (a+b+hap) % 10
            x.next = newNode
            hap = int((a+b+hap) / 10)

            # 얘네들을 꼭 해야됨
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            if x:
                x = x.next

        return first.next