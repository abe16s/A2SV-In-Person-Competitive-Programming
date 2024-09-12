# Problem: Add Two Numbers II - https://leetcode.com/problems/add-two-numbers-ii/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        cur = l1
        while cur:
            stack1.append(cur.val)
            cur = cur.next
        cur = l2
        while cur:
            stack2.append(cur.val)
            cur = cur.next
        
        ans = ""
        alegn = 0
        while stack1 and stack2:
            cur = stack1.pop() + stack2.pop() + alegn
            if cur >= 10:
                cur -= 10
                alegn = 1
            else:
                alegn = 0
            ans = str(cur) + ans

        while stack1:
            cur = stack1.pop() + alegn
            if cur >= 10:
                cur -= 10
                alegn = 1
            else:
                alegn = 0
            ans = str(cur) + ans
        
        while stack2:
            cur = stack2.pop() + alegn
            if cur >= 10:
                cur -= 10
                alegn = 1
            else:
                alegn = 0
            ans = str(cur) + ans
        
        if alegn:
            ans = "1" + ans

        cout = ListNode()
        cur = cout
        for c in ans:
            cur.next = ListNode(int(c))
            cur = cur.next

        return cout.next

