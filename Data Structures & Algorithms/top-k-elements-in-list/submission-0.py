from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for num in nums:
            freq_map[num] += 1

        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))  # Heaps sort by the first item in a tuple.
            # We push (frequency, number) so it sorts by frequency.

            if len(heap) > k:
                heapq.heappop(
                    heap
                )  ## when we have atleast k items, kick out the furthest right of a minHeap as it's the smallest frequency

            res = []
        for pair in heap:
            res.append(pair[1])
        return res
