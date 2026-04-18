class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)
        ans = []
        counter = 0
        sortedFreq = sorted(freqMap.items(), key=lambda x: x[1])
        while counter < k:
            lastTuple = sortedFreq[len(sortedFreq)-(counter+1)]
            ans.append(lastTuple[0])
            counter+=1
        return ans

