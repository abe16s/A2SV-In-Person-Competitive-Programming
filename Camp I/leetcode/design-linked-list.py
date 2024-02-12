class Node:
    def __init__(self, e):
        self.val = e
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        i = 0
        cur = self.head
        while cur and i < index:
            i += 1
            cur = cur.next
        if cur:
            return cur.val
        return -1

    def addAtHead(self, val: int) -> None:
        temp = self.head
        self.head = Node(val)
        self.head.next = temp

    def addAtTail(self, val: int) -> None:
        cur = self.head
        if not cur:
            self.head = Node(val)
            return
        while cur and cur.next:
            cur = cur.next
        cur.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
            return
        i = 0
        cur= self.head
        while cur and i < index-1:
            cur = cur.next
            i += 1
        if not cur:
            return
        temp = cur.next
        cur.next = Node(val)
        cur.next.next = temp
        
    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
            return 
        i = 0
        cur= self.head
        while i < index - 1:
            cur = cur.next
            i += 1 
        if cur and cur.next:
            cur.next = cur.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)