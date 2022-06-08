
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1=ListNode(3)
h2=ListNode(1,h1)
h3=ListNode(2,h2)
h4=ListNode(4,h3)
head=ListNode(1,h4)



def insertionSortList(head):
    dummyHead = ListNode(next=head)
    cur = head
    begin = dummyHead

    while cur.next != None:
        nex = cur.next
        if cur.val > nex.val:
            while (begin.next.val < nex.val):
                begin = begin.next

            cur.next = nex.next
            nex.next = begin.next
            begin.next = nex
            begin = dummyHead
        else:
            cur = cur.next

    return dummyHead.next

if __name__ == '__main__':
    insertionSortList(h4)