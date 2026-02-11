class Solution(object):
    def mergeTwoLists(self, list1, list2):
        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        dummy = cur = ListNode(0)
        for v in arr:
            cur.next = ListNode(v)
            cur = cur.next

        return dummy.next
