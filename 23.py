class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def list2nodes(lst):
    linked = temp = ListNode()  # Use a temporary variable, so we don't have to use recursion

    for e in lst:
        temp.next = ListNode(e)
        temp = temp.next

    return linked.next  # Skip the empty node


def nodes2list(linked):
    lst = []

    while linked:
        lst.append(linked.val)
        linked = linked.next

    return lst

lists = [list2nodes([1,4,5]), list2nodes([1,3,4]), list2nodes([2,6])]

# Actual logic starts here
flattened = []
for l in lists:
    flattened.extend(nodes2list(l))

out = list2nodes(sorted(flattened))
print(out)
