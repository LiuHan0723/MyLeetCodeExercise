class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1=ListNode(5)
h2=ListNode(4,h1)
h3=ListNode(3,h2)
h4=ListNode(2,h3)
head=ListNode(1,h4)
def reverse(head ,tail):
    pre =tail.next
    cu =head
    next1 =cu.next

    while pre!=tail:
        cu.next =pre
        pre =cu
        cu =next1
        next1 =next1.next

    return pre ,head

def reverseKGroup(head,k):

    dummyHead =ListNode(next=head)
    cur =dummyHead
    while head!=None:
        tail =cur
        for i in range(k):
            tail =tail.next
            if not tail:
                return dummyHead.next
        nex =tail.next

        head ,tail =reverse(head ,tail)

        cur.next =head
        tail.next =nex
        cur =tail
        head =tail.next

    return dummyHead.next

if __name__ == '__main__':
    reverseKGroup(head,2)