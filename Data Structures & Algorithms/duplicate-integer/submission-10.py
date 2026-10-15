from collections import defaultdict

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freqMap = defaultdict(int)

        for n in nums: 
            freqMap[n] += 1
        
        for n in nums:
            if freqMap[n] >= 2:
                return True
        
        return False