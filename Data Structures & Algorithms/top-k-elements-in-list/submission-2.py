class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = defaultdict(int)
        solution = []

        for num in nums:
            freqMap[num] += 1

        sortedMap = sorted(freqMap, key = freqMap.get, reverse=True)

        for i in range(k):
            solution.append(sortedMap[i])

        return solution

            





