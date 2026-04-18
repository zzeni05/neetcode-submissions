class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = dict()
        tDict = dict()
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1
        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1
        if (sDict == tDict):
            return True
        else:
            return False


        