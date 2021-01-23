class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
head = ListNode(1)


ans = ""
while(head):
      ans += str(head.data)
      head = head.next
print(ans)
# ans = ""
# for x in head:
#     ans += str(x)
# print(int(ans, 2))