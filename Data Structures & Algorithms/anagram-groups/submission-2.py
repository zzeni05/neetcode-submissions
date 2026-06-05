class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        charDict = defaultdict(list)
        solution = []

        for str in strs:
            count = [0] * 26

            for char in str:
                count[ord(char) - ord('a')] += 1

            charDict[tuple(count)].append(str)

        return list(charDict.values())