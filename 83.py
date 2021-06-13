class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(val=1, next=ListNode(val=1, next=ListNode(val=2)))

for 