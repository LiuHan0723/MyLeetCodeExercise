
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        if self.val < other.val:
            return True
        else:
            return False

h1=ListNode(3)
h2=ListNode(1,h1)
h3=ListNode(2,h2)
h4=ListNode(4,h3)
head=ListNode(5,h4)

def sortList(head):
    sort=split(head, None)
    return sort.val
def split(head, tail):
    p1 = head
    p2 = head
    if not head:
        return head

    if head.next==tail:
        head.next=None

        return head

    while p2 != tail and p2.next != tail:
        p1 = p1.next
        p2 = p2.next.next

    # while p2!=tail:
    #     p1 = p1.next
    #     p2 = p2.next
    #     if p2!=tail:
    #         p2=p2.next

    sorted_head1 = split(head, p1)
    sorted_head2 = split(p1, tail)
    return merge(sorted_head1, sorted_head2)


def merge(head1, head2):
    dummpyHead = ListNode()
    tmp = dummpyHead
    while head1 and head2:

        if head1.val<head2.val:
            tmp.next=head1
            head1=head1.next

        else:
            tmp.next=head2
            head2=head2.next
        tmp=tmp.next
    if head1:
        tmp.next=head1

    else:
        tmp.next=head2


    return dummpyHead.next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(head1: ListNode, head2: ListNode) -> ListNode:
            dummyHead = ListNode(0)
            temp, temp1, temp2 = dummyHead, head1, head2
            while temp1 and temp2:
                if temp1.val <= temp2.val:
                    temp.next = temp1
                    temp1 = temp1.next
                else:
                    temp.next = temp2
                    temp2 = temp2.next
                temp = temp.next
            if temp1:
                temp.next = temp1
            elif temp2:
                temp.next = temp2
            return dummyHead.next

        if not head:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        dummyHead = ListNode(0, head)
        subLength = 1
        while subLength < length:
            prev, curr = dummyHead, dummyHead.next
            while curr:
                head1 = curr
                for i in range(1, subLength):
                    if curr.next:
                        curr = curr.next
                    else:
                        break
                head2 = curr.next
                curr.next = None
                curr = head2
                for i in range(1, subLength):
                    if curr and curr.next:
                        curr = curr.next
                    else:
                        break

                succ=None
                if curr:
                    succ = curr.next
                    curr.next = None

                merged = merge(head1, head2)
                prev.next = merged
                while prev.next:
                    prev = prev.next
                curr = succ
            subLength <<= 1

        return dummyHead.next

if __name__ == '__main__':

    print(h4<h3)