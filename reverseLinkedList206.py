
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

h1=ListNode(5)
h2=ListNode(4,h1)
h3=ListNode(3,h2)
h4=ListNode(2,h3)
head=ListNode(1,h4)

def reverseList(head,left,right):

    if head==None:
        return None

    head=ListNode(next=head)
    res=head
    cleft=0
    while cleft!=left-1:
        head=head.next
        cleft+=1

    res_n=head
    cur=head.next

    if cur==None:
        return res.next

    nex=head.next.next



    while cleft!=right+1:
        head=head.next
        cleft+=1

    pre=head

    times=0

    while times<(right-left):

        cur.next = pre
        pre = cur
        cur = nex

        nex = nex.next

        times+=1

    cur.next=pre


    # if pre:
    #     right_rv = pre.val
    #     while nex.val !=right_rv:
    #         cur.next = pre
    #         pre = cur
    #         cur = nex
    #
    #         nex = nex.next
    #     cur.next=pre
    #
    # else:
    #     while nex!=None:
    #         cur.next = pre
    #         pre = cur
    #         cur = nex
    #
    #         nex = nex.next
    #     cur.next = pre

    res_n.next=cur
    return res.next

def oddEvenList(head):

    if (head == None or head.next == None or head.next.next == None):
        return head

    l1 = head
    l2 = head.next
    lt1 = l1
    lt2 = l2
    count = 1
    head=head.next.next
    while head != None:
        if count % 2 == 1:
            lt1.next = head
            lt1 = lt1.next

        else:
            lt2.next = head
            lt2 = lt2.next
        count += 1
        head=head.next

    lt2.next=None
    lt1.next = l2
    return l1

if __name__ == '__main__':

    oddEvenList(head)