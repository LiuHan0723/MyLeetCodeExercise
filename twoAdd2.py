
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1=ListNode(5)
h2=ListNode(2,h1)
h3=ListNode(3,h2)
h4=ListNode(4,h3)
head=ListNode(1,h4)

l1=ListNode(9)
l2=ListNode(9,l1)
L1=ListNode(9,l2)

l1_=ListNode(9)
l2_=ListNode(9,l1_)
L2=ListNode(5,l2_)

def addTwoNumbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """

    myList = ListNode()
    carry = 0
    tmpList = myList
    while l1 != None or l2 != None or carry!=0:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        lv = (v1 + v2+carry) % 10

        carry = 1 if (v1+v2+carry) >= 10 else 0

        lvlist = ListNode(lv)
        tmpList.next = lvlist
        tmpList = lvlist

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return myList.next


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """

    myHead1 = ListNode()
    tmp1 = myHead1
    myHead2 = ListNode()
    tmp2 = myHead2
    while head != None:

        if head.val < x:
            tmp1.next = head
            tmp1 = tmp1.next
        else:
            tmp2.next = head
            tmp2 = tmp2.next

        head = head.next

    tmp2.next = None
    tmp1.next = myHead2
    return myHead1.next

if __name__ == '__main__':
    partition(head,3)