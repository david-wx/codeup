# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1, p2 = l1[0], l2[0]
        s, c = 0, 0
        head_p, prev_p = None, None

        while p1 or p2 or c:
            if p1 and p2:
                v1, v2 = p1.val, p2.val
            elif p1 and not p2:
                v1, v2 = p1.val, 0
            elif not p1 and p2:
                v1, v2 = 0, p2.val
            elif c:
                v1, v2 = 0, 0
            print(v1,v2,c)
            s, c = (c + v1 + v2) % 10, (c + v1 + v2) // 10
            n = ListNode(s)
            if prev_p is None:
                head_p = n
            else:
                prev_p.next = n
            prev_p = n

            if p1:
                p1=p1.next
            if p2:
                p2=p2.next

        return head_p


def make_sl(l):
    prev_p = None
    node_list = [ListNode(x) for x in l]
    for n_first, n_second in zip(node_list[0:-1], node_list[1:]):
        n_first.next = n_second
    return node_list


def show_sl(l):
    p = l[0]
    while p:
        print("{} , ".format(p.val), end="")
        p = p.next
    print()


def show_slp(l):
    p = l
    while p:
        print("{} , ".format(p.val), end="")
        p = p.next
    print()


if __name__ == '__main__':
    pass
    # print(Solution().addTwoNumbers((2, 7, 11, 15), 9))
    # show_sl
    l1 = make_sl([2, 4, 3,1])
    l2 = make_sl([5, 6, 4])

    show_slp(l1[0])
    show_slp(l2[0])

    l3 = Solution().addTwoNumbers(l1, l2)
    show_slp(l3)
