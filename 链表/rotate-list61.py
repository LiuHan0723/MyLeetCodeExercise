class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1=ListNode(5)
h2=ListNode(4,h1)
h3=ListNode(3,h2)
h4=ListNode(2,h3)
head=ListNode(1,h4)


def rotateRight(head, k):
    if k == 0:
        return head

    p1 = head
    fix = head
    length = 0
    while head != None:
        length += 1
        head = head.next

    if length == 0 or length == 1:
        return head

    times = k % length

    if times == 0:
        return head

    p2 = p1
    while times:
        p2 = p2.next
        times -= 1
    while p2.next:
        p1 = p1.next
        p2 = p2.next
    new_head = p1.next
    p2.next=fix
    p1.next = None

    return new_head

if __name__ == '__main__':
    rotateRight(head,2)