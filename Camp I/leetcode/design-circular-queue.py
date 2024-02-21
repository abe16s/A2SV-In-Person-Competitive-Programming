class ListNode():
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyCircularQueue:
    def __init__(self, k: int):
        self.k = k
        self.head = ListNode()
        self.tail = self.head

    def enQueue(self, value: int) -> bool:
        if self.k == 0:
            return False
        self.tail.next = ListNode(value)
        self.tail = self.tail.next
        self.k -= 1
        return True

    def deQueue(self) -> bool:
        if not self.head.next:
            return False
        self.head.next = self.head.next.next
        self.k += 1
        if not self.head.next:
            self.tail = self.head
        return True

    def Front(self) -> int:
        if self.head.next:
            return self.head.next.val
        return -1

    def Rear(self) -> int:
        if self.head.next:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return not self.head.next

    def isFull(self) -> bool:
        return self.k == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()