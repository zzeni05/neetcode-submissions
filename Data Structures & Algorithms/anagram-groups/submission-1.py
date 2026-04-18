class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        ans = []

        for s in strs:
            sortedWord = ''.join(sorted(s))
            groups[sortedWord].append(s)

        for group in groups.values():
            ans.append(group)

        return ans
        
