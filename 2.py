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


def nodes2int(lst):
    return int("".join([str(x) for x in reversed(nodes2list(lst))]))


l1 = [2, 4, 3]
l2 = [5, 6, 4]

l1 = list2nodes(l1)
l2 = list2nodes(l2)

# Actual logic starts here
out = list2nodes(reversed(list(str(nodes2int(l1) + nodes2int(l2)))))

print(list(out))