# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 하나짜리인 경우를 대비해 head 앞 dummy 생성
        dummy = ListNode(0, head)
        
        # 길이 측정
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        cnt = 0
        cur = dummy
        while cur:
            if cnt == length - n:
                break
            cur = cur.next
            cnt += 1
        
        cur.next = cur.next.next

        return dummy.next
