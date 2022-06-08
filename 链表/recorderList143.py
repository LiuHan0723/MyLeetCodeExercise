class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1=ListNode(5)
h2=ListNode(4,h1)
h3=ListNode(3,h2)
h4=ListNode(2,h3)
head=ListNode(1,h4)
def reorderList(head):
    """
    Do not return anything, modify head in-place instead.
    """
    myhead = head
    p1 = head
    p2 = head

    while p2 and p2.next:
        p1 = p1.next
        p2 = p2.next.next

    pre = None
    cur = p1

    while cur:
        nex = cur.next
        cur.next = pre
        pre = cur
        cur = nex

    newhead = myhead
    while myhead and pre:

        if myhead==pre or myhead.next==pre:
            return newhead
        n1=myhead.next
        n2=pre.next
        myhead.next=pre
        pre.next=n1
        pre=n2
        myhead=n1

    return newhead

if __name__ == '__main__':
    reorderList(h4)