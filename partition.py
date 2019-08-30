# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def partition(self, A, B):
        ans = lessList = ListNode(0)
        dummy = ListNode(0)
        dummy.next = A
        A = dummy
        while A.next:
            print ("Anext: ", A.next.val)
            if A.next.val<B:
                lessList.next = A.next
                lessList = lessList.next
                A.next = A.next.next
                print ("Anext: ", A.next.val)
                lessList.next = None
                print ("Less:", lessList.val)
            else:
                A = A.next
        lessList.next = dummy.next        
        return ans.next

a = ListNode(1)
a.next = ListNode(2)
a.next.next = ListNode(3)

s = Solution()
ans = s.partition(a, 3)

while ans:
    print (ans.val)
    ans = ans.next
