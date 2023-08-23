# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        minHeap = []
        for idx, lst in enumerate(lists):
            if l:
                heapq.heappush(minHeap, (lst.val, idx, lst))
        
        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            curr.next = node
            curr = curr.next
        
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
            
        return dummy.next