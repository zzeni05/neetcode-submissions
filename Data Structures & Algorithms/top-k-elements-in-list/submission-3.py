class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        solution = []

        for num in nums:
            freqMap[num] += 1

        minHeap = []

        for num in freqMap:
            heapq.heappush(minHeap, (freqMap[num], num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        minHeapSize = len(minHeap)
        for i in range(minHeapSize):
            solution.append(heapq.heappop(minHeap)[1])

        return solution



            





