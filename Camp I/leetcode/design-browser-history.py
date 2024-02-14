class ListNode:
    def __init__(self, val=""):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:
    def __init__(self, homepage: str):
        self.backward = ListNode(homepage)
        self.forward11 = ListNode()

    def visit(self, url: str) -> None:
        newUrl = ListNode(url)
        self.backward.next = newUrl
        newUrl.prev = self.backward
        self.backward = newUrl
        self.forward11 = ListNode()

    def back(self, steps: int) -> str:
        while steps and self.backward.prev:
            self.forward11.prev = self.backward
            self.backward.next = self.forward11
            self.forward11 = self.forward11.prev
            self.backward = self.backward.prev
            self.backward.next = None 
            self.forward11.prev = None
            steps -= 1
        return self.backward.val

    def forward(self, steps: int) -> str:
        while steps and self.forward11.next:
            self.backward.next = self.forward11
            self.forward11.prev = self.backward
            self.backward = self.backward.next
            self.forward11 = self.forward11.next
            self.backward.next = None
            self.forward11.prev = None
            steps -= 1
        return self.backward.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)