class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencyMapS = {}
        frequencyMapT = {}

        for char in s:
            if char not in frequencyMapS:
                frequencyMapS[char] = 1
            else:
                frequencyMapS[char] += 1
        for char in t:
            if char not in frequencyMapT:
                frequencyMapT[char] = 1
            else:
                frequencyMapT[char] += 1
        
        if frequencyMapS == frequencyMapT:
            return True
        
        return False