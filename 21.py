class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

l1 = ListNode([1,2,4])
l2 = [1,3,4]

print(sorted(l1 + l2))