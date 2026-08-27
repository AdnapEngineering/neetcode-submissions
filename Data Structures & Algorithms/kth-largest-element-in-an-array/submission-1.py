import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ##min heap of size k so root is at the top
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap,num)
        return heap[0]        