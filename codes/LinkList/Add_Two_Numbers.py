#define linklist class

class LinkNode:
    def __init__ (self, val=0,next=None):
        self.val=val
        self.next=next
class Solution:
    def addTwoNumbers(self,l1:LinkNode,l2:LinkNode):
        dummy = LinkNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry :
            v1 =l1.val if l1 else 0
            v2 =l2.val if l2 else 0

            total = v1+v2+carry
            carry = total // 10
            curr.next = LinkNode(total%10)

            curr = curr.next

            if l1:l1=l1.next
            if l2:l2=l2.next

        return dummy.next

#to convert list to link list
def build_linked_list(arr):
    dummy = LinkNode()
    curr = dummy
    for num in arr:
        curr.next = LinkNode(num)
        curr = curr.next
    return dummy.next


l1 = build_linked_list([1,2,3])
l2 = build_linked_list([3,4,5])

result = Solution().addTwoNumbers(l1, l2)

#to show output in linklis format
def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_list(result)
