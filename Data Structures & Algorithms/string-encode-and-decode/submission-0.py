class Solution:

    def encode(self, strs: List[str]) -> str:
        sentinel = "."
        finalStr = ""
        for s in strs:
            s += sentinel
            finalStr+=s
        return finalStr

    def decode(self, s: str) -> List[str]:
        finalStrList = []
        lP = 0
        rP = 1
        for i in range(0, len(s)):
            if s[i] == ".":
                rP = i - 1
                finalStrList.append(s[lP:i])
                lP = i+1
        return finalStrList

